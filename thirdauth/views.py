from django.shortcuts import render_to_response
from django.template.context import RequestContext
from contacts.models import Contact

def home(request):
	user = request.user
	print("user123",user)
	all_contact_list = Contact.objects.filter(created_by=request.user.id)
	return render_to_response('home.html', locals())


