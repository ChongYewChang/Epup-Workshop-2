import pickle

"""
Exercise - Timetable planner
A course code has a list of lectures and tutorials

User inputs the index to choose a lecture, tutorial and lab if neccesary

When the user has finished for all classes print the complete timetable

for example if a student picks 'ACC501'

[('Accounting & Financial Mgt 1A', 'LEC', 'A', 'Tue 16-18 (w11, Science Th); Thu 16-18 (w1-9, Science Th)'), ('Accounting & Financial Mgt 1A', 'LEC', 'B', 'Wed 09-11 (w1-10, Science Th)'), ('Accounting & Financial Mgt 1A', 'LEC', 'C', 'Wed 09-11 (w11, CLB 7); Fri 09-11 (w1-8,10, CLB 7)'), ('Accounting & Financial Mgt 1A', 'LEC', 'D', 'Tue 13-15 (w11, PhysicsTh); Thu 13-15 (w1-9, PhysicsTh)'), ('Accounting & Financial Mgt 1A', 'LEC', 'E', 'Wed 12-14 (w11, PhysicsTh); Fri 12-14 (w1-8,10, PhysicsTh)')

To pick a lecture you would enter 0 as in integer as the lecture is the first index of the list
"""

with open("timetable.pickle","rb") as pickle_in:
    # treat offerings as a dictionary
    offerings = pickle.load(pickle_in)
print(offerings)

# Enter Courses -> prompt the user to input their courses
# if you are not a UNSW student please input the courses, COMP3121, COMP3231, COMP4337
course1 = ?
course2 = ?
course3 = ?

# Store all our courses in 1 list for easy access and reference
semester = ?
# we need a dictionary to store our choices for class times how do we do that?
enrollment = ? 

# iterate over all the courses you entered
for course in semester:
    # get your specific course details from "offerings" using "course" as a key
    course_choices = ?
    # print out all the classes in your course
    for index,classes in enumerate(course_choices):
        print(index,classes)
    # enter a choice for your tutorial and lecture, this needs to be entered as a number to index course_choices list
    tutorial = ?
    lecture = ?
    #lab = int(input("Please enter your lab\n"))
    # Using tutorial & lectures (which are integers) select an index in course_choices as a tutorial or lecture
    enrollment[course] = "lecture:\n" + ? 
    + "\n" + "tutorial:\n" + ?

# print our course timetable



# functions
def check_clash():
    pass

# we can check if a course is offered in trimester 1
def check_offered():
    # replace ACC501 with your own course
    course = "ACC501"
    if course in offerings:
        print("course is offered")
    else:
        print("course is not offered")