from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views as recipe_views

router = DefaultRouter()
router.register('tags', recipe_views.TagViewSet)
router.register('ingredients', recipe_views.IngrdientViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
