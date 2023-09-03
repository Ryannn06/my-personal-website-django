from django.db import models
from django.db.models import Model
from django.conf import settings

from django.core.validators import FileExtensionValidator,  MinLengthValidator

from django.contrib.auth.models import AbstractUser, User


#Account Credentials Model
class account_credentials(AbstractUser):
	email = models.EmailField(unique=True)
	is_superuser = models.BooleanField(default=False)
	csv = models.FileField(upload_to='personal_files/', blank=True, null=True ,validators=[FileExtensionValidator(['pdf'])],)

	def __str__(self):
		return self.first_name +" "+ self.last_name

CATEGORIES = [
	('Major Requirement', 'Major Requirement'),
	('Minor Requirement', 'Minor Requirement'),
	('Capstone Project', 'Capstone Project'),

]

class project_collections(Model):
	title = models.CharField(unique=True, max_length=210, blank=True, null=True)
	date = models.DateField(blank=True, null=True)
	category = models.CharField(max_length=50, choices=CATEGORIES, default='Major Requirement')
	keyword = models.CharField(max_length=30, blank=True, null=True)
	keyword_description = models.TextField(blank=True, null=True, validators=[MinLengthValidator(50, 'the field must be at least 50 characters')])
	key_aspects = models.TextField(blank=True, null=True, validators=[MinLengthValidator(50, 'the field must be at least 50 characters')])
