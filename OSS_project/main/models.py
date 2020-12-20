from django.db import models

class Post(models.Model):
    objects = models.Manager()
    postname = models.CharField(max_length=50)
    contents = models.TextField()

    # postname이 Post object 대신 나오기
    def __str__(self):
        return self.postname