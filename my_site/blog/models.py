from django.db import models

from django.core.validators import MinLengthValidator


################################___changes___made___121__###########################################
class Tag(models.Model):
    caption = models.CharField(max_length=20)
################################___changes___made___###########################################


################################___changes___made___120___###########################################
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


################################___changes___made___###########################################


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date= models.DateField(auto_now=True)
    slug= models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
################################___changes___made___120___###########################################
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,related_name="posts")
################################___changes___made___###########################################

################################___changes___made___121___###########################################
    tags=models.ManyToManyField(Tag)
################################___changes___made___###########################################




