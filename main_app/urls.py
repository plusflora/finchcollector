from django.urls import path
from . import views

# how we map our urls to views
# views are the 'controllers', they map http request to code. This file is how we match those requests to specific urls.
# `name = 'home'` is a kwarg, which gives the route a name. 
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # index route
  path('finches/', views.finches_index, name='index'),
  # DON'T FUCK THIS UP YOU'LL NEED IT FOR THE PROJECT
  # detail route
  # need an id + the ability to refer to the id
  path('finches/<int:finch_id>', views.finches_detail, name='detail'),
  path('finches/create', views.FinchCreate.as_view(), name='finches_create'),
  path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name='finches_update'),
  path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name='finches_delete')

]