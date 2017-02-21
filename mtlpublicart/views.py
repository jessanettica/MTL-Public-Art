from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response

from mtlpublicart.forms import *
from mtlpublicart.models import *

import urllib2
import random
import json


def index(request):
    return render(request, 'mtlpublicart/main_page.html', {
        "title": "Hello World"
    })


def logout_page(request):
    """Display the logout page."""
    logout(request)
    return HttpResponseRedirect('/montreal_public_art')


def register_page(request):
    """Display the register page."""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password']
                )
            authenticated_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
                                )
            login(request, authenticated_user)
            return HttpResponseRedirect('/montreal_public_art')
    form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('registration/register.html', variables)
