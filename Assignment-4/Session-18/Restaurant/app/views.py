# views.py
# Contains all the function-based views for the Django application.
# Includes views for the homepage, restaurant search, and distance search.
# Implements local fallback geocoding to support testing without active Google Cloud billing.

import math
import requests
from django.shortcuts import render
from django.conf import settings

def calculate_haversine_distance(lat1, lng1, lat2, lng2):
    """
    Manually calculates the distance between two points on the Earth
    using the Haversine formula.
    """
    # Earth's radius in kilometers
    EARTH_RADIUS = 6371.0
    
    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(float(lat1))
    lng1_rad = math.radians(float(lng1))
    lat2_rad = math.radians(float(lat2))
    lng2_rad = math.radians(float(lng2))
    
    # Calculate the difference between coordinates
    diff_lat = lat2_rad - lat1_rad
    diff_lng = lng2_rad - lng1_rad
    
    # Haversine formula calculation steps
    a = (math.sin(diff_lat / 2) ** 2) + math.cos(lat1_rad) * math.cos(lat2_rad) * (math.sin(diff_lng / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = EARTH_RADIUS * c
    
    return distance


def find_nearby_cafes(user_lat, user_lng, cafes):
    """
    Filters and returns cafes that are within 3 km of the user's location.
    """
    nearby_cafes = []
    for cafe in cafes:
        distance = calculate_haversine_distance(user_lat, user_lng, cafe["lat"], cafe["lng"])
        if distance <= 3.0:
            cafe_info = {
                "name": cafe["name"],
                "lat": cafe["lat"],
                "lng": cafe["lng"],
                "distance": round(distance, 2)
            }
            nearby_cafes.append(cafe_info)
    return nearby_cafes


# Mock database of Ahmedabad and Rajkot locations for geocoding fallback (if API billing is missing)
MOCK_LOCATIONS = {
    "iim ahmedabad": (23.0312, 72.5375, "IIM Ahmedabad, Gujarat, India"),
    "ahmedabad railway station": (23.0269, 72.6026, "Ahmedabad Railway Station, Ahmedabad, Gujarat, India"),
    "cg road": (23.0258, 72.5594, "CG Road, Ahmedabad, Gujarat, India"),
    "satellite": (23.0305, 72.5178, "Satellite, Ahmedabad, Gujarat, India"),
    "maninagar": (22.9976, 72.6102, "Maninagar, Ahmedabad, Gujarat, India"),
    "prahlad nagar": (23.0120, 72.5080, "Prahlad Nagar, Ahmedabad, Gujarat, India"),
    "vastrapur": (23.0350, 72.5293, "Vastrapur, Ahmedabad, Gujarat, India"),
    "rajkot": (22.3039, 70.8022, "Rajkot, Gujarat, India"),
    "rajkot railway station": (22.3112, 70.8021, "Rajkot Railway Station, Rajkot, Gujarat, India"),
    "yagnik road": (22.2984, 70.7979, "Yagnik Road, Rajkot, Gujarat, India"),
    "kalawad road": (22.2882, 70.7788, "Kalawad Road, Rajkot, Gujarat, India"),
    "madhapar": (22.3275, 70.7816, "Madhapar, Rajkot, Gujarat, India"),
    "bhaktinagar": (22.2748, 70.8066, "Bhaktinagar, Rajkot, Gujarat, India"),
}

def get_coordinates_fallback(address):
    """
    Returns latitude, longitude, and formatted address for demo locations.
    Falls back to Ahmedabad center coordinates if location is unknown.
    """
    addr_lower = address.lower()
    for key, val in MOCK_LOCATIONS.items():
        if key in addr_lower:
            return val[0], val[1], val[2]
    # Default fallback to center of Ahmedabad for unknown addresses, but keep address name clean
    return 23.0225, 72.5714, f"{address} (Offline Fallback)"


def home(request):
    """
    Renders the homepage containing links to other tasks.
    """
    return render(request, "home.html")


def show_restaurant_location(request):
    """
    Handles restaurant search, converts the address to latitude and longitude,
    and displays it on an embedded Google Map.
    """
    context = {}
    
    if request.method == "POST":
        address = request.POST.get("address", "").strip()
        
        if address:
            geocode_url = "https://maps.googleapis.com/maps/api/geocode/json"
            params = {
                "address": address,
                "key": settings.GOOGLE_MAPS_API_KEY
            }
            
            try:
                response = requests.get(geocode_url, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    status = data.get("status")
                    
                    if status == "OK":
                        location = data["results"][0]["geometry"]["location"]
                        latitude = location["lat"]
                        longitude = location["lng"]
                        formatted_address = data["results"][0]["formatted_address"]
                        
                        context["address"] = formatted_address
                        context["latitude"] = latitude
                        context["longitude"] = longitude
                        context["success"] = True
                        
                        # Generate API-based map url since Geocoding API worked
                        context["map_url"] = f"https://www.google.com/maps/embed/v1/place?key={settings.GOOGLE_MAPS_API_KEY}&q={latitude},{longitude}"
                    else:
                        # Fallback to local geocoder and keyless map embed url if Geocoding API failed/denied
                        lat, lng, fmt_addr = get_coordinates_fallback(address)
                        context["address"] = fmt_addr
                        context["latitude"] = lat
                        context["longitude"] = lng
                        context["success"] = True
                        context["warning_message"] = f"Using local offline geocoder (Google API status: {status})."
                        
                        # Keyless Google Map Embed URL fallback
                        context["map_url"] = f"https://maps.google.com/maps?q={lat},{lng}&z=15&output=embed"
                else:
                    # Fallback on HTTP Error
                    lat, lng, fmt_addr = get_coordinates_fallback(address)
                    context["address"] = fmt_addr
                    context["latitude"] = lat
                    context["longitude"] = lng
                    context["success"] = True
                    context["warning_message"] = f"Using local offline geocoder (HTTP status: {response.status_code})."
                    context["map_url"] = f"https://maps.google.com/maps?q={lat},{lng}&z=15&output=embed"
                    
            except Exception as e:
                # Fallback on connection error
                lat, lng, fmt_addr = get_coordinates_fallback(address)
                context["address"] = fmt_addr
                context["latitude"] = lat
                context["longitude"] = lng
                context["success"] = True
                context["warning_message"] = f"Using local offline geocoder due to error: {str(e)}"
                context["map_url"] = f"https://maps.google.com/maps?q={lat},{lng}&z=15&output=embed"
        else:
            context["error_message"] = "Please enter a valid address."
            
    return render(request, "restaurant_map.html", context)


def search_by_distance(request):
    """
    Converts user's location address into coordinates.
    Then geocodes 5 hardcoded Flipkart Pickup Points in Ahmedabad,
    calculates distances using the manual Haversine formula,
    sorts them from nearest to farthest, and displays them with maps.
    """
    context = {}
    
    if request.method == "POST":
        user_address = request.POST.get("address", "").strip()
        
        if user_address:
            geocode_url = "https://maps.googleapis.com/maps/api/geocode/json"
            user_params = {
                "address": user_address,
                "key": settings.GOOGLE_MAPS_API_KEY
            }
            
            # Initialize variables
            user_lat, user_lng, user_formatted_address = None, None, None
            use_fallback = False
            fallback_reason = ""
            
            try:
                user_response = requests.get(geocode_url, params=user_params)
                
                if user_response.status_code == 200:
                    user_data = user_response.json()
                    user_status = user_data.get("status")
                    
                    if user_status == "OK":
                        user_loc = user_data["results"][0]["geometry"]["location"]
                        user_lat = user_loc["lat"]
                        user_lng = user_loc["lng"]
                        user_formatted_address = user_data["results"][0]["formatted_address"]
                    else:
                        use_fallback = True
                        fallback_reason = f"Google API returned: {user_status}"
                else:
                    use_fallback = True
                    fallback_reason = f"HTTP Status: {user_response.status_code}"
            except Exception as e:
                use_fallback = True
                fallback_reason = str(e)
            
            # Apply local geocoder for user if Google API failed/denied
            if use_fallback:
                user_lat, user_lng, user_formatted_address = get_coordinates_fallback(user_address)
                context["warning_message"] = f"Using offline fallback geocoder ({fallback_reason})."
            
            # Select pickup points dynamically based on target city
            if "rajkot" in user_address.lower():
                pickup_points_names = [
                    "Rajkot Railway Station, Rajkot",
                    "Yagnik Road, Rajkot",
                    "Kalawad Road, Rajkot",
                    "Madhapar, Rajkot",
                    "Bhaktinagar, Rajkot"
                ]
            else:
                # Default to Ahmedabad pickup points
                pickup_points_names = [
                    "Ahmedabad Railway Station, Ahmedabad",
                    "CG Road, Ahmedabad",
                    "Satellite, Ahmedabad",
                    "Maninagar, Ahmedabad",
                    "Prahlad Nagar, Ahmedabad"
                ]
            
            results_list = []
            
            for point_name in pickup_points_names:
                point_lat, point_lng = None, None
                point_fallback = False
                
                # Geocode point
                try:
                    point_params = {
                        "address": point_name,
                        "key": settings.GOOGLE_MAPS_API_KEY
                    }
                    point_response = requests.get(geocode_url, params=point_params)
                    if point_response.status_code == 200:
                        point_data = point_response.json()
                        if point_data.get("status") == "OK":
                            point_loc = point_data["results"][0]["geometry"]["location"]
                            point_lat = point_loc["lat"]
                            point_lng = point_loc["lng"]
                        else:
                            point_fallback = True
                    else:
                        point_fallback = True
                except:
                    point_fallback = True
                
                # Local fallback coordinates for pickup points
                if point_fallback:
                    point_lat, point_lng, _ = get_coordinates_fallback(point_name)
                
                # Calculate manual Haversine distance
                distance_km = calculate_haversine_distance(
                    user_lat, user_lng, point_lat, point_lng
                )
                
                # Generate appropriate map embed URL (standard keyless if using fallback, otherwise API-based)
                if point_fallback or use_fallback:
                    map_url = f"https://maps.google.com/maps?q={point_lat},{point_lng}&z=15&output=embed"
                else:
                    map_url = f"https://www.google.com/maps/embed/v1/place?key={settings.GOOGLE_MAPS_API_KEY}&q={point_lat},{point_lng}"
                
                results_list.append({
                    "name": point_name.split(",")[0],
                    "address": point_name,
                    "latitude": point_lat,
                    "longitude": point_lng,
                    "distance": round(distance_km, 2),
                    "map_url": map_url
                })
            
            # Sort pickup points by nearest distance
            results_list.sort(key=lambda x: x["distance"])
            
            context["user_address"] = user_formatted_address
            context["user_latitude"] = user_lat
            context["user_longitude"] = user_lng
            context["pickup_points"] = results_list
            context["success"] = True
            
            return render(request, "results.html", context)
        else:
            context["error_message"] = "Please enter your address."
            
    return render(request, "search_distance.html", context)
