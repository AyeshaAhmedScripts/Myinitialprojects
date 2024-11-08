# map(function, iterable)

outfit = [("Blouse", "white",62),
          ("Pants", "Cargo",23),
          ("Belt", "Black",65),
          ("Hat", "beret",56)]

to_pkr = lambda data: (data[0], data[1], data[2]/0.0036)

outfit_pkr = list(map(to_pkr, outfit))

for i in outfit_pkr:
    print(i)