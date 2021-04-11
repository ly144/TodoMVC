from django.shortcuts import render
from django.http import JsonResponse
import json
from todo.models import Todos

# Create your views here.

def getTodos(request):
	todo_list = Todos.objects.all()
	todos = []
	for todo in todo_list:
		newtodo = {
			'id': todo.id,
			'content': todo.content,
			'status': todo.status
		}
		todos.append(newtodo)
	return JsonResponse(todos, safe=False, json_dumps_params={'ensure_ascii': False})

def addTodo(request):
	todo = json.loads(request.body.decode())
	content = todo.get('content')
	status = todo.get('status')
	res = Todos.objects.filter(content=content)

	if not res:
		Todos.objects.create(content=content, status=status)

	return JsonResponse(todo, safe=False, json_dumps_params={'ensure_ascii': False})

def doneTodo(request):
	todo = json.loads(request.body.decode())
	id = todo.get('id')
	status = todo.get('status')
	Todos.objects.filter(id=id).update(status=status)
	return JsonResponse(todo, safe=False, json_dumps_params={'ensure_ascii': False})

def removeTodo(request):
	todo = json.loads(request.body.decode())
	id = todo.get('id')
	Todos.objects.filter(id=id).delete()
	return JsonResponse(todo, safe=False, json_dumps_params={'ensure_ascii': False})

def removeCompleted(request):
	Todos.objects.filter(status=0).delete()
	return JsonResponse({'content': '', 'status': 1}, safe=False, json_dumps_params={'ensure_ascii': False})