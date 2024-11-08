#sort method is used with lists
#sort() function is used with iterables
students = ["Robin", "Raven", "Starfire", "Cyborg", "Beast boy"]

students.sort()
students.sort(reverse=True)
for i in students:
    print(i)


students = ("Robin", "Raven", "Starfire", "Cyborg", "Beast boy")
sorted_students = sorted(students, reverse = True)
for i in sorted_students:
    print(i)



students = [("Robin", "F", 19  ),
            ("Raven", "A", 25  ),
            ("Starfire", "C", 17  ),
            ("Beast boy", "D", 15 ),
            ("Cyborg", "A", 30  )]
grade = lambda grades:grades[1]
students.sort(key=grade, reverse=True)
for i in students:
    print(i)
