# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
# Create your views here.
def todo(request):
	todo_items=TodoItem.objects.all()
	return render(request,'todo.html',{'all_items':todo_items})

def addTodo(request):
	new_item=TodoItem(content=request.Post['content'])
	new_item.save()
	return HttpResponseRedirect('/todo/')

def deleteTodo(request,todo_id):
	item_to_delete=TodoItem.objects.get(object=todo_id)
	new_item=TodoItem(content=request.Post['content'])
	new_item.save()
	return HttpResponseRedirect('/todo/')