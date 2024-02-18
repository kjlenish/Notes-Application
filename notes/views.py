from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer, UserSerializer, VersionSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json



class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

@api_view(['POST'])
def signup(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            username = serializer.data.get('username')
            return Response({'message': f'Account created for {username}. Log in...'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class NoteCreate(APIView):
    def post(self, request, *args, **kwargs):
        serializer = NoteSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def note_detail(request, id):
    try:
        note = Note.objects.get(id=id)
    except Note.DoesNotExist:
        return JsonResponse({'error': 'Note does not exist'}, status=404)

    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = json.loads(request.body)

        serializer = NoteSerializer(note, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
def share_note(request, id):
    try:
        note = Note.objects.get(id=id)
    except Note.DoesNotExist:
        return Response({'error': 'Note does not exist'}, status=status.HTTP_404_NOT_FOUND)

    return Response({'message': 'Note shared successfully'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_note_version_history(request, id):
    try:
        note = Note.objects.get(id=id)
        version_history = note.version_history.all()
        serializer = VersionSerializer(version_history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Note.DoesNotExist:
        return Response({'error': 'Note does not exist'}, status=status.HTTP_404_NOT_FOUND)
