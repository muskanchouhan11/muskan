from django.db import models

class Hrproject(models.Model):

    fullname = models.CharField(max_length=122)
    number =  models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    skills= models.CharField(max_length=122)
    img=models.ImageField(upload_to="profile_pics" ,default="front.jpg")
    verified = models.CharField(max_length=122,null=True)
    class Meta():
        db_table="home_hrproject"
         
    def __str__(self):
        return self.fullname

    



