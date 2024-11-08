

friends = [("Robin", 19  ),
            ("Raven", 25  ),
            ("Starfire", 17  ),
            ("Beast boy", 15 ),
            ("Cyborg", 30  )]

age = lambda data:data[1] >= 18

adult_friends=list(filter(age, friends))

for i in adult_friends:
    print(i)