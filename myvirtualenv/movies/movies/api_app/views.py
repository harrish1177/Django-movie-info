from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from .models import Movies, MovieCast, Actors
from .serializers import MovieCastSerializer, MoviesSerializer, ActorsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
import sched, time
from threading import Thread

is_mutex_on = False
global_result = None


def get_result(data):
    data = list(data)
    movie_info = {}
    if data:
        movie_info = data[0]['movie_id']
    for entry in data:
        del entry['id']
        del entry['movie_id']
    # make a movie info at the start of the response
    if data:
        data.insert(0, movie_info)
    return data

def get_latest_movie(scheduler):
    global global_result
    global is_mutex_on
    # schedule the next call first
    scheduler.enter(60, 1, get_latest_movie, (scheduler,))

    is_mutex_on = True

    latest_movie_id = Movies.objects.order_by('movie_id').last().movie_id
    data = MovieCast.objects.select_related().filter(movie_id=latest_movie_id)
    serializer = MovieCastSerializer(data, many=True)
    global_result = get_result(serializer.data)
    print("updated latest data from DB")

    is_mutex_on = False


# It is assumed that the DB gets updated every 1 min with the latest movie info
# Query DB only once every 1 minute and get the latest movie info.
# for an entire minute, the cached data (global_result) will be sent
def custom_movie_updater_scheduler():
    # update latest movie every 1 minute
    my_scheduler = sched.scheduler(time.time, time.sleep)
    my_scheduler.enter(0, 1, get_latest_movie, (my_scheduler,))
    my_scheduler.run()

thread = Thread(target = custom_movie_updater_scheduler)
thread.start()



# Creating the view here
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_data(request):
    # wait till mutex is released
    while is_mutex_on:
        continue
    # send the cached movie info
    return Response(global_result)

