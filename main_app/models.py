from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.urls import reverse

CATEGORY_CHOICES=(
    ('ADVICE & RESOURCES-GENERAL', 'ADVICE & RESOURCES-GENERAL'),
    ('ADVICE & RESOURCES-CAREER', 'ADVICE & RESOURCES-CAREER'),
    ('BIPOC IN TECH', 'BIPOC IN TECH'),
    ('CAREER CHANGER', 'CAREER CHANGER'),
    ('CAREER DEVELOPMENT', 'CAREER DEVELOPMENT'),
    ('ENTREPRENEURSHIP', 'ENTREPRENEURSHIP'),
    ('IN THE WORKPLACE', 'IN THE WORKPLACE'),
    ('Q & A', 'Q & A'),
    ('MOMMY IN TECH', 'MOMMY IN TECH'),
    ('NETWORKING', 'NETWORKING'),
    ('NEW TO TECH', 'NEW TO TECH'),
    ( 'TECH TALK', 'TECH TALK'),
)
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=500, validators=[MinLengthValidator(3, "Please create a title greater than 3 characters")])
    topic_category=models.CharField(max_length=50,choices=CATEGORY_CHOICES, default='NEW TO TECH')
    author_firstname=models.CharField(max_length=30)
    author_lastname=models.CharField(max_length=30)
    post=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' | ' + str(self.topic_category)
    
    def get_absolute_url(self):
        return reverse("blog", kwargs={"blog_id": self.id})
    
    class Meta:
        ordering=['-updated_at']