from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Finch


# finches = [
#   {'species': 'Lolo', 'population': 'tabby', 'habitat': 'furry little demon', 'note': 3},
#   {'species': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
# ]

# Create your views here.

# define home view here - '/'
# GET - Home
def home(request):
  #remember to include the .html file extension
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# index view
def finches_index(request):
  finches = Finch.objects.all()
  for finch in finches:
    print(finch)
  return render(request, 'finches/index.html', { 'finches': finches })

# detail view
def finches_detail(request, finch_id):
  # YOU'RE GONNA NEED THIS ISH FOR THE PROJECT
  # THE ID COMES FROM THE URL. PAY ATTENTION DUDE
  finch = Finch.objects.get(id=finch_id)

  return render(request, 'finches/detail.html', { 'finch': finch})

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  success_url = 'finches/{finch_id}'
  
class FinchUpdate(UpdateView):
  model = Finch
  fields = ['population', 'habitat', 'about']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'