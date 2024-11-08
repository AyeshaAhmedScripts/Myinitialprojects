# list =[expression for item in iterable if conditional]

#normal code
square= []
for i in range(1, 11):
    square.append( i*i)

print(square)

#code with list comprehension
square = [i*i for i in range(1,11)]
print(square)

#with lambda
students_grade = [100,90,67,54,43,23,5,66,76,12,97,0]
passed_students = list(filter(lambda x:x >=60, students_grade))
print(passed_students)

#with list comprehension
students_grade = [100,90,67,54,43,23,5,66,76,12,97,0]
passed_students = [i for i in students_grade if i >= 60]
print(passed_students)

#when changing failed numbers to fail
# list =[expression(if/else) for item in iterable]
students_grade = [100,90,67,54,43,23,5,66,76,12,97,0]
passed_students = [i if i >=60 else "FAILED" for i  in students_grade]
print(passed_students)