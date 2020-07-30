from django.shortcuts import render,redirect
from .models import Todo
from django.views.decorators.csrf import csrf_protect
# Create your views here.
@csrf_protect
def home(request):
	context = {
	'todos' : Todo.objects.all()
	}
	if request.method == "POST":
		if 'add' in request.POST:
			post = request.POST.get('todo')
			todo = Todo(todo=post)
			todo.save()
			return redirect('/')

		if 'remove' in request.POST:
			check = request.POST.getlist('todoCheck')
			for todo_id in check:
				Todo.objects.get(id=int(todo_id)).delete()
			return redirect('/')
	return render(request,'index.html',context)
