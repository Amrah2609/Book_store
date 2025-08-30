from django.db import models

# Create your models here.


class IndexPage(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Home Pages"
