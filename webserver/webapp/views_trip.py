from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponseBadRequest
from django.template.loader import render_to_string

from rest_framework.request import Request
from rest_framework.decorators import api_view

from webapp import api_trip
from webapp.Category import Category
from webapp.Country import Country
from webapp.Trip import Trip


@api_view(['GET'])
def trip_get(request: Request):
    """
    Get a Trip (which may have already been or have not been prepared)
    """
    trip_id = request.query_params.get('id')
    if trip_id is None:
        return HttpResponseBadRequest()

    try:
        trip = api_trip.get_trip(trip_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()

    return HttpResponse(render_to_string('trip.html', _trip_to_view(trip)))


@api_view(['GET'])
def trip_step(request: Request):
    parameters = request.query_params

    home_country = parameters.get('hc')
    if home_country is None:
        return HttpResponse(render_to_string('index.html', {
            'countries': _destinations(),
        }))

    interest_ids = parameters.get('in')
    if interest_ids is None:
        return HttpResponse(render_to_string('step_in.html', {
            'hc': home_country,
            'categories': _categories(),
        }))

    destinations = parameters.get('dst')
    if destinations is None:
        return HttpResponse(render_to_string('step_dst.html', {
            'hc': home_country,
            'interests': interest_ids,
            'countries': _destinations(),
        }))

    trip = api_trip.create_trip(home_country, interest_ids, destinations)
    return HttpResponseRedirect('/trip?id={}'.format(trip.id))


def _trip_to_view(trip: Trip) -> dict:
    """
    Transform a Trip object into a dictionary for the HTML template
    """
    # TODO
    return {
        'id': trip.id
    }


def _categories() -> list:
    """
    Get a list of all available categories
    """
    # categories_rs = Category.objects.all()
    result = [
        {
            'name': 'a', # category.name,
            'id': category, # category.id,
        }
        for category in range(2) # categories_rs
    ]
    return result


def _destinations() -> list:
    """
    Get a list of all available countries
    """
    # countries_rs = Country.objects.all()
    result = [
        {
            'name': 'c', # country.name,
            'id': country # country.id,
        }
        for country in range(2) # countries_rs
    ]
    return result
