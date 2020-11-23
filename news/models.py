from django.db import models
from profiles.models import CustomUser

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True, blank=False)
    slug = models.SlugField(max_length=100, blank=False)
    text = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    pub_date = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField('Comment',  related_name='related_xxx')
    image = ProcessedImageField(upload_to='post_images',
                                processors=[ResizeToFill(400, 300)],
                                format='JPEG',
                                options={'quality': 80})

    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(50, 50)],
                                     format='JPEG',
                                     options={'quality': 80})

    def __str__(self):
        return str(self.title)


class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)
    description = models.TextField(default='This tag has no description yet')

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='related_asd')
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author.get_full_name()}: {self.text[0:50]}'


class PostUserLike(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.user.get_full_name()} like {self.post.title}'
