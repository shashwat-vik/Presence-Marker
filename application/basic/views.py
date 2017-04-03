from flask import Blueprint, render_template, redirect, request, url_for
from scripts.dhcp_list import DHCP
basic_blueprint = Blueprint("basic_blue", __name__, template_folder="templates")

base_url = '982aeace73ed943e80b408b12e816f2b'

@basic_blueprint.route("/{0}/attendance_sheet".format(base_url), methods=['POST'])
def attendance_sheet():
    print ("{0} - {1} - {2}".format(request.form['sem'], request.form['branch'], request.form['sect']))
    print ("{0} - {1}".format(request.form['start_roll'], request.form['end_roll']))
    print (request.form['period'])
    data = {
    'sem' : request.form['sem'],
    'branch' : request.form['branch'],
    'sect' : request.form['sect'],
    'start_roll' : int(request.form['start_roll']),
    'end_roll' : int(request.form['end_roll'])
    }
    return render_template("attendance_sheet.html", data=data)

@basic_blueprint.route("/")
def student_submit():
    return render_template("student_submit.html")

@basic_blueprint.route("/{0}/create_sheet".format(base_url))
def create_attendance_sheet():
    return render_template("create_attendance_sheet.html")
