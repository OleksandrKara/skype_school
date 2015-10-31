# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

def home_handler(request):
    return render_to_response('home.html')

def main_page(request):
    return render_to_response('index.html')

def ceni_handler(request):
    return render_to_response('ceni.html')
	
def otzivi_handler(request):
    return render_to_response('otzivi.html')

def faq_handler(request):
    return render_to_response('faq.html')