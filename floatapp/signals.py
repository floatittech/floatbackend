# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from .models import Screenshot
# import blurhash

# @receiver(pre_save, sender=Screenshot)
# def Blurhash(sender, instance, *args, **kwargs):
#         if instance._state.adding:
#                 instance.blurhash = blurhash.encode(instance.screenshot, x_components=4, y_components=3)
#                 print("If hash")

