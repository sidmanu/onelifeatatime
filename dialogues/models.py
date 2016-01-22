from django.core.validators import RegexValidator
from django.db import models

class Leader(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=60, unique=True)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone = models.CharField(validators=[phone_regex], max_length=15, blank=True) 

	def __str__(self):
		return "Leader: %s "%(self.name)

class Zone(models.Model):
	name = models.CharField(max_length=60, unique=True)
	leader = models.ForeignKey(Leader, null=True)

	def __str__(self):
		return "Zone: %s"%self.name

class Region(models.Model):
	name = models.CharField(max_length=60, unique=True)
	parent = models.ForeignKey(Zone)
	leader = models.ForeignKey(Leader, null=True)

	def __str__(self):
		return "Region: %s"%self.name

class Chapter(models.Model):
	name = models.CharField(max_length=60, unique=True)
	parent = models.ForeignKey(Region)
	leader = models.ForeignKey(Leader, null=True)

	def __str__(self):
		return "Chapter: %s"%self.name

class District(models.Model):
	name = models.CharField(max_length=60, unique=True)
	parent = models.ForeignKey(Chapter)
	leader = models.ForeignKey(Leader, null=True)
	
	def __str__(self):
		return "District: %s"%self.name

class Dialogue(models.Model):
	member_name = models.CharField(max_length=60)
	friend_name = models.CharField(max_length=60)
	member_email = models.CharField(max_length=60)
	district = models.ForeignKey(District)
	dialogue_date = models.DateField()

	def __str__(self):
		return "Diag in %s district: %s spoke to %s "%(self.district.name,
				self.member_name, self.friend_name)
