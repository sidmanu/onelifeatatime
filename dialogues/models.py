from django.db import models

class Zone(models.Model):
	name = models.CharField(max_length=60, unique=True)

	def __str__(self):
		return "Zone: %s"%self.name

class Region(models.Model):
	name = models.CharField(max_length=60, unique=True)
	parent = models.ForeignKey(Zone)

	def __str__(self):
		return "Region: %s"%self.name

class Chapter(models.Model):
	name = models.CharField(max_length=60, unique=True)
	parent = models.ForeignKey(Region)

	def __str__(self):
		return "Chapter: %s"%self.name

class District(models.Model):
	name = models.CharField(max_length=60, unique=True)
	parent = models.ForeignKey(Chapter)
	
	def __str__(self):
		return "District: %s"%self.name

class Dialogue(models.Model):
	member_name = models.CharField(max_length=60)
	friend_name = models.CharField(max_length=60)
	member_email = models.CharField(max_length=60, unique=True)
	district = models.ForeignKey(District)
	dialogue_date = models.DateField()

	def __str__(self):
		return "Diag in %s district: %s spoke to %s "%(self.district.name,
				self.member_name, self.friend_name)
