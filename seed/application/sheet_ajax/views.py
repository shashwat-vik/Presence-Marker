from flask import Blueprint, request, redirect, url_for
from scripts.dhcp_list import DHCP

from scripts.create_csv import attendance_csv
from scripts.create_csv import ip_role_csv
from scripts.create_csv import dhcp_tp_link_csv

import queue, json

sheet_ajax_blueprint = Blueprint("sheet_ajax", __name__, template_folder="templates")

base_url = '44eee68d93bd9ce7c9eca0047bbdb460'
sheet_queue = queue.Queue()
client_ips = queue.Queue()      # TO ENSURES 1 SUBMISSION PER IP
client_data = queue.Queue()     # KEEPS (IP, ROLL) DATA

status = {
        "A":(101, "INVALID NUMBER",),
        "B":(102, "ADDED"),
        "C":(103, "ALREADY EXISTS"),
        "D":(104, "DELETED"),
        "E":(105, "QUEUE EMPTY"),
        "F":(106, "POLLED")
        }

def form_response(status_idx, data):
    global status
    out = {"status":status[status_idx][0], "data":data}
    return json.dumps(out)

@sheet_ajax_blueprint.route("/{0}/add".format(base_url), methods=["POST"])
def add_client_sheet_ajax():
    global sheet_queue, client_data, client_ips
    ip = request.remote_addr
    #print (request.__dict__)
    #print(ip)
    role = 100*int(request.form['hund']) + 10*int(request.form['ten']) + int(request.form['zero'])
    if role != 0 and ip not in client_ips.queue:
        client_ips.put(ip)
        client_data.put((ip, role))
        sheet_queue.put(role)
        #print (list(client_data.queue))
        #DHCP()
    return redirect(url_for("basic_blue.student_submit"))

@sheet_ajax_blueprint.route("/{0}/submitted_attendance".format(base_url), methods=['POST'])
def submitted_attendance():
    global client_data
    sem = request.form['hid_sem']
    branch = request.form['hid_branch']
    sect = request.form['hid_sect']
    period = request.form['hid_per']
    start_roll = int(request.form['hid_start_roll'])
    end_roll = int(request.form['hid_end_roll'])
    var_id = request.form.getlist("var_id[]")

    present_rolls = set()
    for i in var_id:
        present_rolls.add(int(i[2:]))
    filename = "F:/X/{0}_{1}_{2}_{3}.csv".format(sem, branch, sect, period)
    attendance_csv(filename, sem, branch, sect, period, start_roll, end_roll, present_rolls)

    client_data_sorted_list = sorted(list(client_data.queue), key=lambda x:x[1])
    ip_role_csv('F:/X/ip_role.csv', client_data_sorted_list)

    ip_mac = DHCP()
    dhcp_tp_link_csv('F:/X/dhcp_csv_tp_link.csv', client_data_sorted_list, ip_mac)
    return "<h1>AWESOME !</h1>"

@sheet_ajax_blueprint.route("/{0}/display".format(base_url))
def display_sheet_ajax():
    global sheet_queue
    #print (list(sheet_queue.queue))
    data = {
    "Sheet Queue":list(sheet_queue.queue),
    "Client Data":list(client_data.queue)
    }
    return json.dumps(data, indent=4).replace("\n","<br>").replace(" ","&nbsp")

@sheet_ajax_blueprint.route("/{0}/poll".format(base_url))
def poll_sheet_ajax():
    global sheet_queue
    if not sheet_queue.empty():
        return form_response("F", list(sheet_queue.queue))     # POLLED
    return form_response("E", None)         # QUEUE EMPTY

@sheet_ajax_blueprint.route("/{0}/delete".format(base_url), methods=['POST'])
def delete_sheet_ajax():
    global sheet_queue
    data = request.json
    #print (repr(data))
    #data = json.loads(str(data))
    #print (type(data.get('data')))
    #print (data)
    if not sheet_queue.empty():
        for i in data.get('data'):
            x = sheet_queue.get()
            if x != i:
                sheet_queue.put(x)
        return form_response("D", None)     # DELETED
    return form_response("E", None)         # QUEUE EMPTY
