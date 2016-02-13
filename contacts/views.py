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
def createContact(request, contact_id=None, action=None):
    """
        In this form we can create,edit or delete a contact,
        In this view a form for creating new contact or editing an existing contact  
        will be loaded and contact details will be saved in database.
    """
    current_user = request.user
    if contact_id and request.method != "POST" and action=="edit":
        contact = Contact.objects.get(pk=contact_id)
        if contact.created_by != current_user:
            return HttpResponseForbidden()
        else:
            form = ContactForm({'firstName':contact.firstName,'lastName':contact.lastName,
                                'email':contact.email,'phone_number':contact.phone_number})
            return render_to_response('edit_contact.html', locals())
    elif contact_id and request.method != "POST" and action=="delete":
        contact = Contact.objects.get(pk=contact_id)
        contact.delete()
        return HttpResponseRedirect('/')

    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            try:
                contact = Contact.objects.get(pk=contact_id)
                if contact:
                    contact.firstName = firstName
                    contact.lastName = lastName
                    contact.email = email
                    contact.phone_number = phone_number
                    contact.save()
            except:
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
    """
        In this view contacts whose first name starts with the clicked_alphabet
        will be filtered.
    """
    clicked_alphabet = request.POST.get('clicked_alphabet')
    filtered_contact_list = Contact.objects.filter(created_by=request.user.id,firstName__startswith=
                                                   clicked_alphabet).values_list('firstName', 'lastName', 'email', 'phone_number','id')
    return HttpResponse(json.dumps({'status': 'success', 'filtered_contact_list': list(filtered_contact_list)}))


