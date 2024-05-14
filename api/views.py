from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import CustomUser, Paragraph
from .serializers import UserRegistrationSerializer, UserLoginSerializer, ParagraphSerializer
from django.http import Http404

# User Registration API View
class UserRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login API View
class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Paragraph List and Create API View
class ParagraphListCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        paragraphs = Paragraph.objects.all()
        serializer = ParagraphSerializer(paragraphs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ParagraphSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Paragraph Detail, Update, and Delete API View
class ParagraphDetailAPIView(APIView):
    def get_object(self, pk):
      try:
        return Paragraph.objects.get(pk=pk)
      except Paragraph.DoesNotExist:
        raise Http404

    def get(self, request, pk, *args, **kwargs):
      paragraph = self.get_object(pk)
      serializer = ParagraphSerializer(paragraph)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, *args, **kwargs):
        paragraph = self.get_object(pk)
        serializer = ParagraphSerializer(paragraph, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        paragraph = self.get_object(pk)
        paragraph.delete()
        return Response({'message': 'Paragraph deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# Paragraph search for updating and getting APIView
class ParagraphSearchView(APIView):
    def get(self, request, *args, **kwargs):
        if 'word' not in request.query_params:
            return Response({'message': 'Please provide the search term (word) in the query parameters.'})

        word = request.query_params.get('word', '')
        if not word:
            return Response({'error': 'Search term not provided'}, status=status.HTTP_400_BAD_REQUEST)

        paragraphs = Paragraph.objects.filter(content__icontains=word)
        serializer = ParagraphSerializer(paragraphs, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        word = request.data.get('word', '')
        if not word:
            return Response({'error': 'Search term not provided in request body'}, status=status.HTTP_400_BAD_REQUEST)

        paragraphs = Paragraph.objects.filter(content__icontains=word)
        serializer = ParagraphSerializer(paragraphs, many=True)
        return Response(serializer.data)





    # ViewSets create views that allow you



    



