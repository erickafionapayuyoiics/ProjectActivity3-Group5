import urllib.parse
import requests
import time
from datetime import datetime, timedelta
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "EA1IU2OTCZxouWIPnzADikvALm1NUGrt"
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    now = input("Time of Departure(follow format: hh:mm:ss): ")
    if now == "quit" or now == "q":
        break
    rtype = input(" V - Vehicle \n W - Walk \n B - Bicycle \nMode of Transportation: ")
    if rtype == "V" or rtype == "v":
        rtype = input(" F - Fastest \n S - Shortest \nWhich route do you prefer: ")
        if rtype == "F" or rtype == "f":
            rtype = "Fastest"
        elif rtype == "S" or rtype == "s":
            rtype = "Shortest"
    elif rtype == "W" or rtype == "w":
        rtype = "Pedestrian"
    elif rtype == "B" or rtype == "b":
        rtype = "Bicycle"
    elif rtype == "quit" or rtype == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "routeType": rtype})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    
    duration = (json_data["route"]["formattedTime"])
    t = datetime.strptime(duration, '%H:%M:%S')
    ct = datetime.strptime(now, "%H:%M:%S")
    d = timedelta(hours = t.hour, minutes = t.minute, seconds = t.second)
    eta = ct + d
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Route Type: " + (rtype))
        print("Trip Duration: " + duration)
        print("Expected Time of Arrival: " + eta.strftime("%H:%M:%S"))
        print("Miles: " + str(json_data["route"]["distance"]))
        print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
        print("=============================================")
        print("Kilometers: " + str((json_data["route"]["distance"])*1.61))
        print("Fuel Used (Ltr): " + str((json_data["route"]["fuelUsed"])*3.78))
        print("Kilometers: " +
        str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " +
        str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")