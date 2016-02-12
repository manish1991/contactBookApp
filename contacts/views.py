import json
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from contacts.forms import ContactForm
from contacts.models import Contact



@login_required
@csrf_exempt
def createContact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            current_user = request.user
            Contact.objects.create(firstName=firstName,lastName=lastName,
                                   email=email,phone_number=phone_number,
                                   created_by=current_user
            )
            return HttpResponseRedirect('/')
        else:
            lform = form
            return render_to_response('createContact.html', locals())
    else:
        form = ContactForm()
        state = "Please enter your new password"
        return render_to_response('createContact.html', locals())   





@login_required
@csrf_exempt
def  get_contacts(request):
    clicked_alphabet = request.POST.get('clicked_alphabet')
    filtered_contact_list = Contact.objects.filter(firstName__startswith=clicked_alphabet).values_list('firstName', 'lastName', 'email', 'phone_number')
    return HttpResponse(json.dumps({'status': 'success', 'filtered_contact_list': list(filtered_contact_list)}))


