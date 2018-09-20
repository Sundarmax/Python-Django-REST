from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from myapp import views
from myapp import api
from blog import api as blog_api
from blog import views as blog_view
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'post', api.PostViewSet)
router.register(r'article',blog_api.ArticleViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]