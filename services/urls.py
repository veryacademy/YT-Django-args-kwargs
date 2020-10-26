from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'services'

urlpatterns = [
    path('termsofuse/',
         TemplateView.as_view(template_name="services/termsofuse.html")),
    path('privicy/',
         TemplateView.as_view(template_name="services/privacy.html")),
    path('cookie/',
         TemplateView.as_view(template_name="services/cookie.html")),
    path('comments/',
         TemplateView.as_view(template_name="services/comments.html")),
    path('copyright/',
         TemplateView.as_view(template_name="services/copyright.html")),
    path('helpdesk/',
         TemplateView.as_view(template_name="services/helpdesk.html")),
]
