from django.shortcuts import render, redirect, get_object_or_404
from .models import Todos
from .forms import TodoForm

# Create your views here.

def todos(request):
    todo_items = Todos.objects.all()
    return render(request ,"todo.html", {"todo_items": todo_items} )

def create(request):
    if request.method == 'POST':
        todos_from_form = TodoForm(request.POST)
        if todos_from_form.is_valid():
            todos_from_form.save()  # Save the form data to the database
            return redirect('todo')
    else:
        create_form = TodoForm()
    return render(request, "create_todo.html", {"create_form": create_form} )

def delete(request, todo_id):
    todo_to_delete = get_object_or_404(Todos, id=todo_id)

    todo_to_delete.delete()

    return redirect('todo')

def update(request, todo_id):
    todo_to_update = get_object_or_404(Todos, id=todo_id)

    if request.method == 'POST':
        todos_from_form = TodoForm(request.POST, instance=todo_to_update)
        if todos_from_form.is_valid():
            todos_from_form.save()  # Save the form data to the database
            return redirect('todo')
    else:
        create_form = TodoForm(instance=todo_to_update)

    return render(request, "create_todo.html", {"create_form": create_form} )
