
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from webapp.models import JUser

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import \
    HTTP_201_CREATED, \
    HTTP_400_BAD_REQUEST, \
    HTTP_403_FORBIDDEN, \
    HTTP_409_CONFLICT, \
    HTTP_422_UNPROCESSABLE_ENTITY


@api_view(['POST'])
def user_register(request):
    try:
        username = request.data['username']
        password = request.data['password']
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        residence = request.data.get('country')
    except KeyError:
        return Response(None, HTTP_400_BAD_REQUEST)

    try:
        user = JUser.objects.create_user(
            username=username, password=password,
            email=email, first_name=first_name, last_name=last_name,
            country=residence
        )
    except:
        return Response(None, HTTP_409_CONFLICT)

    user.refresh_from_db()
    auth.login(request, user)

    return Response(None, HTTP_201_CREATED)


@api_view(['POST'])
def user_sign_in(request):
    try:
        username = request.data['username']
        password = request.data['password']
    except KeyError:
        return Response(None, HTTP_400_BAD_REQUEST)

    user = auth.authenticate(request, username=username, password=password)
    if user is None:
        return Response(None, HTTP_403_FORBIDDEN)

    auth.login(request, user)
    return Response(None)