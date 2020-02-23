from django.db import models
# from django.conf.auth.models import User
# from django.conf import settings          이부분 오류
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)
    body = RichTextUploadingField()
    # tags = models.CharField(max_length=100, blank=True)

