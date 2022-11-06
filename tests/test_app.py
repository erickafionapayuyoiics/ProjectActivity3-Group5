from MapQuest import myfunc
from tests.tud_test_base import set_keyboard_input, get_display_output

def test_1():
    set_keyboard_input(["Bulacan", "Pampanga", "12:12:12", "V", "S", "N"])

    myfunc()

    output = get_display_output()

    assert output == ["Starting Location: ",
                    "Destination: ", 
                    "Time of Departure (follow this format: hh:mm:ss): ",
                    "\n  V - Vehicle \n  W - Walk \n  B - Bicycle \nChoose your mode of transportation: ",
                    "\n  F - Fastest \n  S - Shortest \nChoose your preferred route: ",
                    "\n  C - Cautious \n  N - Normal \n  A - Aggressive \nChoose your preferred driving style: ",
                    "URL: https://www.mapquestapi.com/directions/v2/route?key=EA1IU2OTCZxouWIPnzADikvALm1NUGrt&from=Bulacan&to=Pampanga&routeType=Shortest&drivingStyle=Normal",
                    "API Status: 0 = A successful route call.\n",
                    "==========================================================================================",
                    "Directions from Bulacan to Pampanga",
                    "Route Type: Shortest",
                    "Driving Style: Normal",
                    "==========================================================================================",
                    "This route has no highway or limited access road along the way.",
                    "This route has no toll roads/gates (e.g. NLEX, SCTEX, TPLEX, STAR, CAVITEX, SLEX) along the way.",
                    "This route has no unpaved or dirt roads along the way.",
                    "==========================================================================================",
                    "Trip Duration: 01:16:57",
                    "Expected Time of Arrival: 13:29:09",
                    "Miles: 27.9368",
                    "==========================================================================================",
                    "Kilometers: 44.97824800000001",
                    "Kilometers: 44.98",
                    "Head north on Obando-Bulacan-Malolos Rd. Go for 1.0 mi. (1.53 km)",
                    "Continue on Camino Real. Go for 1.9 mi. (3.03 km)",
                    "Turn left onto National Rd. Go for 4.2 mi. (6.79 km)",
                    "Turn right toward Paseo de Congreso. Go for 0.2 mi. (0.28 km)",
                    "Continue on Paseo de Congreso. Go for 0.7 mi. (1.16 km)",
                    "Turn left onto Manila North Rd. Go for 15.2 mi. (24.45 km)",
                    "Take the 3rd exit from roundabout onto Gen. Hizon Ave toward San Fernando/City Proper. Go for 0.6 mi. (0.93 km)",
                    "Turn left onto V. Tiomico St. Go for 1.1 mi. (1.83 km)",
                    "Turn right onto Lazatin Blvd. Go for 1.5 mi. (2.47 km)",
                    "Turn left onto MacArthur Hwy (2). Go for 1.6 mi. (2.52 km)",
                    "Arrive at MacArthur Hwy (2). (0.00 km)",
                    "==========================================================================================\n"
                    ]

