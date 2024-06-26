# Generated by Django 4.2.7 on 2023-12-28 12:18

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encrier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('couleur', models.CharField(max_length=255)),
                ('dispo', models.BooleanField()),
                ('prix', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Monture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.IntegerField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaieAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20)),
                ('val', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatternStamp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=255)),
                ('forme', models.CharField(blank=True, max_length=255, null=True)),
                ('format', models.CharField(max_length=255)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('taille_ecritue', models.CharField(blank=True, max_length=255, null=True)),
                ('maxlines', models.IntegerField()),
                ('nom_Entreprise', models.BooleanField()),
                ('tel_Entreprise', models.BooleanField()),
                ('adresse_Entreprise', models.BooleanField()),
                ('nui_Entreprise', models.BooleanField()),
                ('ape_Entreprise', models.BooleanField()),
                ('type_Entreprise', models.BooleanField()),
                ('email_Entreprise', models.BooleanField()),
                ('logo_Entreprise', models.BooleanField()),
                ('format_dateur', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('tel', models.IntegerField()),
                ('adresse', models.CharField(blank=True, max_length=255, null=True)),
                ('nui', models.CharField(blank=True, max_length=255, null=True)),
                ('ape', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('etat', models.BooleanField()),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('val', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_PaiementAccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stamp.paieaccount')),
                ('id_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
                ('etat', models.CharField(max_length=255)),
                ('format', models.CharField(max_length=255)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ContenuStamp', models.CharField(max_length=1024)),
                ('nom_Entreprise', models.CharField(blank=True, max_length=255, null=True)),
                ('tel_Entreprise', models.IntegerField(blank=True, null=True)),
                ('adresse_Entreprise', models.CharField(blank=True, max_length=255, null=True)),
                ('nui_Entreprise', models.CharField(blank=True, max_length=255, null=True)),
                ('ape_Entreprise', models.CharField(blank=True, max_length=255, null=True)),
                ('type_Entreprise', models.CharField(blank=True, max_length=255, null=True)),
                ('email_Entreprise', models.EmailField(blank=True, max_length=255, null=True)),
                ('logo_Entreprise', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('quantité', models.IntegerField()),
                ('cout', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dateliv', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_Encrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stamp.encrier')),
                ('id_Monture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stamp.monture')),
                ('id_Paiement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stamp.paiement')),
                ('id_PatternStamp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stamp.patternstamp')),
                ('id_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
