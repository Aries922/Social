from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from home import views
from sample1 import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('picbio/picbioe/',views.picbioe,name="picbioe"),
    path('postimage',views.postimage,name="postimage"),
    path('',views.home,name="home"),
    path('accounts/profile/',TemplateView.as_view(template_name="profile.html")),
    path('picbio/',TemplateView.as_view(template_name="picbio.html")),

]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)