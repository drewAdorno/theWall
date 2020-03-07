from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.app1.urls')),
	url(r'^wall/', include('apps.wall.urls')),
]
