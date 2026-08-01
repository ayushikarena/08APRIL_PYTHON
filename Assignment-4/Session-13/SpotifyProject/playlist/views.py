from django.shortcuts import render
from django.http import JsonResponse

songs = [
    {"id":1,"name":"Believer"},
    {"id":2,"name":"Perfect"},
    {"id":3,"name":"Shape of You"}
]

def index(request):
    return render(request,"index.html",{"songs":songs})

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def delete_song(request, id):
    global songs

    if request.method == "DELETE":
        songs = [song for song in songs if song["id"] != id]
        return JsonResponse({"success": True})

    return JsonResponse({"success": False})