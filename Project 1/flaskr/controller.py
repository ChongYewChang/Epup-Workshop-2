import pickle
import datetime
import calendar

def welcome():
    return "Hello World"

def read_timetable():
    """
    @return: offerings(dict) which contains 
    """
    # File I/O
    with open("flaskr/timetable.pickle","rb") as pickle_in:
        offerings = pickle.load(pickle_in)
    #print(offerings)
    return offerings

def create_student_timetable():
    """
    FILL THIS OUT
    @return: timetable(Dict): containing student classes and the corresponding tut/lec
    """
    pass

def get_class_time(schedule):
    """
    FILL THIS OUT
    @args: schedule(String): e.g 'Tue 18-21 (w1-10,Webst ThB)')
    @return: class time(Datetime)
    tips: you can assume that the start of the week is 17/12/2018 and classes only run during this week
    """
    #list(calendar.day_abbr)
    pass

def check_timetable_clash(timetable):
    """
    FILL THIS OUT
    @return: Boolean 
    """
    pass

def create_html_select():
    """
    https://www.w3schools.com/tags/tag_select.asp
    Creates a dictionary to create options for dropdown
    @return: dropdown(dict)
    tips: you may need to write a similar function for creating checkboxes in class_times.html
    """
    subjects = list(read_timetable().keys())
    dropdown = {v:v for v in subjects}
    return dropdown

if __name__ == "__main__":
    print(read_timetable())