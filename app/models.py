from django.db import models

# Create your models here.
class Topic(models.Model):
    topicname=models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.topicname



class Webpage(models.Model):
    topicname=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()


    def __str__(self) -> str:
        return self.name



class Accessrecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()


    def __str__(self) -> str:
        return self.author
    
    

