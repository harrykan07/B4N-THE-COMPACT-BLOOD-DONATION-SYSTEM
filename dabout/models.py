from django.db import models

class AboutPageBody(models.Model):
    id_about = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    about_text = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.title
