from django.shortcuts import render

from .models import Parent

def index(request):
	parent_list = Parent.objects.order_by("id")
	context = {'parent_list': parent_list}
	return render(request, 'parent/index.html', context)