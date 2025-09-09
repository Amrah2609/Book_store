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


class AboutPage(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='about')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "About Pages"


class BookCategory(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    icon = models.ImageField(upload_to='category_icons/')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Book Categories"


class CategorySection(models.Model):
    heading = models.CharField(max_length=100, default="Book Category")
    subheading = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural = "Category Sections"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Messages"