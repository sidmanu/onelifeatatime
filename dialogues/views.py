from django.shortcuts import render

from dialogues.models import * 
import dialogues.queries as q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

import datetime
from django.core.mail import send_mail

def home_visit_index(request):
	context = {}
	context['zone_list'] = q.get_all_zones()
	return render(request, 'dialogues/home_visit_index.html', context)

def dist_direct_home_visit_index(request, district_id):
	context = {}
	context['district_id'] = district_id
	context['dist'] = q.get_district_by_id(district_id)
	context['total_hv_count'] = q.get_home_visits_count_by_district_id(district_id)
	context['month_hv_count'] = q.get_this_month_home_visits_count_by_district_id(district_id)
	context['total_gi_count'] = q.get_guest_invites_count_by_district_id(district_id)
	context['month_gi_count'] = q.get_this_month_guest_invites_count_by_district_id(district_id)
	context['month_home_visit_list'] = q.get_this_month_home_visits_by_district_id(district_id)
	context['month_guest_invite_list'] = q.get_this_month_guest_invites_by_district_id(district_id)
	return render(request, 'dialogues/hv_direct_district_summary.html', context)


def index(request):
	context = {}
	context['total_count'] = q.get_total_count()
	context['zone_list'] = q.get_all_zones()
	context['daily_count_list'] = q.get_daily_count_list()
	return render(request, 'dialogues/index.html', context)

def logout_user(request):
	context = {}
	context['global_message'] = "You've been logged out."
	logout(request)
	return HttpResponseRedirect('/')

def send_my_activities_email(email_id, dialogues, hv, gi):
	recipients = [email_id]
	subject = 'My Activities Summary- onelifeatatime.in'
	sender = 'noreply@onelifeatatime.in'
	content = """
Dear Bodhisattva,

Here is your dialogue history: 

"""
	
	
	if len(dialogues) == 0:
		content += "You have no recorded dialogues!"

	count = 0
	for d in dialogues:
		count += 1
		line = "%d) %s on %s in %s district\n"%(count, d.friend_name, str(d.dialogue_date),
					d.district.name)
		content += line
		
	if len(hv) == 0:
		content += "You have no recorded home visits!"
	else:
		content += "\n\nHere are the home visits you recorded:\n\n"

	count = 0
	for d in hv:
		count += 1
		line = "%d) %s on %s in %s district\n"%(count, d.visited_name, str(d.visit_date),
					d.district.name)
		content += line
	
	
	if len(gi) == 0:
		content += "You have no recorded guest invites!"
	else:
		content += "\n\nHere are the guest invites you recorded:\n\n"

	count = 0
	for d in gi:
		count += 1
		line = "%d) %s on %s in %s district\n"%(count, d.friend_name, str(d.invite_date),
					d.district.name)
		content += line

	content += '\nThank You!\nonelifeatatime.in'
	send_mail(subject, content, sender, recipients)


def my_activities(request):
	context = {}
	if request.POST:
		email = request.POST['email']
		dialogues = q.get_dialogues_list_by_email(email)
		home_visits = q.get_home_visits_list_by_email(email)
		guest_invites = q.get_guest_invites_list_by_email(email)
		send_my_activities_email(email, dialogues, home_visits, guest_invites)
		context['display_message'] = 'If entered email-id was valid, you\'ll receive an email shortly!'

	return render(request, 'dialogues/my_activities.html', context)

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
	context['all_chapter_list'] = q.get_all_chapters() 
	context['daily_count_list'] = q.get_daily_count_list()
	context['district_count_list'] = q.get_district_wise_dialogues_count()
	context['district_hv_count_list'] = q.get_district_wise_hv_count()
	context['district_count_zero_list'] = q.get_district_wise_dialogues_count_zero()
	context['district_hv_count_zero_list'] = q.get_district_wise_hv_count_zero()
	context['regionwise_total_count'] = q.get_regionwise_total_count()
	return render(request, 'dialogues/leaders_dashboard.html', context)

def ajax_hv_get_district_summary(request, district_id):
	context = {}
	context['district_id'] = district_id
	context['dist'] = q.get_district_by_id(district_id)
	context['total_hv_count'] = q.get_home_visits_count_by_district_id(district_id)
	context['month_hv_count'] = q.get_this_month_home_visits_count_by_district_id(district_id)
	context['total_gi_count'] = q.get_guest_invites_count_by_district_id(district_id)
	context['month_gi_count'] = q.get_this_month_guest_invites_count_by_district_id(district_id)
	context['month_home_visit_list'] = q.get_this_month_home_visits_by_district_id(district_id)
	context['month_guest_invite_list'] = q.get_this_month_guest_invites_by_district_id(district_id)
	return render(request, 'dialogues/ajax_hv_district_summary.html', context)


