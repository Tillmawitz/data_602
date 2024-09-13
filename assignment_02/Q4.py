# Q4. Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should also create a
# dictionary containing course numbers and the names of the instructors that teach each
# course. After that, the program should let the user enter a course number, then it should
# display the course’s room number, instructor, and meeting time.

course_room = {'Data 606': 'Room 606', 'Data 607': 'Room 607', 'Data 624': 'Room 624', 'Data 602': 'Room 602'}
course_instructor = {'Data 606': 'Dave', 'Data 607': 'Jane', 'Data 624': 'Bob', 'Data 602': 'Tina'}
course_time = {'Data 606': '6:00', 'Data 607': '7:00', 'Data 624': '8:00', 'Data 602': '9:00'}

course_name = input("Enter a course name from the options " + ', '.join(course_room.keys()) + ": ")

if (course_name in course_room.keys()) and (course_name in course_instructor.keys()) and (course_name in course_time.keys()):
    print("The " + course_name + " class is taught in room " + course_room[course_name] + " by instructor " + course_instructor[course_name] + " at " + course_time[course_name])
else:
    print("There is not complete data on " + course_name)