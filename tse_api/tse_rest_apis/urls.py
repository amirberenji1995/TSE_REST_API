from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tse_rest_apis import views

urlpatterns = [
    path('symbols/', views.SymbolsList.as_view()),
    path('symbols/<str:pk>/', views.SymbolDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
