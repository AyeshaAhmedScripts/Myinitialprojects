command = ""
started = False
stopped = False
while True:
    command = input(">").lower()
    if command == "help":
       print("""
start - to start the car
stop - stop the car
quit - to exit""")
    elif command == 'start':
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started... Ready to go")
    elif command == 'stop':
        if not started:
            print("Car is already stopped")
        else:
            started =False
            print("Car stopped.")
    elif command == 'quit':
      print("")
      break
    else:
      print("I don't understand that...")
