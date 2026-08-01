from django.http import JsonResponse


# JSON Example
# {
#     "name": "Flipkart Smart Watch",
#     "price": 2999
# }

# XML Example
# <product>
#     <name>Flipkart Smart Watch</name>
#     <price>2999</price>
# </product>


def hello_spotify(request):
    return JsonResponse({
        "message": "Hello, Spotify Fans!"
    })