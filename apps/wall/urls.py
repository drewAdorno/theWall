from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^post$', views.post_message),
    url(r'^post_comment/(?P<message_id>\d+)$', views.post_comment),
]