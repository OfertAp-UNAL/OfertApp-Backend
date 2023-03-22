# Generated by Django 3.2.16 on 2023-03-22 00:47

import django.contrib.auth.models
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
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.IntegerField(db_column='usrId', primary_key=True, serialize=False, unique=True)),
                ('firstName', models.CharField(db_column='usrFirstName', max_length=45)),
                ('lastName', models.CharField(db_column='usrLastName', max_length=45)),
                ('username', models.CharField(db_column='usrUsername', max_length=45, unique=True)),
                ('email', models.EmailField(db_column='usrEmail', max_length=45, unique=True)),
                ('password', models.CharField(db_column='usrPassword', max_length=256)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='usrCreatedAt')),
                ('birthdate', models.DateField(db_column='usrBirthdate')),
                ('idenIdType', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extranjería'), ('TI', 'Tarjeta de identidad'), ('PP', 'Pasaporte'), ('NIT', 'Número de identificación tributaria')], db_column='usrIdType', default='CC', max_length=3)),
                ('phone', models.CharField(db_column='usrPhone', max_length=20)),
                ('address', models.CharField(db_column='usrAddress', max_length=100)),
                ('townId', models.DecimalField(db_column='usrTownId', decimal_places=4, max_digits=9)),
                ('profilePicture', models.ImageField(blank=True, db_column='usrProfilePicture', null=True, upload_to='profile_pictures')),
                ('blocked', models.BooleanField(db_column='usrBlocked', default=False)),
                ('verified', models.BooleanField(db_column='usrVerified', default=False)),
                ('accountType', models.CharField(choices=[('PP', 'PayPal'), ('EF', 'Efecty'), ('NQ', 'Nequi'), ('CD', 'Credit Card')], db_column='usrAccountType', default='PP', max_length=2)),
                ('accountId', models.CharField(db_column='usrAccountId', max_length=45)),
                ('vipState', models.BooleanField(db_column='usrVipState', default=False)),
                ('vipPubCount', models.IntegerField(db_column='usrVipPubCount', default=0)),
                ('reputation', models.FloatField(db_column='usrReputation', default=1.0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'USER',
                'unique_together': {('accountType', 'accountId')},
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('hiredDate', models.DateField(db_column='admHiredDate')),
                ('user', models.OneToOneField(db_column='admUsrId', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='admin', serialize=False, to='users_auth.user')),
            ],
            options={
                'db_table': 'ADMIN',
            },
        ),
    ]
