from django.contrib import admin
from .models import Person, Movie, Cast

# Register your models here.


@ admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	pass


@ admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ("title", )

# , 	def get_person_name(self, obj):
# 		return obj.person.name


@ admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
	pass