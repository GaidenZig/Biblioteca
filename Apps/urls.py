from django.conf.urls import url, include
from rest_framework import routers
from Apps.Biblioteca.quickstart import views 

router = routers.DefaultRouter()
router.register(r'editorials', views.BookViewSet)
router.register(r'genres', views.GenresViewSet)

urlpatterns=[

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]