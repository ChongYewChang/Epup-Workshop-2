from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import json
from .controller import *

# http://flask.pocoo.org/docs/1.0/tutorial/views/
bp = Blueprint('index', __name__, url_prefix='')

@bp.route('/', methods=['GET'])
def index():
    return welcome()

@bp.route('/select', methods=['GET'])
def select_course():
    # This route populates the dropdowns but largely you dont need to worry about it
    return render_template("index.html",timetable = create_html_select())

@bp.route('/select', methods=['POST'])
def get_class():
    # EDIT THIS FUNCTION TO RETURN THE LIST OF CLASSES FOR A COURSE for your html
    # request.form gets the form data from a http post request
    print(request.form["class 1"])
    print(request.form["class 2"])
    print(request.form["class 3"])
    return redirect(url_for('index.select_time'))

@bp.route('/times', methods=['GET'])
def select_time():
    # you need to render the html and return a dictionary to populate the checkboxes
    return render_template("class_times.html")

@bp.route('/times', methods=['POST'])
def show_timetable():
    # using the inputs from the checkboxes, check if this is a valid timetable
    # else return the string "RIP you have timetable clashes, please try again =("
    return "RIP you have timetable clashes, please try again =("

