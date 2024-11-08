numbers=[4,5,3,6,7,3,2,3,2,5,7,5,1,7,8,7,6,9,0,8,4,3,1,0,4,2]
single = []
for number in numbers:
    if number not in single:
        single.append(number)
print(single)