from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import *
from django.utils.timezone import now
from django.contrib.humanize.templatetags.humanize import naturaltime


class ScreenshotSerializers(serializers.ModelSerializer):
    #userdetails = serializers.PrimaryKeyRelatedField(many=True, queryset=UserDetail.objects.all())
    screenshot = Base64ImageField()
    #metadata = serializers.JSONField()
    
    class Meta:
        model = Screenshot
        exclude = ('userdetail', )
        #depth = 1
        #fields = "__all__"
        #read_only_fields = ('id',)

class UserDetailSerializers(serializers.ModelSerializer):
    screen_shot = ScreenshotSerializers(many=True)
    id = serializers.UUIDField()
    time_since_update = serializers.SerializerMethodField()

    class Meta:
        model = UserDetail
        exclude = ('user','created_at', 'updated_at' )
        #depth = 1
        #fields = '__all__'
        read_only_fields = ('id',)

    def get_time_since_update(self, obj):
        return naturaltime(obj.updated_at)

    def create(self, validated_data):
        tracks_data = validated_data.pop('screen_shot')
        album = UserDetail.objects.create(**validated_data)
        for track_data in tracks_data:
            Screenshot.objects.create(**track_data, userdetail=album)
        return album

class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = (
            'pk',
            'first_name',
            'last_name',
            'email',
            'role',
            'mobile',
        )
        read_only_fields = ('pk', 'email',)
