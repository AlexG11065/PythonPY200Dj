from django.urls import path
# from .views import MyFormView, TemplView
from .views import index_view

urlpatterns = [
    path('', index_view),
    # path('landing', TemplView.as_view()),
    # path('landing/', MyFormView.as_view()),
]
