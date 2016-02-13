from dialogues.models import *
from django.db.models import Count
import datetime

def get_total_count():
    return Dialogue.objects.count()

def get_daily_count_list():
	today = datetime.date.today()
	fifteen_days_ago = today - datetime.timedelta(days=15)
	return Dialogue.objects.filter(dialogue_date__gte=fifteen_days_ago).values('dialogue_date').annotate(count=Count('dialogue_date')).order_by('count')



def get_district_wise_count():
	return Dialogue.objects.all().values('district__name').annotate(count=Count('district')).order_by('count')

def get_all_dialogues():
	return Dialogue.objects.all()

def get_chapter_total_count(chapter_id):
	chapter = Chapter.objects.get(id=chapter_id)
	districts = chapter.district_set.all()
	count = 0
	for district in districts:
		count += Dialogue.objects.filter(district=district).count()
	return count 


def get_regionwise_total_count():
	regions = Region.objects.all()
	data_list = []
	for region in regions:
		ele = {}
		ele['name'] = region.name
		region_count = 0
		for chapter in region.chapter_set.all():
			region_count += get_chapter_total_count(chapter.id)
			
		ele['region_count'] = region_count
		data_list.append(ele)
	return data_list


def get_chapter_dialogues_in_date_range(start_date, end_date, chapter_id):
	districts = Chapter.objects.get(id=chapter_id).district_set.all()
	data_list = []
	for district in districts:
		ele = {}
		ele['district_name'] = district.name
		ele['dialogues'] = Dialogue.objects.filter(district=district,
					dialogue_date__range=[start_date, end_date])
		data_list.append(ele)
	return data_list

def get_dialogues_in_date_range(start_date, end_date):
	return Dialogue.objects.filter(dialogue_date__range=[start_date, end_date])

def get_all_zones():
	return Zone.objects.all()

def get_all_chapters():
	return Chapter.objects.all().order_by('name')

def get_regions_in_zone(zone_id):
	zone = Zone.objects.get(id=zone_id)
	return zone.region_set.all()

def get_chapters_in_region(id):
	region = Region.objects.get(id=id)
	return region.chapter_set.all()

def get_districts_in_chapter(id):
	chapter = Chapter.objects.get(id=id)
	return chapter.district_set.all()

def get_district_by_id(id):
	return District.objects.get(id=id)

def get_home_visits_list_by_email(email):
	return HomeVisit.objects.filter(visitor_email=email)

def get_guest_invites_list_by_email(email):
	return GuestInvite.objects.filter(member_email=email)


def get_dialogues_list_by_email(email):
	return Dialogue.objects.filter(member_email=email)

#Home Visits 

def get_guest_invites_count_by_district_id(district_id):
	dist = District.objects.get(id=district_id)
	return GuestInvite.objects.filter(district=dist).count()

def get_home_visits_count_by_district_id(district_id):
	dist = District.objects.get(id=district_id)
	return HomeVisit.objects.filter(district=dist).count()	

def get_this_month_guest_invites_by_district_id(district_id):
	dist = District.objects.get(id=district_id)
	today = datetime.datetime.today()
	month_start = today - datetime.timedelta(days=(today.day - 1))
	return GuestInvite.objects.filter(district=dist, invite_date__gte=month_start)


def get_this_month_home_visits_by_district_id(district_id):
	dist = District.objects.get(id=district_id)
	today = datetime.datetime.today()
	month_start = today - datetime.timedelta(days=(today.day - 1))
	return HomeVisit.objects.filter(district=dist, visit_date__gte=month_start)

def get_this_month_guest_invites_count_by_district_id(district_id):
	dist = District.objects.get(id=district_id)
	today = datetime.datetime.today()
	month_start = today - datetime.timedelta(days=(today.day - 1))
	return GuestInvite.objects.filter(district=dist, invite_date__gte=month_start).count()

def get_this_month_home_visits_count_by_district_id(district_id):
	dist = District.objects.get(id=district_id)
	today = datetime.datetime.today()
	month_start = today - datetime.timedelta(days=(today.day - 1))
	return HomeVisit.objects.filter(district=dist, visit_date__gte=month_start).count()

