from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import TodoItem

first_time = True

# Create your views here.
def todoView(request):
  all_todo_items = TodoItem.objects.all()
  return render(request, 'index.html', 
  {'all_items': all_todo_items})

def moreInfo(request, todo_id):
	item_to_view = TodoItem.objects.get(id=todo_id)
	return render(request, 'view.html', {'todo_item': item_to_view})

def editTodo(request, todo_id):
	item_to_edit = TodoItem.objects.get(id=todo_id)
	return render(request, 'edit.html', {'todo_item': item_to_edit})

def saveEdit(request, todo_id):
	item_to_edit = TodoItem.objects.get(id=todo_id)
	item_to_edit.content = request.POST['content']
	item_to_edit.desc = request.POST['desc']
	item_to_edit.save()
	return HttpResponseRedirect('/')

def addTodo(request):
  new_item = TodoItem(content = request.POST['content'], done = False, desc="")
  new_item.save()
  return HttpResponseRedirect('/')

def deleteTodo(request, todo_id):
  item_to_delete = TodoItem.objects.get(id=todo_id)
  item_to_delete.delete()
  return HttpResponseRedirect('/')

def toggleDone(request, todo_id):
	item_to_toggle = TodoItem.objects.get(id=todo_id)
	print(item_to_toggle.done)
	if item_to_toggle.done:
		item_to_toggle.done = False
	else:
		item_to_toggle.done = True
	item_to_toggle.save()
	return HttpResponseRedirect('/')

def coverImage(request):
    image_data = open("./todo/app.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")