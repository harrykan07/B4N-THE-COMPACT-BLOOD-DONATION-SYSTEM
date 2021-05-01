from django.db import models

class ContactPageBody(models.Model):
    id_contact = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    contact_text = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.title
