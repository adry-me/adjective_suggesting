from django.urls import path
from . import views


app_name = 'SuggestAdjectives'
urlpatterns = [
    path('', views.sample),
    path('input', views.input_contents, name='InputContents'),
    path('suggest', views.suggest, name='Suggest'),
    path('generated', views.generated, name='Generated'),
    path('select', views.select_words, name='SelectWords'),

    path('api/check/adjective-exists', views.api_check_adjectives_in_db),
    path('api/save/adjectives', views.api_save_new_words),

]