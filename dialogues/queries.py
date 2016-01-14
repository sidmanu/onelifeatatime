from dialogues.models import *

def get_total_count():
    return Dialogue.objects.count()


def get_all_zones():
	return Zone.objects.all()

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
