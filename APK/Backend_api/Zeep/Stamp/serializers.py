from .models import PatternStamp,Monture
from rest_framework import serializers  


from django.core.files import File #pour l'ouverture d'une image
import base64 #pour transformer une image en JSON

class Serialazer_Mixin:
    
    image = serializers.SerializerMethodField()
    def get_image(self, obj):
        f = open(obj.image_example.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        f.close()
        return data
    
class PatternStamp_liste_serializer(Serialazer_Mixin,serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = PatternStamp
        fields = ['id','titre','prix','image','forme','image_example']
        
class PatternStamp_detail_serializer(Serialazer_Mixin,serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = PatternStamp
        fields = ['id','titre','prix','image','forme']
    
    
class Monture_liste_serializer(Serialazer_Mixin,serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Monture
        fields = ['id','name','prix','image','forme','image_example','type']
        
class Monture_detail_serializer(Serialazer_Mixin,serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = PatternStamp
        fields = ['id','name ','prix','image','forme','type']
    