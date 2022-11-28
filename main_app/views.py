from django.shortcuts import render
from django.views.generic.edit import CreateView
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird


# Create your views here.
# Add the following import

# Define the home view
def home(request):
    return render(request, 'home.html')

class BirdUpdate(UpdateView):
  model = Bird
  fields = ['breed', 'description', 'age']
  success_url='/birds/'

  
class BirdDelete(DeleteView):
  model = Bird
  success_url = '/birds/'
    

class BirdCreate(CreateView):
    model = Bird
    fields = '__all__'
    success_url='/birds/'


def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    return render(request, 'birds/detail.html', {'bird': bird})
# Add new view
def birds_index(request):
    birds_list = Bird.objects.all()
    return render(request, 'birds/index.html', {
        'birds': birds_list
    })

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('<h1> About the birdCollector </h1>')