from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

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
    post=models.TextField()
    author_firstname=models.CharField(max_length=30)
    author_lastname=models.CharField(max_length=30)
    topic_category=models.CharField(max_length=50,choices=CATEGORY_CHOICES, default='NEW TO TECH')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)