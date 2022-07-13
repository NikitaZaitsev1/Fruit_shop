from django.conf import settings
from django.db import models
from django.utils import timezone


class PostManager(models.Manager):
    def get_queryset(self):
        qs = super(PostManager, self).get_queryset()
        return qs.filter(is_published=True)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "tags"

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag, blank=True, related_name='posts')
    objects = models.Manager()
    post_manager = PostManager()

    class Meta:
        db_table = "posts"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
