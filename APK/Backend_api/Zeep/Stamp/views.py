from django.forms import model_to_dict
from django.shortcuts import render
from django.contrib.auth.models import User

from .serializers import PatternStamp_liste_serializer,PatternStamp_detail_serializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators  import api_view
from django.http import JsonResponse
from rest_framework.viewsets import ReadOnlyModelViewSet,ModelViewSet
from Stamp.models import PatternStamp,CustomUser
from django.contrib.auth.decorators import login_required

from .permissions import IsAdminAuthenticated


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()



def initioll(request):
    # Créer 5 utilisateurs fictifs
    # Création de 5 utilisateurs personnalisés fictifs
    user1 = CustomUser.objects.create_user(username='alo', email='alo@example.com', password='alice123', type='client', tel=123456789, adresse='1 rue du Paradis', nui='1234567890123', ape='1234A')

    print('ok')
    return 'ok'

def affol(request):
    users = CustomUser.objects.all() # obtenir tous les utilisateurs
    for user in users: # parcourir le QuerySet
        print(user.username) # afficher le nom d'utilisateur
        print(user.type) # afficher le type
        print(user.tel) # afficher le téléphone
        print(user.adresse) # afficher l'adresse
        print(user.nui) # afficher le nui
        print(user.ape) # afficher l'ape
    return 'good'

@api_view(['GET','POST'])
def api_view(request):
    
    users = CustomUser.objects.all() # obtenir tous les utilisateurs
    user = users[0]
    user_dic = model_to_dict(user)
    return JsonResponse(user_dic, safe=False)
    #return JsonResponse({}, safe=False)
        
        
        
@login_required        
def profile(request):
    return render(request,'Stamp/profile.html',{})


class Read_PatternStamp(ReadOnlyModelViewSet):
    serializer_class = PatternStamp_liste_serializer
    detail_serializer_class = PatternStamp_detail_serializer
    
    def get_queryset(self):
        return PatternStamp.objects.all()
    

class Admin_PatternStamp(ModelViewSet):
    
    serializer_class = PatternStamp_liste_serializer
    detail_serializer_class = PatternStamp_detail_serializer
    permission_classes = [IsAdminAuthenticated]
    
    def get_queryset(self):
        return PatternStamp.objects.all()
    
    
