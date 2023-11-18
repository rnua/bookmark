from django.contrib import admin
from .models import Bookmark

# Register your models here.

admin.site.register(Bookmark) # 모델을 관리자페이지에 등록하여 보이게 함