from .models import PatternStamp
from rest_framework import serializers  


from django.core.files import File #pour l'ouverture d'une image
import base64 #pour transformer une image en JSON


class PatternStamp_liste_serializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = PatternStamp
        fields = ['id','titre','prix','image','forme','image_example']
        
    def get_image(self, obj):
        f = open(obj.image_example.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        f.close()
        return data
    
class PatternStamp_detail_serializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = PatternStamp
        fields = ['id','titre','prix','image','forme']
        
    def get_image(self, obj):
        f = open(obj.image_example.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        f.close()
        return data
    
    