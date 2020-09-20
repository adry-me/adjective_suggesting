from django.urls import path
from . import views


app_name = 'SuggestAdjectives'
urlpatterns = [
    path('', views.sample),
    path('input', views.input_contents, name='InputContents'),
    path('suggest', views.suggest, name='Suggest'),
    path('generated', views.generated, name='Generated'),
]