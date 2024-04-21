from django.db import models
from django.contrib.auth.models import AbstractUser


class Brou(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)
    val = models.IntegerField()

class CustomUser(AbstractUser):
    type = models.CharField(max_length=255)
    tel = models.IntegerField(null=True, blank=True)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    nui = models.CharField(max_length=255, null=True, blank=True)
    ape = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)


class PaieAccount(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    val = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Paiement(models.Model):
    id = models.AutoField(primary_key=True)
    id_PaiementAccount = models.ForeignKey(PaieAccount, on_delete=models.CASCADE)
    id_User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    etat = models.BooleanField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    val = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Monture(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Encrier(models.Model):
    id = models.AutoField(primary_key=True)
    couleur = models.CharField(max_length=255)
    dispo = models.BooleanField()
    prix = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PatternStamp(models.Model):
    ROND= 'ROND'
    CARRE = "CARRE"
    FORME_CHOICES = (
        
        (ROND,'Rond'),
        (CARRE,'Carré')
    )
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=255)
    forme = models.CharField(max_length=255,choices=FORME_CHOICES, null=True, blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_example = models.ImageField(upload_to='MEDIA/image_example/PatternStamp',blank=False,null=False)
"""
        un model de backup pour les PatternStamp supprimés
        NB: l'opperation est effectuée dans un signal sur la fonction 
        patternStamp_back_up() du fichier signals.py
        
        
"""

class Commande(models.Model):
    id = models.AutoField(primary_key=True)
    id_User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id_Monture = models.ForeignKey(Monture, on_delete=models.CASCADE)
    id_Paiement = models.ForeignKey(Paiement, on_delete=models.CASCADE)
    id_Encrier = models.ForeignKey(Encrier, on_delete=models.CASCADE)
    id_PatternStamp = models.ForeignKey(PatternStamp, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    etat = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    ContenuStamp = models.CharField(max_length=1024)
    nom_Entreprise = models.CharField(max_length=255, null=True, blank=True)
    tel_Entreprise = models.IntegerField(null=True, blank=True)
    adresse_Entreprise = models.CharField(max_length=255, null=True, blank=True)
    nui_Entreprise = models.CharField(max_length=255, null=True, blank=True)
    ape_Entreprise = models.CharField(max_length=255, null=True, blank=True)
    type_Entreprise = models.CharField(max_length=255, null=True, blank=True)
    email_Entreprise = models.EmailField(max_length=255, null=True, blank=True)
    logo_Entreprise = models.ImageField(upload_to='logos/', null=True, blank=True)
    quantité = models.IntegerField()
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    dateliv = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
