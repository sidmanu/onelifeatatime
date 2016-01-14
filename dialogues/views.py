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
                return HttpResponseRedirect('/dialogues/leaders_dashboard/')
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


def export_dialogue_list_xls(request, dialogue_list):
    import xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=dialogue_list.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("All dialogues")
    
    row_num = 0
    
    columns = [
        (u"Member Name", 8000),
        (u"Member Email", 8000),
        (u"Friend Name", 8000),
        (u"Zone", 6000),
        (u"Region", 6000),
        (u"Chapter", 6000),
        (u"District", 6000),
        (u"Date", 6000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1
    for d in dialogue_list:
        row_num += 1
        row = [
            d.member_name,
            d.member_email,
            d.friend_name,
            d.district.parent.parent.parent.name,
            d.district.parent.parent.name,
            d.district.parent.name,
            d.district.name,
			d.dialogue_date
        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            
    wb.save(response)
    return response



def export_entire_dialogue_list_xls(request):

	all_dialogues = q.get_all_dialogues()
	return export_dialogue_list_xls(request, all_dialogues)
   

def export_dialogue_list_date_range_xls(request):
	
	start_date = request.GET.get('start_date','01/11/2015 8:01 PM')
	start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y %I:%M %p').strftime('%Y-%m-%d')

	end_date = request.GET.get('end_date','01/11/2015 8:08 PM')
	end_date = datetime.datetime.strptime(end_date, '%m/%d/%Y %I:%M %p').strftime('%Y-%m-%d')
	dialogues = q.get_dialogues_in_date_range(start_date, end_date) 

	return export_dialogue_list_xls(request, dialogues)

