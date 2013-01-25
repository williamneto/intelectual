# -*- coding: utf-8 -*-
from mongoengine.django.shortcuts import get_document_or_404
from django.shortcuts import render
from intelectual.accounts.models import AdminProfile

def superuser_only(function):
    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, 'access_denied.html', locals())           
        return function(request, *args, **kwargs)
    return _inner

    
