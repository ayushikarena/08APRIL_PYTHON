from django.shortcuts import render

from django.http import JsonResponse

from .models import Movie



def watchlater(request):


    movies=Movie.objects.all()


    return render(

        request,

        "watchlater.html",

        {

        "movies":movies

        }

    )





def delete_movie(request,id):


    if request.method=="DELETE":


        movie=Movie.objects.get(
            id=id
        )


        movie.delete()



        return JsonResponse({

            "status":"success",

            "message":
            "Movie removed successfully"

        })