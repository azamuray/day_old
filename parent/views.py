from django.shortcuts import render

from .models import Parent

def index(request):
	latest_parent_list = Parent.objects.order_by('parent_name')
	context = {'latest_parent_list': latest_parent_list}
	return render(request, 'parent/index.html', context)