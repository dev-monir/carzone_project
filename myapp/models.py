from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blogs/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.title
