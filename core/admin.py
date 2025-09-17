from django.contrib import admin
from .models import CustomUser, BagList, tBagList, Item, tBagList_Items, Tag, BagList_Tags, Favorite
# Registro de modelos en el panel de administración de Django.
# Esto permite gestionar desde la interfaz web:
#   - Usuarios (CustomUser)
#   - BagLists y sus subcategorías (tBagList)
#   - Items y su relación con tBagLists (tBagList_Items)
#   - Etiquetas (Tag) y su relación con BagLists (BagList_Tags)
#   - Favoritos de los usuarios (Favorite)

admin.site.register(CustomUser)
admin.site.register(BagList)
admin.site.register(tBagList)
admin.site.register(Item)
admin.site.register(tBagList_Items)
admin.site.register(Tag)
admin.site.register(BagList_Tags)
admin.site.register(Favorite)
