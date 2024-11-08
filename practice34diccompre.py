#dictionary = {key: expression for (key,value) in iterable}
#dictionary = {key: expression for (key,value) in iterable if conditional}
#dictionary = {key: (if/ else )expression for (key,value) in iterable}
#dictionary = {key: function (expression) for (key,value) in iterable}
cities_F = {'New York': 32,'Boston': 72, 'Los Angeles': 100 , 'Chicago': 50}
cities_C  = {key: round((value-32)*(5/9)) for (key,value ) in cities_F.items()}
cities_C  = {key: round((value-32)*(5/9)) for (key,value ) in cities_F.items() if value>=55}
dis_cities  = {key: ( "warm" if value>=50 else "cold") for (key,value ) in cities_F.items()}
print(cities_C )
print(dis_cities)