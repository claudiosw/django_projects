from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mview(request):
    num_visits = request.session.get('num_visits', 0) + 1
    resp = HttpResponse('view count='+str(num_visits))
    resp.set_cookie('hello', 42) # No expired date = until browser close
    #resp.set_cookie('sakaicar', 42, max_age=1000) # seconds until expire
    request.session['num_visits'] = num_visits
    # if num_visits > 4 : del(request.session['num_visits'])
    resp.set_cookie('dj4e_cookie', 'e9d3e114', max_age=1000)
    return resp
