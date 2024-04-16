from django.db import models
from django.contrib.auth.models import AbstractUser


class Brou(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)
    val = models.IntegerField()

class CustomUser(AbstractUser):
    type = models.CharField(max_length=255)
    tel = models.IntegerField()
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
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=255)
    forme = models.CharField(max_length=255, null=True, blank=True)
    format = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    taille_ecritue = models.CharField(max_length=255, null=True, blank=True)
    maxlines = models.IntegerField()
    nom_Entreprise = models.BooleanField()
    tel_Entreprise = models.BooleanField()
    adresse_Entreprise = models.BooleanField()
    nui_Entreprise = models.BooleanField()
    ape_Entreprise = models.BooleanField()
    type_Entreprise = models.BooleanField()
    email_Entreprise = models.BooleanField()
    logo_Entreprise = models.BooleanField()
    format_dateur = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
