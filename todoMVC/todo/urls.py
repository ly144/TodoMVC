from django.urls import path
import todo.views

urlpatterns = [
    path('getTodos/', todo.views.getTodos),
    path('addTodo/', todo.views.addTodo),
    path('doneTodo/', todo.views.doneTodo),
    path('removeTodo/', todo.views.removeTodo),
    path('removeCompleted/', todo.views.removeCompleted),
]
