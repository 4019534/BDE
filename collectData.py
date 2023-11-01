# import requests
#from datetime import datetime
import datetime
# #Waze api

# ory = "48.72528 ,2.35944"
# cdg = "49.0092286 ,2.5606637176262623"
# lbg = "48.963318,2.418656"

# sourceCO = ""
# deslat = input("Enter latitude of hotel: ")
# deslong = input("Enter longitude of hotel: ")
# date = input("Please enter date in the format yyyy-mm-dd: ")
# date2 = date.replace("-", "")
# airport = input("Enter airport IATA three-letter geocode XXX: ")

# if airport == "ORY":
#     sourceCO = ory
# elif airport == "CDG":
#     sourceCO = cdg
# elif airport == "LBG":
#     sourceCO = lbg
# else:
#     sourceCO = ""
# url = "https://waze.p.rapidapi.com/driving-directions"
# #"48.8456678, 2.3757617"

# querystring = {"source_coordinates":str(sourceCO),"destination_coordinates":str(deslat) + "," + str(deslong),"return_route_coordinates":"true"}

# headers = {
# 	"X-RapidAPI-Key": "7e08d8ea8dmshb3fe17a6c8f27e7p18bb03jsn484b83cec05a",
# 	"X-RapidAPI-Host": "waze.p.rapidapi.com",
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"

# }

# response = requests.get(url, headers=headers, params=querystring)
# if response.status_code == 200:
#     print("Your responses are being processessed......")
# else:
#     print("A problem happened with your response :/")

# data = response.json()

# routes = [item['route_name'] for item in data['data']]
# length = [item['length_meters'] for item in data['data']]

# duration_seconds_list = [item['duration_seconds'] for item in data['data']]
# travelTime = 0
# travelDist = 0
# for dur in duration_seconds_list:
#     travelTime = travelTime + dur

# path = ""
# for leng in length:
#     travelDist = travelDist + leng
# for route in routes:
#     path = path + " -> " + str(route)

# routing = "Route: " + path + "\nTravel time (sec): " + str(travelTime)  + "\nTravel distance (m): " + str(j)


# #FightSearch api from rapid api
# # value1 = str(sys.argv[1])
# # value2 = str(sys.argv[2])
# url2 = "https://flight-fare-search.p.rapidapi.com/v2/flights/"
# # date = input("Please enter date in the format yyyy-mm-dd: ")
# querystring2 = {"from":"CPT","to":str(airport),"date":str(date),"adult":"1","type":"economy","currency":"USD"}
# #"2023-11-30" - example to use

# #
# headers2 = {
# 	"X-RapidAPI-Key": "7e08d8ea8dmshb3fe17a6c8f27e7p18bb03jsn484b83cec05a",
# 	"X-RapidAPI-Host": "flight-fare-search.p.rapidapi.com",
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"

# }

# #save the request results
# response2 = requests.get(url2, headers=headers2, params=querystring2)

# if response2.status_code == 200:
#     print("Almost done processessing response......")
# else:
#     print("A problem happened with your response :/")

# data2 = response2.json()
# #Extract the wanted data from the api results
# timedepart = data2["results"][0]["departureAirport"]['time']
# timearrive = data2["results"][0]["arrivalAirport"]['time']

# time_str1 = str(timedepart)
# time_str2 = str(timearrive)

# # Convert the time strings to datetime objects
# time1 = datetime.fromisoformat(time_str1)
# time2 = datetime.fromisoformat(time_str2)

# # Calculate the time difference
# time_difference = time2 - time1

# # Extract the time difference as hours, minutes, and seconds
# hours, remainder = divmod(time_difference.seconds, 3600)
# minutes, seconds = divmod(remainder, 60)

# #################

# #Weather api
# url3 = "https://weather338.p.rapidapi.com/weather/forecast"
# #input coordinates to get weather conditions 
# # deslat = input("latitude: ")
# # deslong = input("longitude: ")
# # date2 = input("Please enter the date again in this format yyyymmdd: ")
# querystring3 = {"date":str(date2),"latitude":str(deslat),"longitude":str(deslong),"language":"en-US","units":"m"}
# #latitude":"48.853","longitude":"2.348"
# headers3 = {
# 	"X-RapidAPI-Key": "7e08d8ea8dmshb3fe17a6c8f27e7p18bb03jsn484b83cec05a",
# 	"X-RapidAPI-Host": "weather338.p.rapidapi.com",
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"

# }

# response3 = requests.get(url3, headers=headers3, params=querystring3)

# if response3.status_code == 200:
#     print("Nearly there......")
# else:
#     print("A problem happened with your response :/")

# data3 = response3.json()
# # #puts each condition type in a separate variable
# # tempMin = data3["v3-wx-conditions-historical-dailysummary-30day"]["temperatureMin"][1]
# # tempMax = data3["v3-wx-conditions-historical-dailysummary-30day"]["temperatureMax"][0]
# # rain = data3["v3-wx-conditions-historical-dailysummary-30day"]["rain24Hour"][0]
# # snow = data3["v3-wx-conditions-historical-dailysummary-30day"]["snow24Hour"][0]
# # day = data3["v3-wx-conditions-historical-dailysummary-30day"]["dayOfWeek"][0]

# weather = data3["v3-wx-forecast-hourly-10day"]
# day =  weather2["dayOfWeek"][0]
# pchance = weather2['precipChance'][0]
# ptype = weather2['precipType'][0]
# temp2 = weather2['temperature'][0]
# offset = ""
# print(routing)
# rain = 20
# snow = 30
# print()
# print(f"Time Difference: {time_difference.days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
# print()
# flightTime = (hour*3600) + (minute*60) + seconds
# estimatedDT = travelTime + flightTime
# print("Estimated delivery duration: " + str(estimatedDT))
# if ptype == "rain":
#     print("There will be a " + str(pchance) + "percent chance of " + str(ptype) + " and as such we consider a " + str(rain) + "% time buffer for our delivery estimate.")
#     offset = rain
#     offset = estimatedDT/offset
#     estimatedDT = estimatedDT + offset
#     print("Estimated delivery duration:" + str(estimatedDF))
# elif ptype == "snow":
#     print("There will be a " + str(pchance) + "percent chance of " + str(ptype) + " and as such we consider a " + str(snow) + "% time buffer for our delivery estimate.")
#     offset = snow
#     offset = estimatedDT/offset
#     estimatedDT = estimatedDT + offset
#     print("Estimated delivery duration:" + str(estimatedDF))

datea = "2023-11-30"
rest_hours = input("Enter opening time of restaurant (HH:MM): ")

estimatedDF = (22*3600) + (50*60)
rest_hours = datetime.datetime.strptime(rest_hours, "%H:%M")
arrival_date = datetime.datetime.strptime(datea, "%Y-%m-%d")

# Estimated travel time in seconds
estimated_travel_time_seconds = 3600  # Replace with your estimate in seconds

# Calculate departure date and time by subtracting the estimated travel time
departure_datetime = arrival_date - datetime.timedelta(seconds=estimatedDF)
departure_time = rest_hours - datetime.timedelta(seconds=estimatedDF)
# Format the departure date and time
departure_date_time_str = departure_datetime.strftime("%Y-%m-%d")

departure_time_str = departure_time.strftime("%H:%M")

print(f"Departure date and time: {departure_date_time_str}")
print(f"Departure time: {departure_time_str}")