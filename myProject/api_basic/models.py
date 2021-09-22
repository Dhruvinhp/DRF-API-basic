from django.db import models
from django.utils import timezone
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
# from pygments import highlight

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='article', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)

