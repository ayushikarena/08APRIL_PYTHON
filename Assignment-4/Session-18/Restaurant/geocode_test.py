# Task 1: Standalone Python Script for Geocoding
# This script uses the requests library to send a request to Google's Geocoding API.
# It includes a local fallback to display coordinates even if the API Key is not configured/billed.

import requests

# Set the target address to search
address = "IIM Ahmedabad, Gujarat"

# Google Geocoding API Endpoint URL
url = "https://maps.googleapis.com/maps/api/geocode/json"

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
API_KEY = "YOUR_API_KEY"

# Define the parameters to send with the HTTP GET request
parameters = {
    "address": address,
    "key": API_KEY
}

# Local Fallback dictionary for testing without active billing/key
MOCK_LOCATIONS = {
    "iim ahmedabad": (23.0312, 72.5375, "IIM Ahmedabad, Gujarat, India"),
}

def print_result(lat, lng, formatted_addr, is_fallback=False):
    suffix = " (Offline Local Fallback)" if is_fallback else ""
    print(f"Address: {formatted_addr}{suffix}")
    print(f"Latitude: {lat}")
    print(f"Longitude: {lng}")

try:
    # Send the GET request to Google API
    response = requests.get(url, params=parameters)
    
    if response.status_code == 200:
        data = response.json()
        api_status = data.get("status")
        
        if api_status == "OK":
            first_result = data["results"][0]
            latitude = first_result["geometry"]["location"]["lat"]
            longitude = first_result["geometry"]["location"]["lng"]
            formatted_address = first_result["formatted_address"]
            print_result(latitude, longitude, formatted_address)
        else:
            # Fallback to local coordinate database
            lat, lng, fmt_addr = MOCK_LOCATIONS["iim ahmedabad"]
            print_result(lat, lng, fmt_addr, is_fallback=True)
            print(f"[Notice: Google Geocoding API returned status '{api_status}', using local fallback]")
    else:
        # Fallback to local coordinate database
        lat, lng, fmt_addr = MOCK_LOCATIONS["iim ahmedabad"]
        print_result(lat, lng, fmt_addr, is_fallback=True)
        print(f"[Notice: HTTP request failed with code {response.status_code}, using local fallback]")

except Exception as error:
    # Fallback on network/connection issues
    lat, lng, fmt_addr = MOCK_LOCATIONS["iim ahmedabad"]
    print_result(lat, lng, fmt_addr, is_fallback=True)
    print(f"[Notice: Network error occurred ({error}), using local fallback]")
