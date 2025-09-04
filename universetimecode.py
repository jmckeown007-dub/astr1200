from tabulate import tabulate

if __name__ == "__main__":

    event_name = "" # initialize variable
    

    total_time = 1.4e10 # 14 billion years
    total_new_time = 130 # 130 minutes, a random length of a movie 

    events_in_minutes = {} # initialize dictionary to add to

    while True:
        event_name = input("What is the name of the event? (type 'exit' to quit) \n")

        if event_name.lower() in ("exit", "stop"):
            print("Exiting cosmic calendar...")
            break

        event_time = float(input("Enter event time (how many years ago?): "))

        

        scaled_time = (event_time / total_time) * total_new_time # calculates how many minutes from the end
        scaled_time_from_beginning = (total_new_time - scaled_time) # calculates how many minutes from the beginning

        events_in_minutes[event_name] = scaled_time_from_beginning

        if event_name.endswith("s"):
            print(f"In a {total_new_time}-minute cosmic movie, "
              f"the {event_name} occur at {scaled_time_from_beginning:.5f} minutes in.") # .5f shows up to 5 decimal places for accuracy's sake
        else:
            print(f"In a {total_new_time}-minute cosmic movie, "
              f"the {event_name} occurs at {scaled_time_from_beginning:.5f} minutes in.")


    table = [(name, f"{time:.5f} minutes in") for name, time in events_in_minutes.items()]
    print(tabulate(table, headers=["Event", "Time"], tablefmt="fancy_grid"))

