# Bernabe, Alexandra B. 
# Martin, Traicy H. 
# Payuyo, Ericka Fiona T. 
# Valles, Ranielle Christian M. 

import urllib.parse
import requests
import time
from datetime import datetime, timedelta
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "EA1IU2OTCZxouWIPnzADikvALm1NUGrt"


def myfunc():
        orig = input("Starting Location: ")
        if orig == "quit" or orig == "q":
            exit
        
        dest = input("Destination: ")
        if dest == "quit" or dest == "q":
            exit
        
        try: 
            now = datetime.strptime((input("Time of Departure(follow format: hh:mm:ss): ")), "%H:%M:%S")
            exit
        except ValueError:
            print("Please enter the right format.")
        if now == "quit" or now == "q":
            exit

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
            exit

        dstyle = input (" 1 - Cautious \n 2 - Normal \n 3 - Aggressive \nWhich Driving Style do you prefer: ")
        if dstyle == "1":
            dstyle = "Cautious"
        elif dstyle == "2":
            dstyle = "Normal"
        elif dstyle == "3":
            dstyle = "Aggressive"
        elif dstyle == "quit" or dstyle == "q":
            exit
        
        # Retrieve data from API 
        url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "routeType": rtype, "drivingStyle": dstyle})
        print("URL: " + (url))
        json_data = requests.get(url).json()
        json_status = json_data["info"]["statuscode"]
    
        # Format time input with formatted time of API 
        duration = (json_data["route"]["formattedTime"])
        t = datetime.strptime(duration, '%H:%M:%S')
        d = timedelta(hours = t.hour, minutes = t.minute, seconds = t.second)
        eta = now + d
        
        
        # Display route details 
        if json_status == 0:
            print("API Status: " + str(json_status) + " = A successful route call.\n")
            print("=============================================")
            print("Directions from " + (orig) + " to " + (dest))
            print("Route Type: " + (rtype))
            print("Driving Style: " + (dstyle))
        
            # Give warning to user when route includes highway or limited access road (Added feature)
            if (json_data["route"]["hasHighway"]) == True:
                print("=============================================")
                print("Warning! This route includes highway or limited access road. ")
            else:
                print("=============================================")
                print("This route has no highway or limited access road along the way.")

            print("=============================================")
            print("Trip Duration: " + duration)
            print("Expected Time of Arrival: " + eta.strftime("%H:%M:%S"))
            print("Miles: " + str(json_data["route"]["distance"]))
            
            
            print("=============================================")
            print("Kilometers: " + str((json_data["route"]["distance"])*1.61))
            
            print("Kilometers: " +
            str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
            
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
            print("For Status Code: " + str(json_status) + "; Refer to:")
            print("https://developer.mapquest.com/documentation/directions-api/status-codes")
            print("************************************************************************\n")
            
myfunc()  