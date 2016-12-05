from django.conf.urls import url
from blog.views import name,name1

urlpatterns = [
     url(r'^name/', name),
     url(r'^name1/', name1),
]
