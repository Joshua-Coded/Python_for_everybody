#python simple gdp calculator

print("Welcome to the GPA calculator:")
print("PLease enter all your letter grades, one per line:")
print("Enter a blank line to designate the end:")

# map through letter grade to point value

points = {"A+": 5.0, "A": 4.0, "A-": 3.67, "B+": 3.3, "B": 3.0, "B-": 2.67, "C+": 2.33, "C": 2.0, "C-": 1.67, "D+":1.34,"D":1.0,"F":0.0}

num_courses = 0
total_points = 0
done = False
while not done:
    grade = input()
    if grade == '':
        done = True
    elif grade not in points:
        print("Unknown grade '{0}' being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]
    if num_courses > 0:
        print("YOur GPA IS {0:.3}".format(total_points / num_courses))
