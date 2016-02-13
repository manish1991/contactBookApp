from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'views.home'),
    url(r'^createContact$', 'contacts.views.createContact'),
    url(r'^getContacts/$', 'contacts.views.get_contacts'),
    url(r'^createContact/(?P<contact_id>\d+)/(?P<action>\w+)/$', 'contacts.views.createContact'),
    #(r'^kinoscrap/(?P<kinoid>\d+)/(?P<shortid>\d+)/$', kinoscrap),


)