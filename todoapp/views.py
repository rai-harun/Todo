from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def home(request):
    all_data = Todo.objects.all()
    context = {
        'all_data': all_data
    }
    return render(request, 'home.html', context)

def createNote(request):
    form = TodoForm()
    if request.method == 'POST':
        data = TodoForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('home')
    else:
        context = {
            'form': form
        }
        return render(request, 'create_note.html', context)

def updateNote(request, pk):
    # data = TodoForm()
        
    # else:
    context = {}
    note_update = Todo.objects.get(id=pk)
    data_update = TodoForm(instance=note_update)
    
    if request.method == 'POST':
        data_update = TodoForm(request.POST, instance=note_update)
        if data_update.is_valid():
            data_update.save()
            return redirect('/')
    context['data_update'] = data_update
    return render(request, 'update_note.html', context)

def deleteNote(request, pk):
    del_note = Todo.objects.get(pk=pk)
    del_note.delete()
    return redirect('/')

    
