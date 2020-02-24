from django.urls import path
from .views import studentList, studentCreate, studentUpdate, studentDelete
urlpatterns = [
	path('',studentList, name="list"),
	path('create/',studentCreate, name="create"),
	path('update/<id>/',studentUpdate, name="update"),
	path('delete/<id>/',studentDelete, name="delete"),
]