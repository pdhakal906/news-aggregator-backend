from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=2048)
    image_url = models.URLField(max_length=2048, blank=True, null=True)
    source = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "News"
        verbose_name_plural = "News Items"

    def __str__(self):
        return self.title
