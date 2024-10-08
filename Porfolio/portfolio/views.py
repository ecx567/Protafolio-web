from django.shortcuts import render, redirect
from .models import Project
#from django.contrib.auth.decorators import login_required



def home(request):
    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})


"""
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def signup(request):
  if request.method == 'GET ':
    return render(request, 'signup.html',{
    'form':UserCreationForm
  })
  else:
    if request.POST['password1'] == request.POST['password2']:
      try:
        user = User.objects.create_user(username=request.POST['username'],
        password=request.POST['password1'])
        user.save()
        login(request, user)
        return redirect ('home')
      except IntegrityError:
        return render(request, 'signup.html',{
    'form':UserCreationForm,
    "error": 'User already exists'
  })
    return render(request, 'signup.html',{
    'form':UserCreationForm,
    "error": 'Passwords do not match'
  })

@login_required  
def signout(request):
  logout(request)
  return redirect('home')

def signin(request):
  if request.method == 'GET':
    return render(request, 'signin.html',{
    'form':AuthenticationForm
  })
  else:
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
      return render(request, 'signin.html',{
    'form':AuthenticationForm,
    "error": 'Username or password is incorrect'
  })
    else:
      login(request, user)
      return redirect('home')




"""

"""
class ExperienciaListView(ListView):
    model = Experiencia
    template_name = 'experiencia/experiencia_list.html'
    context_object_name = 'experiencias'

class ExperienciaCreateView(CreateView):
    model = Experiencia
    template_name = 'experiencia/experiencia_form.html'
    fields = ['institucion_del_curso', 'descripcion_curso', 'fecha_curso', 'numero_horas']
    success_url = reverse_lazy('experiencia_list')

class ExperienciaUpdateView(UpdateView):
    model = Experiencia
    template_name = 'experiencia/experiencia_form.html'
    fields = ['institucion_del_curso', 'descripcion_curso', 'fecha_curso', 'numero_horas']
    success_url = reverse_lazy('experiencia_list')

class ExperienciaDeleteView(DeleteView):
    model = Experiencia
    template_name = 'experiencia/experiencia_confirm_delete.html'
    success_url = reverse_lazy('experiencia_list')



"""
