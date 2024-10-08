from django.shortcuts import render, redirect, get_object_or_404
from .models import Experiencia
from .forms import ExperienciaForm

# Vista para listar las experiencias
def experiencia_list(request):
    experiencias = Experiencia.objects.all()
    return render(request, 'experiencia/experiencia_list.html', {'experiencias': experiencias})

# Vista para agregar una nueva experiencia
def agregar_experiencia(request):
    if request.method == 'POST':
        form = ExperienciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('experiencia_list')
    else:
        form = ExperienciaForm()

    return render(request, 'experiencia/agregar_experiencia.html', {'form': form})

# Vista para editar una experiencia existente
def editar_experiencia(request, pk):
    experiencia = get_object_or_404(Experiencia, pk=pk)
    if request.method == 'POST':
        form = ExperienciaForm(request.POST, instance=experiencia)
        if form.is_valid():
            form.save()
            return redirect('experiencia_list')
    else:
        form = ExperienciaForm(instance=experiencia)

    return render(request, 'experiencia/editar_experiencia.html', {'form': form, 'experiencia': experiencia})

# Vista para eliminar una experiencia
def eliminar_experiencia(request, pk):
    experiencia = get_object_or_404(Experiencia, pk=pk)
    if request.method == 'POST':
        experiencia.delete()
        return redirect('experiencia_list')
    return render(request, 'experiencia/eliminar_experiencia.html', {'experiencia': experiencia})
