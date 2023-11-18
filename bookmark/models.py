from django.db import models
from django.urls import reverse # 모델에서는 reverse를 쓰고 모델 안의 필드값에서는 reverse_lazy를 쓴다

# Create your models here.

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return "이름: "+self.site_name+", 주소 : "+self.url
    
    def get_absolute_url(self):
        return reverse('detail', args=[self.id])