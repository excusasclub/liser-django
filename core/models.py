from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Modelo CustomUser: extiende el usuario de Django con un campo de rol
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('usuario', 'Usuario'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='usuario')

    def __str__(self):
        return self.username

# Modelo BagList: lista principal creada por un usuario
class BagList(models.Model):
    VISIBILITY_CHOICES = [
        ('private', 'Private'),
        ('public_open', 'Public Open'),
        ('public_registered', 'Public Registered'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='private')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Modelo tBagList: subcategoría dentro de una BagList
# Ahora solo es un contenedor de Items
class tBagList(models.Model):
    baglist = models.ForeignKey(BagList, on_delete=models.CASCADE, related_name='tbaglists')
    name = models.CharField(max_length=255)
    micro_description = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Modelo Item: producto del catálogo de un usuario
class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=140)
    image_url = models.URLField(blank=True)
    micro_description = models.CharField(max_length=100, blank=True)
    discount_code = models.CharField(max_length=50, blank=True)
    link_url = models.URLField(blank=True)
    video_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Tabla intermedia tBagList_Items: relación N:N entre tBagList e Items
class tBagList_Items(models.Model):
    tbaglist = models.ForeignKey(tBagList, on_delete=models.CASCADE, related_name='tbaglist_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='tbaglist_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('tbaglist', 'item')  # evita duplicados dentro de la misma tBagList

    def __str__(self):
        return f"{self.tbaglist.name} - {self.item.name}"

# Modelo Tag: etiqueta creada por un usuario
class Tag(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Tabla intermedia BagList_Tags: relación N:N entre BagList y Tags
class BagList_Tags(models.Model):
    baglist = models.ForeignKey(BagList, on_delete=models.CASCADE, related_name='baglist_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='baglist_tags')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('baglist', 'tag')

    def __str__(self):
        return f"{self.baglist.name} - {self.tag.name}"

# Modelo Favorite: permite marcar BagLists o Items como favoritos
class Favorite(models.Model):
    TARGET_CHOICES = [
        ('baglist', 'BagList'),
        ('item', 'Item'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    target_type = models.CharField(max_length=10, choices=TARGET_CHOICES)
    target_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.target_type} {self.target_id}"
