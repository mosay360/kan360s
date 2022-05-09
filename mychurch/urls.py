"""mychurch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

#admin.site.site_header= " MOSAY360 Admin"
#admin.site.site_title = "Mosay360 Admin Portal"
#admin.site.index_title= "Welcome to 360 Enterprise"

sitemaps = {
    'posts':PostSitemap,
}


urlpatterns = [

    path("i18n/", include("django.conf.urls.i18n")),
    path('', include('amchurch.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
   name='django.contrib.sitemaps.views.sitemap'),
    
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
