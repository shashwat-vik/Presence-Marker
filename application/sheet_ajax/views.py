from flask import Blueprint, request, redirect, url_for
from scripts.dhcp_list import DHCP
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

@sheet_ajax_blueprint.route("/{0}/add/<number>".format(base_url))
def add_sheet_ajax(number):
    global sheet_queue
    try:
        number = int(number)
    except ValueError:
        return form_response("A", None)     # INVALID NUMBER
    if number not in sheet_queue.queue:
        sheet_queue.put(number)
        return form_response("B", None)     # ADDED
    return form_response("C", None)         # ALREDY EXISTS

@sheet_ajax_blueprint.route("/{0}/add".format(base_url), methods=["POST"])
def add_client_sheet_ajax():
    global sheet_queue, client_data, client_ips
    ip = request.remote_addr
    role = 100*int(request.form['hund']) + 10*int(request.form['ten']) + int(request.form['zero'])
    if role != 0 and ip not in client_ips.queue:
        client_ips.put(ip)
        client_data.put((ip, role))
        sheet_queue.put(role)
        print (list(client_data.queue))
        #DHCP()
    return redirect(url_for("basic_blue.student_submit"))

@sheet_ajax_blueprint.route("/{0}/display".format(base_url))
def display_sheet_ajax():
    global sheet_queue
    print (list(sheet_queue.queue))
    return ""

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
