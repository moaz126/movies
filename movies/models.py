from django.db import models

class movies(models.Model):
    movie_id = models.AutoField
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=10)
    subcategory=models.CharField(max_length=10)
    release_date=models.DateField()
    image=models.ImageField(upload_to="images",default="")

    def __str__(self):
        return self.title
