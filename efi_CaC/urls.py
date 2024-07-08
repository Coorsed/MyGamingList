"""
URL configuration for efi_CaC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from core import views as core_views
from django.conf import settings
from noticias import views as noticias_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",core_views.inicio, name="inicio"), 
    path("biblioteca/",core_views.biblioteca, name="biblioteca"), 
    path("foro/",core_views.foro, name="foro"), 
    path("noticias/",noticias_views.noticias, name="noticias"), 
    path("reviews/",core_views.reviews, name="reviews"), 
    path("biblioteca_mongus/",core_views.biblioteca_mongus, name="biblioteca-mongus"),
    path("coorsed/",core_views.coorsed, name="coorsed"),
    path("crash/",core_views.crash, name="crash"),
    path("denuncia/",core_views.denuncia, name="denuncia"),
    path("elden_ring_review/",core_views.elden_ring_review, name="elden_ring_review"),
    path("elden_ring/",core_views.elden_ring, name="elden_ring"),
    path("facebook/",core_views.facebook, name="facebook"),
    path("half/",core_views.half, name="half"),
    path("hilo_pcs/",core_views.hilo_pcs, name="hilo-pcs"),
    path("instagram/",core_views.instagram, name="instagram"),
    path("mongus/",core_views.mongus, name="mongus"),
    path("noticia1/",core_views.noticia1, name="noticia1"),
    path("noticia2/",core_views.noticia2, name="noticia2"),
    path("noticia3/",core_views.noticia3, name="noticia3"),
    path("noticia4/",core_views.noticia4, name="noticia4"),
    path("re4/",core_views.re4, name="re4"),
    path("sekiro/",core_views.sekiro, name="sekiro"),
    path("spidy/",core_views.spidy, name="spidy"),
    path("tlou/",core_views.tlou, name="tlou"),
    path("twitter/",core_views.twitter, name="twitter"),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)