from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
class Category(models.Model):
    name = models.CharField(max_length=255)


 
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
    
    def post_count(self):
        return Post.objects.filter(category=self).count()

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="Esnile Innova Tech Ltd")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    slug = models.SlugField()
    image = models.ImageField(null=True, blank=True, upload_to='blog_images/')
    intro = models.TextField()
    body = models.TextField()
    category = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    class Meta:
        ordering = ['date_added']
