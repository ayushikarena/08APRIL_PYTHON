from unittest.mock import patch
from django.urls import reverse
from django.test import override_settings
from rest_framework import status
from rest_framework.test import APITestCase

class MusicWeatherTests(APITestCase):


    @patch('api.views.requests.get')
    def test_music_weather_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "main": {"temp": 22.5},
            "weather": [{"description": "clear sky"}]
        }

        url = "/api/music-weather/London/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("temperature", response.data)
        self.assertIn("description", response.data)
        self.assertEqual(response.data["temperature"], 22.5)
        self.assertEqual(response.data["description"], "clear sky")

    @patch('api.views.requests.get')
    def test_music_weather_not_found(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        url = "/api/music-weather/UnknownCity/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("error", response.data)


@override_settings(GOOGLE_MAPS_API_KEY='test_key')
class FoodLocationTests(APITestCase):

    @patch('api.views.requests.get')
    def test_food_location_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "OK",
            "results": [
                {
                    "geometry": {
                        "location": {
                            "lat": 37.4224764,
                            "lng": -122.0842499
                        }
                    }
                }
            ]
        }

        url = "/api/food-location/?name=McDonalds"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("latitude", response.data)
        self.assertIn("longitude", response.data)
        self.assertEqual(response.data["latitude"], 37.4224764)
        self.assertEqual(response.data["longitude"], -122.0842499)

    @patch('api.views.requests.get')
    def test_food_location_not_found(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ZERO_RESULTS",
            "results": []
        }

        url = "/api/food-location/?name=NonExistentRestaurant"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("error", response.data)

    def test_food_location_missing_param(self):
        url = "/api/food-location/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)


class CountryInfoTests(APITestCase):

    @patch('api.views.requests.get')
    def test_country_info_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "name": {"common": "France"},
                "capital": ["Paris"],
                "population": 67391582
            }
        ]

        url = "/api/country-info/France/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["country"], "France")
        self.assertEqual(response.data["capital"], "Paris")
        self.assertEqual(response.data["population"], 67391582)

    @patch('api.views.requests.get')
    def test_country_info_not_found(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        url = "/api/country-info/Atlantis/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("error", response.data)


class GithubReposTests(APITestCase):

    @patch('api.views.requests.get')
    def test_github_repos_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"name": "repo-one"},
            {"name": "repo-two"}
        ]

        url = "/api/github-repos/octocat/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0], "repo-one")
        self.assertEqual(response.data[1], "repo-two")

    @patch('api.views.requests.get')
    def test_github_repos_not_found(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        url = "/api/github-repos/nonexistentuser/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("error", response.data)
