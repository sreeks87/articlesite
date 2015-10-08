from django.db import models
from django.utils import timezone
# Create your models here.
'''
Model created for DB tble : PostArticle
Field names in table : Title,Author,Body text, publisher date,article category
hero image, additional image.
'''
class PostArticle(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=50)
	body_txt = models.TextField()
	pub_date = models.DateTimeField(blank=True, null=True)
	article_cat = models.CharField(max_length=50)
	hero_img = models.ImageField(upload_to="image")
	opt_img = models.ImageField(upload_to="image",blank=True,null=True)
	'''
	Optional Method for publishing the data to DB, it saves the data into table.
	'''
	def pub_article(self):
		self.pub_date = timezone.now()
		self.save()
	'''
	Unicode function to return proper string values to admin page
	'''
	def __str__(self):
		return self.title
