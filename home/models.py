from django.db import models

class HomePageSlider(models.Model):
    id_number = models.IntegerField(blank=True, null=True)
    title = models.CharField(blank=True, null=True, max_length=20)
    slider_1 = models.ImageField(upload_to='slider')
    slider_2 = models.ImageField(upload_to='slider')
    slider_3 = models.ImageField(upload_to='slider')

    def __str__(self):
        return self.title


class HomePageBody(models.Model):
    id_vision = models.IntegerField(blank=True, null=True)
    title = models.CharField(blank=True, null=True, max_length=20)
    body_img = models.ImageField(upload_to='home_body')
    body_text = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.title