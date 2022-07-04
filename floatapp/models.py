from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from pathlib import Path
from django.utils.timezone import now
import uuid
from .storages import PrivateMediaStorage
# Get Year , Month Etc.
getyr = now().year
month  = now().strftime('%B')

ROLE_CHOICES = [
        ('1', 'Admin'),
        ('2', 'Cafe'),
        ('3', 'Customer')
    ]

class MyUser(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, blank=True, null=True)
    profile_pic = models.ImageField(upload_to= "media/profile_pic/",blank=True, null=True)
    mobile = models.CharField(max_length=10, unique=True, blank=True, null=True)

def file_upload_path(instance, filename):
        ext = filename.split('.')[-1]
        name = Path(filename).stem
        exclude_fields = set(('id', 'user_id'))
        #ami = UserScreenshots.objects.filter(user=instance.user).values().first()
        return f"media/{getyr}/{month}/{name}-{uuid.uuid4().hex}.{ext}"

class UserDetail(models.Model):
    id = models.UUIDField(primary_key=True, editable=True, unique=True, default=uuid.uuid4)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE, null=True)
    share = models.BooleanField(default=False)
    #workflow_id = models.UUIDField(editable=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.user)
    
    class Meta:
        ordering = ["-updated_at"]

class Screenshot(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    userdetail = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="screen_shot", null=True)
    screenshot = models.ImageField(upload_to=file_upload_path , blank=True , width_field='screenshot_width', height_field='screenshot_height')
    screenshot_width = models.IntegerField(default=1920)
    screenshot_height = models.IntegerField(default=892)
    metadata = models.JSONField(default=list)
    blurhash = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.userdetail)

    class Meta:
        ordering = ["id"]










    


