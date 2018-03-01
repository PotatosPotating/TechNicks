from django.db import models
import datetime

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length = 250,primary_key=True)
    contentText = models.TextField()
    author = models.CharField(max_length = 250)
    image = models.CharField(null=True,max_length = 1000)
    date = models.DateField(("Date"), default=datetime.date.today)
    edit_date = models.DateField(null=True)

    def __str__(self):
        return self.title + " by "+ self.author

class Comments(models.Model):
    blog = models.ForeignKey(BlogPost,on_delete=models.CASCADE,default='N/A')
    username = models.CharField(max_length=250)
    comment = models.TextField()
    date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.username+" : "+self.comment
