numbers_in_words = {
    "1":"one",
    "2":"two",
      "3" : "three",
     "4" : "four",
     "5" : "five",
     "6" : "six",
     "7" : "seven",
     "8" : "eight",
     "9" : "nine",
     "0" : "zero"
}
number= input("Phone:")
num = ""
for digit in number:
    num += numbers_in_words.get(digit,"!") + " "
print(num)
