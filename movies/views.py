from django.shortcuts import render
from .models import Person, Movie, Cast
from .serializers import MovieSerializer, PersonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.
	

class MoviesView(APIView):

	def get(self, request, format=None): # format nie jest potrzebnym argumentem, możemy go nie wpisywać, chodzi o format danych jakie są przesyłane np. za pomocą API
		movies = Movie.objects.all()
		serializer = MovieSerializer(movies, many=True)
		return Response(serializer.data)



class MovieView(APIView):

	def get_object(self, movie_id): # get_object to funkcja pomocnicza stosowana po to, aby pobrać obiekt z bazy
		try:					# i zwrócić obiekt, jeśli istnieje, a jeśli nie - zwróci 404
			return 	Movie.objects.get(pk=movie_id) # f.get_object stosujemy po to żeby nie powtarzac poniżej w GET i DELETE tego samego tylko odwoływac się do tej funkcji
		except Movie.DoesNotExist:
			raise Http404

	def get(self, request, movie_id, format=None):
		movie = self.get_object(movie_id)
		serializer = MovieSerializer(movie)
		return Response(serializer.data)

	def delete(self, request, movie_id, format=None):
		movie = self.get_object(movie_id)
		movie.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def put(self, request, movie_id, format=None):
		movie = self.get_object(movie_id)
		serializer = MovieSerializer(movie, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




