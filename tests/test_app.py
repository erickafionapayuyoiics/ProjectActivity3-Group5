from ProjectActivity3-Group5.MapQuest import myfunc
from tests.tud_test_base import set_keyboard_input, get_display_output

def test_1():
    set_keyboard_input(["Bulacan", "Manila", "12:12:12", "V", "F"])

    myfunc()

    output = get_display_output()

    assert output == ["Starting Location: ",
                    "Destination: ", 
                    "Time of Departure(follow format: hh:mm:ss): ",
                    " V - Vehicle \n W - Walk \n B - Bicycle \nMode of Transportation: ",
                    " F - Fastest \n S - Shortest \nWhich route do you prefer: ",
                    "URL: https://www.mapquestapi.com/directions/v2/route?key=EA1IU2OTCZxouWIPnzADikvALm1NUGrt&from=Bulacan&to=Manila&routeType=Fastest",
                    "API Status: 0 = A successful route call.\n",
                    "=============================================",
                    "Directions from Bulacan to Manila",
                    "Route Type: Fastest",
                    "=============================================",
                    "Warning! This route includes highway or limited access road. ",
                    "=============================================",
                    "Trip Duration: 00:59:30",
                    "Expected Time of Arrival: 13:11:42",
                    "Miles: 27.2067",
                    "=============================================",
                    "Kilometers: 43.802787",
                    "Kilometers: 43.80",
                    "Head north on Obando-Bulacan-Malolos Rd. Go for 1.0 mi. (1.53 km)",
                    "Continue on Camino Real. Go for 0.2 mi. (0.34 km)",
                    "Turn right onto Molina St. Go for 1.3 mi. (2.05 km)",
                    "Continue on Matungao Rd. Go for 62 ft. (0.02 km)",
                    "Keep left onto C. Mercado toward Guiguinto. Go for 1.1 mi. (1.73 km)",
                    "Turn left onto Manila North Rd (1 AH26). Go for 1.7 mi. (2.77 km)",
                    "Turn right and take ramp onto Tabang Spur Rd (E1 AH26) toward NLEX. Go for 2.6 mi. (4.13 km)",
                    "Take ramp onto E1 AH26 (NLEX). Go for 14.6 mi. (23.44 km)",
                    "Continue on 160 (Balintawak Cloverleaf). Go for 0.1 mi. (0.19 km)",
                    "Continue on A. Bonifacio Ave (160) toward Blumentritt/Sgt. Rivera/Manila. Go for 1.5 mi. (2.39 km)",
                    "Continue on Mayon Ave. Go for 1.4 mi. (2.30 km)",
                    "Turn right toward Espana/170. Go for 240 ft. (0.07 km)",
                    "Continue on Espana (170). Go for 1.2 mi. (1.91 km)",
                    "Keep left toward Nicanor Reyes St. Go for 233 ft. (0.07 km)",
                    "Turn slightly left onto Nicanor Reyes St. Go for 0.2 mi. (0.35 km)",
                    "Turn right onto Claro M. Recto Ave (145) toward Divisoria/Lucky China Town. Go for 0.1 mi. (0.23 km)",
                    "Turn right onto Andalucia. Go for 0.2 mi. (0.26 km)",
                    "Arrive at España Blvd. (0.00 km)",
                    "=============================================\n"
                    ]