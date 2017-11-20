from django.db import models

# Create your models here.


class Person(models.Model):
	first_name = models.CharField(max_length=32)
	last_name = models.CharField(max_length=32)

	@property
	def name(self):
		return "{} {}".format(self.first_name, self.last_name)

	def __str__(self):
		return self.name


class Movie(models.Model):
	title = models.CharField(max_length=128)
	description = models.TextField()
	director = models.ForeignKey(Person, related_name='direcotr')
	actors = models.ManyToManyField(Person, related_name='actors', through='Cast')
	year = models.IntegerField()

	def __str__(self):
		return self.title 

	@property
	def director_name(self):
		return self.director.name

	@property
	def actors_list(self):
		return ", ".join([str(actor) for actor in self.actors.all()])


class Cast(models.Model):
	person_id = models.ForeignKey(Person)
	movie_id = models.ForeignKey(Movie)
	role = models.CharField(max_length=128, null=True)

	def __str__(self):
		return self.role