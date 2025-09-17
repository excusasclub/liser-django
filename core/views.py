from django.shortcuts import render, get_object_or_404
from .models import BagList

def baglist_detail(request, baglist_id):
    baglist = get_object_or_404(BagList, id=baglist_id)
    tbaglists = baglist.tbaglists.all()  # Sublistas de la baglist actual

    # Todas las BagLists del usuario para la sección "Mis BagLists"
    baglists = BagList.objects.filter(user=request.user)

    context = {
        'baglist': baglist,
        'tbaglists': tbaglists,
        'baglists': baglists,  # <-- Aquí
    }
    return render(request, 'core/baglist_detail.html', context)

def baglist_edition(request):
    # Todas las BagLists del usuario
    baglists = BagList.objects.filter(user=request.user)
    context = {
        'baglists': baglists,
    }
    return render(request, 'core/baglist_edition.html', context)

