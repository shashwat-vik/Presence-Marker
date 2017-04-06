from flask import Blueprint, render_template, redirect, request, url_for
from scripts.create_csv import get_ip_address

basic_blueprint = Blueprint("basic_blue", __name__, template_folder="templates")

base_url = '982aeace73ed943e80b408b12e816f2b'

@basic_blueprint.route("/{0}/attendance_sheet".format(base_url), methods=['POST'])
def attendance_sheet():
    #if request.method == 'GET':
    #    data = {'branch': 'IT', 'end_roll': 15, 'sem': '1', 'sect': 'A', 'start_roll': 1, 'period': 1, 'ip_address' : get_ip_address()}
    #    return render_template("attendance_sheet.html", data=data)
    #print ("{0} - {1} - {2}".format(request.form['sem'], request.form['branch'], request.form['sect']))
    #print ("{0} - {1}".format(request.form['start_roll'], request.form['end_roll']))
    #print (request.form['period'])
    data = {
    'sem' : request.form['sem'],
    'branch' : request.form['branch'],
    'sect' : request.form['sect'],
    'start_roll' : int(request.form['start_roll']),
    'end_roll' : int(request.form['end_roll']),
    'period' : int(request.form['period']),
    'ip_address' : get_ip_address()
    }
    return render_template("attendance_sheet.html", data=data)

@basic_blueprint.route("/")
def student_submit():
    return render_template("student_submit.html")

@basic_blueprint.route("/{0}/create_sheet".format(base_url))
def create_attendance_sheet():
    return render_template("create_attendance_sheet.html")