def ajax_get_total_count(request):
	context = {}
	context['total_count'] = q.get_total_count()
	return render(request, 'dialogues/ajax_total_count.html', context)

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
def ajax_submit_new_guest_invite(request):
	context = {}
	if request.method == 'POST':
		dist_id = request.POST.get('district_id')
		dist = q.get_district_by_id(request.POST.get('district_id'))
		gi = GuestInvite(member_name=request.POST.get('member_name','dummy'),
			friend_name=request.POST.get('friend_name','dummy_friend'),
			member_email=request.POST.get('member_email','abc@xyz.com'),
			district=dist, invite_date= datetime.date.today(), 
			info=request.POST.get('info',''))
		
		gi.save()
	return HttpResponseRedirect('/dialogues/ajax_hv_get_district_summary/'+dist_id+'/')

@csrf_exempt
def ajax_submit_new_home_visit(request):
	context = {}
	if request.method == 'POST':
		dist_id = request.POST.get('district_id')
		dist = q.get_district_by_id(request.POST.get('district_id'))
		hv = HomeVisit(visitor_name=request.POST.get('visitor_name','dummy'),
			visited_name=request.POST.get('visited_name','dummy_friend'),
			visitor_email=request.POST.get('visitor_email','abc@xyz.com'),
			district=dist, visit_date= datetime.date.today())
		
		hv.save()
	return HttpResponseRedirect('/dialogues/ajax_hv_get_district_summary/'+dist_id+'/')


@csrf_exempt
def ajax_submit_new_dialogue(request):
	context = {}
	if request.method == 'POST':
		are_you_human_ans = request.POST.get('are_you_human')
		if are_you_human_ans.strip() != '9':
			context['submit_msg'] ='Please answer the question correctly!'
		else:
			try:
				dist = q.get_district_by_id(request.POST.get('district_select'))
				dlg = Dialogue(member_name=request.POST.get('member_name','dummy'),
					friend_name=request.POST.get('friend_name','dummy_friend'),
					member_email=request.POST.get('member_email','abc@xyz.com'),
					district=dist, dialogue_date = datetime.date.today())
				
				dlg.save()
				context['submit_msg']='Congratulations! Your dialogue is submitted'
			except:
				context['submit_msg'] ='Invalid data!'
	
	return render(request, 'dialogues/ajax_submit_new_dialogue_response.html', context)


def export_dist_sheet_dialogue_list_xls(request, dist_wise_list):
	import xlwt
	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename=dialogue_list.xls'
	wb = xlwt.Workbook(encoding='utf-8')
	for dist_data in dist_wise_list:
		ws = wb.add_sheet(dist_data['district_name'])
	
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
		for d in dist_data['dialogues']:
			row_num += 1
			row = [
				d.member_name,
				d.member_email,
				d.friend_name,
				d.district.parent.parent.parent.name,
				d.district.parent.parent.name,
				d.district.parent.name,
				d.district.name,
				str(d.dialogue_date)
			]
			for col_num in xrange(len(row)):
				ws.write(row_num, col_num, row[col_num], font_style)
				
	wb.save(response)
	return response


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
			str(d.dialogue_date)
		]
		for col_num in xrange(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)
			
	wb.save(response)
	return response


def export_entire_dialogue_list_xls(request):

	all_dialogues = q.get_all_dialogues()
	return export_dialogue_list_xls(request, all_dialogues)
 
def export_chapter_dialogue_list_date_range_xls(request):
	
	chapter_id = int(request.GET.get('chapter_id',''))
	start_date = request.GET.get('start_date','01/01/2016 0:01 AM')
	start_date = datetime.datetime.strptime(start_date, '%d-%m-%Y').strftime('%Y-%m-%d')

	end_date = request.GET.get('end_date','12/1/2016 8:08 PM')
	end_date = datetime.datetime.strptime(end_date, '%d-%m-%Y').strftime('%Y-%m-%d')
	dist_wise_list = q.get_chapter_dialogues_in_date_range(start_date, end_date, chapter_id) 

	return export_dist_sheet_dialogue_list_xls(request, dist_wise_list)

def export_dialogue_list_date_range_xls(request):
	
	start_date = request.GET.get('start_date','01/11/2015 8:01 PM')
	start_date = datetime.datetime.strptime(start_date, '%d-%m-%Y').strftime('%Y-%m-%d')

	end_date = request.GET.get('end_date','01/11/2015 8:08 PM')
	end_date = datetime.datetime.strptime(end_date, '%d-%m-%Y').strftime('%Y-%m-%d')
	dialogues = q.get_dialogues_in_date_range(start_date, end_date) 

	return export_dialogue_list_xls(request, dialogues)

