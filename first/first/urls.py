from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from index.views import Display, AddPost, RemovePost, Registration, Login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Display.as_view(), name="main"),
    url('add-post/', AddPost.as_view(), name="add-post"),
    url(r'RemovePost/(?P<pk>\d+)$', RemovePost.as_view(), name="remove-post"),
    url(r'register/$', Registration.as_view(), name="registration"),
    url(r'login/$', Login.as_view(), name="login")


]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
