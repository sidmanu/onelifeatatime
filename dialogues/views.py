from django.shortcuts import render

from dialogues.models import Dialogue
import dialogues.queries as q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect


import datetime

def index(request):
	context = {}
	context['total_count'] = q.get_total_count()
	context['zone_list'] = q.get_all_zones()
	return render(request, 'dialogues/index.html', context)

def login_user(request):
    context = {}
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/leaders_dashboard/')
    return render(request, 'dialogues/login.html', context)

@login_required
def leaders_dashboard(request):
	context = {}
	total_count = q.get_total_count()
	
	
	context['total_count'] = total_count
	return render(request, 'dialogues/leaders_dashboard.html', context)



def ajax_get_districts_in_chapter(request, parent_id):
	context = {}
	context['options'] = q.get_districts_in_chapter(parent_id)

	return render(request, 'dialogues/ajax_select_options.html', context)

def ajax_get_chapters_in_region(request, parent_id):
	context = {}
	context['options'] = q.get_chapters_in_region(parent_id)

	return render(request, 'dialogues/ajax_select_options.html', context)

def ajax_get_regions_in_zone(request, parent_id):
	context = {}
	context['options'] = q.get_regions_in_zone(parent_id)

	return render(request, 'dialogues/ajax_select_options.html', context)

@csrf_exempt
def submit_new_dialogue(request):
	context = {}
	if request.method == 'POST':
		dist = q.get_district_by_id(request.POST.get('district_select'))
		dlg = Dialogue(member_name=request.POST.get('member_name','dummy'),
				friend_name=request.POST.get('friend_name','dummy_friend'),
				member_email=request.POST.get('member_email','abc@xyz.com'),
				district=dist, dialogue_date = datetime.date.today())
			
		dlg.save()
	
	return render(request, 'dialogues/index.html', context)
