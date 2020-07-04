from django.db import models
from django.utils import timezone

class Article(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    text = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    draft = models.BooleanField(default=False)
    url = models.SlugField(max_length=102)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'