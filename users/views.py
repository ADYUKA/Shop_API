from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from users.models import ConfirmCode
from . import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import random
import string


@api_view(['POST'])
def register_api_view(request):
    serializer = serializers.UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.create_user(username=username, password=password, is_active=False)

    # create code(6-symbol)
    user_id = User.objects.get(username=username)
    code = ''.join(random.choice(string.digits) for i in range(6))
    code_obj = ConfirmCode.objects.create(code=code, user_id=user_id.id)
    return Response({
        'success': 'user created; confirmation required',
        'confirmation code': code_obj.code
    }, status=status.HTTP_201_CREATED
    )


@api_view(['POST'])
def confirm_user_api_view(request):
    serializer = serializers.ConfirmValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    code = request.data.get('code')
    try:
        confirm_code = ConfirmCode.objects.get(code=code)
    except ConfirmCode.DoesNotExist:
        return Response({'error': 'invalid confirmation code'}, status=status.HTTP_400_BAD_REQUEST)

    user_id = confirm_code.user_id
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    confirm_code.delete()
    return Response({'success': 'user confirmed'})


@api_view(['POST'])
def login_api_view(request):
    serializer = serializers.LoginValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response({'Error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)