from django.shortcuts import render, get_object_or_404
from .models import BagList

def baglist_detail(request, baglist_id):
    baglist = get_object_or_404(BagList, id=baglist_id)
    tbaglists = baglist.tbaglists.all()  # Trae todas las sublistas
    context = {
        'baglist': baglist,
        'tbaglists': tbaglists,
    }
    return render(request, 'core/baglist_detail.html', context)
