with open("./files/economic-indicators.csv","r") as boston:
    total_flights = 0
    higher_traffic = 0
    total_passengers = 0
    highest_daily_average = 0
    year_choice = input("Which year do you want to search for? ")
    for line in boston.readlines()[1:-1]:
        list = line.split(",")
        total_flights = total_flights + float(list[3])
        if float(list[2]) > float(higher_traffic):
            higher_traffic = list[2]
            year = list[0]
            month = list[1]
        if year_choice == list[0]:
            total_passengers = total_passengers + float(list[2])
            if float(list[5]) > float(highest_daily_average):
                highest_daily_average = list[5]
                month_higher_daily = list[1]
    print("The total number of flights is:", total_flights)
    print("The most popular month/year at the airport was:", str(month),"/",str(year))
    print("The total number of passengers in", year_choice, "was:", total_passengers)
    print("The month of the year", year_choice, "with the highest average for hotel daily was:", month_higher_daily)