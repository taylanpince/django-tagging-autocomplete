from django.http import HttpResponse
from django.core import serializers
from tagging.models import Tag

def json_list_tags(request):
	try:
		tags = Tag.objects.filter(name__startswith=request.GET['q']).values_list('name', flat=True)
	except MultiValueDictKeyError:
		pass
	
	return HttpResponse('\n'.join(tags), mimetype='text/plain')