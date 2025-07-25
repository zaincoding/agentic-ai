from datetime import datetime
#Destination Agent
def  destination_agent(interest):
    if 'relax' in interest.lower():
        return 'Bali'
    elif 'adventure' in interest.lower():
        return 'Swizerland'

def get_flight(destination, date):
    available_dates = ["2025-07-26","2025-07-28","2025-07-31"]  # Example available dates
    flight_options = []

 
   
    if str(date) in available_dates:
        # If user's date matches, show flights for that date
        flight_options.append(f"{date} - 08:00 am    {destination} PIA")
        flight_options.append(f"{date} - 08:00 pm    {destination} Emirates")
    else:
        print(f"\nNo flights on {date}. Try booking one of the available dates instead:\n")
        for available_date in available_dates:
            flight_options.append(f"{available_date} - 08:00 am    {destination} PIA")
            flight_options.append(f"{available_date} - 08:00 pm    {destination} Emirates")
    return flight_options




#Suggested Hotels
def suggested_hotels(destination):

    if destination == 'Bali':
        return[
        f"{destination} Grand Hotel 5000 per/night",
        f"{destination} AmanKila Hotel 7000 per/night"
        ]
    elif destination =='Swizerland':
        return[
       f"{destination} The Woodward 15000 per/night",
       f"{destination} The Dolder Grand 17000 per/night"
    ]
    else:
         return("Hotel is not booked yet.")

#Booking Agent

def booking_agent(selected_flight, selected_hotel):
    print(f"Flight confirmed: {selected_flight}")

    if selected_hotel:
        print(f"Hotel booked: {selected_hotel}")

    else:
        print(f"Hotel not booked yet.")


#explore Agent
def explore_agent(destination):
    attraction = {
        "Bali":['Beach youga', 'Temple Tour'],
        "Swizerland":['Hiking Alps', 'Skiing']
    }

    print(f"\n Attractions:")
    for place in attraction.get(destination, ['Explore local life']):
        print(f" -{place}")


def travel_planer():
      
    print(f"\nWelcome to AI travel Designer.")

    valid_interest = ['relax', 'adventure']
    while True:
    #user input
        interest = input("What kind of travel experience are you looking for ? (eg. relax, adventure)")
        if interest in valid_interest:
            break
        else:
            print("Invalid date formate. Please choose from: relax, adventure")

    while True:
        user_date = input("Enter your travel date (YYYY-MM-DD).")
        try:
            travel_date = datetime.strptime(user_date, "%Y-%m-%d").date()
            break
        
        except ValueError:
                print("Invalid Date formate. Please use YYYY-MM-DD (e.g 2025-5-20)")
     

    #DestinationAgent
    destination = destination_agent(interest)
    print(f"\nBase on your interest, we suggest: {destination}")

    #show fligh
    flights = get_flight(destination,travel_date)
    for i, flight in enumerate(flights):
        print(f"{i+1}.{flight}")


    while True:
        try:
            selected_index = int(input("\nSelect your flight by number:"))

            if 1 <= selected_index <= len(flights):
                selected_flight = flights[selected_index -1]
                break
            else:
                print("Invalid selection. Choose a number from the list.")
        except ValueError:
                print("Please enter a valid number")


    hotels = suggested_hotels(destination)
    for i,hotel in enumerate(hotels):
        print(f"{i+1}.{hotel}")


    selected_hotel=None
    while True:
        try:
            hotel_index = input("\nSelect your hotel by number or (press enter to skip): ")
            if hotel_index == "":
                hotel_index = None
                break
            else:
                hotel_index = int(hotel_index)
                if 1 <= hotel_index <= len(hotels):
                    selected_hotel = hotels[hotel_index -1]
                    break
                else:
                    print("Invalid selection.Choose a number from the list")

        except ValueError:
            print("Please enter a valid number.")


    booking_agent(selected_flight, selected_hotel)

    explore_agent(destination)


travel_planer()