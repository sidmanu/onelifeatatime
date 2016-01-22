from dialogues.models import *

def get_total_count():
    return Dialogue.objects.count()

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


def get_dialogues_list_by_email(email):
	return Dialogue.objects.filter(member_email=email)