def test_2():
    set_keyboard_input(["Pampanga", "Bulacan", "11:12:21", "B", "A"])

    myfunc()

    output = get_display_output()

    assert output == ["Starting Location: ",
                    "Destination: ", 
                    "Time of Departure (follow this format: hh:mm:ss): ",
                    "\n  V - Vehicle \n  W - Walk \n  B - Bicycle \nChoose your mode of transportation: ",
                    "\n  D - Default Strategy \n  A - Avoid All Hills \n  F - Favor All Hills \nChoose your preferred road grade strategy: ",
                    "URL: https://www.mapquestapi.com/directions/v2/route?key=EA1IU2OTCZxouWIPnzADikvALm1NUGrt&from=Pampanga&to=Bulacan&routeType=Bicycle&roadGradeStrategy=AVOID_ALL_HILLS",
                    "API Status: 0 = A successful route call.\n",
                    "==========================================================================================",
                    "Directions from Pampanga to Bulacan",
                    "Route Type: Bicycle",
                    "Road Grade Strategy: AVOID_ALL_HILLS",
                    "==========================================================================================",
                    "This route has no highway or limited access road along the way.",
                    "This route has no toll roads/gates (e.g. NLEX, SCTEX, TPLEX, STAR, CAVITEX, SLEX) along the way.",
                    "This route has no unpaved or dirt roads along the way.",
                    "==========================================================================================",
                    "Trip Duration: 02:53:28",
                    "Expected Time of Arrival: 14:05:49",
                    "Miles: 26.7538",
                    "==========================================================================================",
                    "Kilometers: 43.073618",
                    "Kilometers: 43.07",
                    "Head southeast on MacArthur Hwy (2). Go for 2.9 mi. (4.70 km)",
                    "Pass 2 roundabouts and continue on MacArthur Hwy (2). Go for 9.2 mi. (14.84 km)",
                    "Turn left toward MacArthur Hwy/2. Go for 0.4 mi. (0.61 km)",
                    "Continue on MacArthur Hwy (2). Go for 9.0 mi. (14.57 km)",
                    "Turn right toward Calle Hagonoy. Go for 141 ft. (0.04 km)",
                    "Turn slightly left onto Calle Hagonoy. Go for 1.7 mi. (2.75 km)",
                    "Continue on Pulo ng Dulo. Go for 0.6 mi. (1.01 km)",
                    "Turn right toward National Rd. Go for 1.5 mi. (2.37 km)",
                    "Turn left onto National Rd. Go for 0.4 mi. (0.65 km)",
                    "Keep right onto Derecho. Go for 1.0 mi. (1.53 km)",
                    "Arrive at Obando-Bulacan-Malolos Rd. (0.00 km)",
                    "==========================================================================================\n"
                    ]

def test_3():
    set_keyboard_input(["Manila", "Quezon City", "9:27:22", "W"])

    myfunc()

    output = get_display_output()

    assert output == ["Starting Location: ",
                    "Destination: ", 
                    "Time of Departure (follow this format: hh:mm:ss): ",
                    "\n  V - Vehicle \n  W - Walk \n  B - Bicycle \nChoose your mode of transportation: ",
                    "URL: https://www.mapquestapi.com/directions/v2/route?key=EA1IU2OTCZxouWIPnzADikvALm1NUGrt&from=Manila&to=Quezon+City&routeType=Pedestrian",
                    "API Status: 0 = A successful route call.\n",
                    "==========================================================================================",
                    "Directions from Manila to Quezon City",
                    "Route Type: Pedestrian",
                    "==========================================================================================",
                    "This route has no highway or limited access road along the way.",
                    "This route has no toll roads/gates (e.g. NLEX, SCTEX, TPLEX, STAR, CAVITEX, SLEX) along the way.",
                    "This route has no unpaved or dirt roads along the way.",
                    "==========================================================================================",
                    "Trip Duration: 03:14:25",
                    "Expected Time of Arrival: 12:41:47",
                    "Miles: 7.2123",
                    "==========================================================================================",
                    "Kilometers: 11.611803",
                    "Kilometers: 11.61",
                    "Head east on España Blvd. Go for 266 ft. (0.08 km)",
                    "Turn right onto R. Papa. Go for 207 ft. (0.06 km)",
                    "Turn left onto Estro de Alix. Go for 125 ft. (0.04 km)",
                    "Turn left onto Nicanor Reyes St. Go for 253 ft. (0.08 km)",
                    "Turn slightly right onto España Blvd. Go for 1.2 mi. (1.99 km)",
                    "Take the street on the right, Espana. Go for 115 ft. (0.03 km)",
                    "Walk left around the roundabout and turn at the 2nd street Quezon Ave. Go for 3.8 mi. (6.07 km)",
                    "Turn left. Go for 262 ft. (0.08 km)",
                    "Turn left onto Elliptical Rd. Go for 0.2 mi. (0.40 km)",
                    "Turn left onto Visayas Ave. Go for 1.3 mi. (2.09 km)",
                    "Turn right onto Congressional Ave. Ext. Go for 0.4 mi. (0.64 km)",
                    "Turn right onto Tandang Sora Ave. Go for 194 ft. (0.06 km)",
                    "Arrive at Tandang Sora Ave. (0.00 km)",
                    "==========================================================================================\n"
                    ]
