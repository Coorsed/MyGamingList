from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "core/inicio.html")

def biblioteca(request):
    return render(request, "core/biblioteca.html")

def foro(request):
    return render(request, "core/foro.html")

def reviews(request):
    return render(request, "core/reviews.html")

def biblioteca_mongus(request):
    return render(request, "core/Biblioteca-Mongus.html")

def coorsed(request):
    return render(request, "core/Coorsed.html")

def crash(request):
    return render(request, "core/crash.html")

def denuncia(request):
    return render(request, "core/Denuncia.html")

def elden_ring_review(request):
    return render(request, "core/elden-ring_review.html")

def elden_ring(request):
    return render(request, "core/elden-ring.html")

def facebook(request):
    return render(request, "core/Facebook.html")

def half(request):
    return render(request, "core/half.html")

def hilo_pcs(request):
    return render(request, "core/Hilo-pcs.html")

def instagram(request):
    return render(request, "core/instagram.html")

def mongus(request):
    return render(request, "core/Mongus.html")

def noticia1(request):
    return render(request, "core/Noticia1.html")

def noticia2(request):
    return render(request, "core/Noticia2.html")

def noticia3(request):
    return render(request, "core/Noticia3.html")

def noticia4(request):
    return render(request, "core/Noticia4.html")

def re4_review(request):
    return render(request, "core/re4_review.html")

def re4(request):
    return render(request, "core/re4.html")

def sekiro(request):
    return render(request, "core/sekiro.html")

def spidy(request):
    return render(request, "core/spidy.html")

def tlou(request):
    return render(request, "core/tlou.html")

def twitter(request):
    return render(request, "core/twitter.html")