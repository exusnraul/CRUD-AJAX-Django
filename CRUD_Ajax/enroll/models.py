from django.db import models

# Create your models here.
class Studentmodel(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    desc = models.TextField()
    
    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Studentmodel_detail", kwargs={"pk": self.pk})
