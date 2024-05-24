from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html



# Create your models here.
# category model
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateField(auto_now_add=True)

    def image_tag(self):
        return format_html(
            '<img src="/Media/{}" style= "width:40px;height:40px;border-radius:50%;" />'.format(self.image))

    def __str__(self):
        return self.title





# Post Model
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    add_date = models.DateField(auto_now_add=True)
    content = models.TextField(default='Default content')  # Added content field

    def __str__(self):
        return self.title