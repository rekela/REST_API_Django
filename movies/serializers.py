from .models import Movie, Person
from rest_framework	import serializers


class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = ('title', 'description', 'director_name', 'actors_list', 'year')


class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = ('first_name', 'last_name')