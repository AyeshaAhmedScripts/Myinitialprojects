#recycling values
import functools
letters =["A","Y","E","S","H","A"]
words =functools.reduce(lambda x, y : x+y,letters)
print(words)

factorial = [1,2,3,4,5]
result =functools.reduce(lambda x, y : x*y,factorial)
print(result)