import requests

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response


# Task 1
class MusicWeather(APIView):

    def get(self, request, city):
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": settings.OPENWEATHER_API_KEY,
            "units": "metric"
        }

        try:
            response = requests.get(url, params=params)
            if response.status_code == 404:
                return Response({"error": "City not found"}, status=404)
            elif response.status_code != 200:
                return Response({"error": "Failed to fetch weather data"}, status=response.status_code)

            data = response.json()
            return Response({
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            })
        except requests.RequestException as e:
            return Response({"error": str(e)}, status=500)


# Task 2
class FoodLocation(APIView):

    def get(self, request):
        restaurant_name = request.query_params.get("name") or request.query_params.get("restaurant")
        if not restaurant_name:
            return Response({"error": "Restaurant name query parameter is required"}, status=400)

        # Fallback mocking if no valid Google Maps API Key is provided
        if settings.GOOGLE_MAPS_API_KEY == "MOCK_GOOGLE_MAPS_API_KEY" or not settings.GOOGLE_MAPS_API_KEY:
            name_lower = restaurant_name.lower()
            if "mcdonald" in name_lower:
                lat, lng = 37.774929, -122.419416  # San Francisco
            elif "starbucks" in name_lower:
                lat, lng = 40.712776, -74.005974  # New York
            elif "subway" in name_lower:
                lat, lng = 41.878113, -87.629798  # Chicago
            else:
                lat, lng = 34.052234, -118.243685  # Los Angeles
            
            return Response({
                "latitude": lat,
                "longitude": lng,
                "note": "Mock coordinates returned (no Google Maps API Key configured)"
            })

        url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            "address": restaurant_name,
            "key": settings.GOOGLE_MAPS_API_KEY
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()

            if data.get("status") == "OK" and data.get("results"):
                location = data["results"][0]["geometry"]["location"]
                return Response({
                    "latitude": location["lat"],
                    "longitude": location["lng"]
                })
            elif data.get("status") == "ZERO_RESULTS":
                return Response({"error": "Restaurant not found"}, status=404)
            else:
                status = data.get("status", "ERROR")
                error_message = data.get("error_message", "Failed to retrieve location")
                return Response({"error": f"Geocoding API error: {status} - {error_message}"}, status=400)
        except requests.RequestException as e:
            return Response({"error": str(e)}, status=500)


# Task 3
class CountryInfo(APIView):

    def get(self, request, country_name):
        url = f"https://restcountries.com/v3.1/name/{country_name}"

        try:
            response = requests.get(url)
            if response.status_code != 200:
                return Response({"error": "Country not found"}, status=response.status_code)

            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                country_data = data[0]
                return Response({
                    "country": country_data["name"]["common"],
                    "capital": country_data.get("capital", ["N/A"])[0],
                    "population": country_data["population"]
                })
            return Response({"error": "Country not found"}, status=404)
        except requests.RequestException as e:
            return Response({"error": str(e)}, status=500)


# Task 4
class GithubRepos(APIView):

    def get(self, request, username):
        url = f"https://api.github.com/users/{username}/repos"
        headers = {
            "User-Agent": "Django-DRF-App"
        }

        try:
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                return Response({"error": "User not found"}, status=response.status_code)

            repos = response.json()
            repo_names = [repo["name"] for repo in repos]
            return Response(repo_names)
        except requests.RequestException as e:
            return Response({"error": str(e)}, status=500)