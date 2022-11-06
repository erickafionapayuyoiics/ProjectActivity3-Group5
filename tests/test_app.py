from MapQuest import myfunc
from tests.tud_test_base import set_keyboard_input, get_display_output

def test_1():
    set_keyboard_input(["Bulacan", "Manila", "12:12:12", "V", "F", "C"])

    myfunc()

    output = get_display_output()

    assert output == ["Starting Location: ",
                    "Destination: ", 
                    "Time of Departure (follow this format: hh:mm:ss): ",
                    "\n  V - Vehicle \n  W - Walk \n  B - Bicycle \nChoose your mode of transportation: ",
                    "\n  F - Fastest \n  S - Shortest \nChoose your preferred route: ",
                    "\n  C - Cautious \n  N - Normal \n  A - Aggressive \nChoose your preferred driving style: ",
                    "URL: https://www.mapquestapi.com/directions/v2/route?key=EA1IU2OTCZxouWIPnzADikvALm1NUGrt&from=Bulacan&to=Manila&routeType=Fastest&drivingStyle=Cautious",
                    "API Status: 0 = A successful route call.\n",
                    "==========================================================================================",
                    "Directions from Bulacan to Manila",
                    "Route Type: Fastest",
                    "Driving Style: Cautious",
                    "==========================================================================================",
                    "Warning! This route includes highway or limited access road.",
                    "Warning! This route includes toll roads/gates (e.g. NLEX, SCTEX, TPLEX, STAR, CAVITEX, SLEX).",
                    "This route has no unpaved or dirt roads along the way.",
                    "==========================================================================================",
                    "Trip Duration: 00:59:17",
                    "Expected Time of Arrival: 13:11:29",
                    "Miles: 27.1508",
                    "==========================================================================================",
                    "Kilometers: 43.712788",
                    "Kilometers: 43.71",
                    "Head north on Obando-Bulacan-Malolos Rd. Go for 1.0 mi. (1.53 km)",
                    "Continue on Camino Real. Go for 0.2 mi. (0.34 km)",
                    "Turn right onto Molina St. Go for 1.3 mi. (2.05 km)",
                    "Continue on Matungao Rd. Go for 62 ft. (0.02 km)",
                    "Keep left onto C. Mercado toward Guiguinto. Go for 1.1 mi. (1.73 km)",
                    "Turn left onto Manila North Rd (1 AH26). Go for 1.7 mi. (2.77 km)",
                    "Turn right and take ramp onto Tabang Spur Rd (E1 AH26) toward NLEX. Go for 2.6 mi. (4.13 km)",
                    "Take ramp onto E1 AH26 (NLEX). Go for 14.6 mi. (23.44 km)",
                    "Continue on 160 (Balintawak Cloverleaf). Go for 0.1 mi. (0.19 km)",
                    "Continue on A. Bonifacio Ave (160) toward Blumentritt/Sgt. Rivera/Manila. Go for 1.5 mi. (2.36 km)",
                    "Keep right onto A. Bonifacio Ave (160) toward Roxas Blvd./Coastal Road/SLEX. Go for 0.8 mi. (1.34 km)",
                    "Turn right onto Blumentritt Rd (160) toward Jose Abad Santos/Rizal Avenue/Dimasalang. Go for 0.2 mi. (0.27 km)",
                    "Turn left onto Aurora Blvd. Go for 0.1 mi. (0.19 km)",
                    "Turn right onto Dimasalang Rd (162). Go for 0.7 mi. (1.11 km)",
                    "Continue on Laong Laan Rd (162). Go for 30 ft. (0.01 km)",
                    "Turn left onto Lacson Ave (140). Go for 0.4 mi. (0.66 km)",
                    "Turn right onto España Blvd (170). Go for 0.4 mi. (0.64 km)",
                    "Keep left toward Nicanor Reyes St. Go for 233 ft. (0.07 km)",
                    "Turn slightly left onto Nicanor Reyes St. Go for 0.2 mi. (0.35 km)",
                    "Turn right onto Claro M. Recto Ave (145) toward Divisoria/Lucky China Town. Go for 0.1 mi. (0.23 km)",
                    "Turn right onto Andalucia. Go for 0.2 mi. (0.26 km)",
                    "Arrive at España Blvd. (0.00 km)",
                    "==========================================================================================\n"
                    ]

def test_2():
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