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
        quit()
    
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        quit()
    
    try: 
        now = datetime.strptime((input("Time of Departure (follow this format: hh:mm:ss): ")), "%H:%M:%S")
    except ValueError:
        print("Please enter the right format.")
        quit()
    if now == "quit" or now == "q":
        quit()


    rtype = input("\n  V - Vehicle \n  W - Walk \n  B - Bicycle \nChoose your mode of transportation: ")
    if rtype == "V" or rtype == "v":
        rtype = input("\n  F - Fastest \n  S - Shortest \nChoose your preferred route: ")
        if rtype == "F" or rtype == "f":
            rtype = "Fastest"
        elif rtype == "S" or rtype == "s":
            rtype = "Shortest"
        elif rtype == "quit" or rtype == "q":
            quit()
            
        dstyle = input("\n  C - Cautious \n  N - Normal \n  A - Aggressive \nChoose your preferred driving style: ")
        if dstyle == "C" or dstyle == "c":
            dstyle = "Cautious"
        elif dstyle == "N" or dstyle == "n":
            dstyle = "Normal"
        elif dstyle == "A" or dstyle == "a":
            dstyle = "Aggressive"
        elif dstyle == "quit" or dstyle == "q":
            quit()

    elif rtype == "W" or rtype == "w":
        rtype = "Pedestrian"

    elif rtype == "B" or rtype == "b":
        rtype = "Bicycle"

        rgs = input("\n  D - Default Strategy \n  A - Avoid All Hills \n  F - Favor All Hills \nChoose your preferred road grade strategy: ")
        if rgs == "D" or rgs == "d":
            rgs = "DEFAULT_STRATEGY"
        elif rgs == "A" or rgs == "a":
            rgs = "AVOID_ALL_HILLS"
        elif rgs == "F" or rgs == "f":
            rgs = "FAVOR_ALL_HILLS"
        elif rgs == "quit" or rgs == "q":
            quit()

    elif rtype == "quit" or rtype == "q":
        quit()
    
    
    # Retrieve data from API 
    if rtype == "Fastest" or rtype == "Shortest":
        url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "routeType": rtype, 
        "drivingStyle": dstyle})
    elif rtype == "Pedestrian":
        url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "routeType": rtype})
    elif rtype == "Bicycle":
        url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "routeType": rtype, 
        "roadGradeStrategy": rgs})
    #url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "routeType": rtype, 
    #"drivingStyle": dstyle, "roadGradeStrategy": rgs})
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
        print("==========================================================================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Route Type: " + (rtype))
        if rtype == "Fastest" or rtype == "Shortest":
            print("Driving Style: " + (dstyle))
        if rtype == "Bicycle":
            print("Road Grade Strategy: " + (rgs))
    
        print("==========================================================================================")
        # Give warning to user when route includes highway or limited access road (Added feature)
        if (json_data["route"]["hasHighway"]) == True:
            print("Warning! This route includes highway or limited access road.")
        else:
            print("This route has no highway or limited access road along the way.")

        # Give warning to user when route includes toll roads/gates (Added feature)
        if (json_data["route"]["hasTollRoad"]) == True:
            print("Warning! This route includes toll roads/gates (e.g. NLEX, SCTEX, TPLEX, STAR, CAVITEX, SLEX).")
        else:
            print("This route has no toll roads/gates (e.g. NLEX, SCTEX, TPLEX, STAR, CAVITEX, SLEX) along the way.")

        # Give warning to user when route includes unpaved or dirt roads (Added feature)
        if (json_data["route"]["hasUnpaved"]) == True:
            print("Warning! This route includes unpaved or dirt roads.")
        else:
            print("This route has no unpaved or dirt roads along the way.")

        print("==========================================================================================")
        print("Trip Duration: " + duration)
        print("Expected Time of Arrival: " + eta.strftime("%H:%M:%S"))
        print("Miles: " + str(json_data["route"]["distance"]))
        #print("Fuel Used: " + str(json_data["route"]["fuelUsed"]))
                
        print("==========================================================================================")
        print("Kilometers: " + str((json_data["route"]["distance"])*1.61))
        
        print("Kilometers: " +
        str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("==========================================================================================\n")
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