from django.db import models
from auth.models import User
import uuid

class Category(models.Model):
    class Meta:
        db_table = "CATEGORY"
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, null=False, unique=True)
    name = models.CharField(max_length=50, null=False)

class Publication(models.Model):

    class Meta:
        db_table = "PUBLICATION"

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, null=False, unique=True)
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=256)
    minOffer = models.DecimalField(max_digits=13,decimal_places=0)
    createdAt = models.DateTimeField(auto_now_add=True, null=False)
    endDate = models.DateTimeField(null=False)
    available = models.BooleanField(default=True, null=False)
    reportable = models.BooleanField(default=True, null=False)
    category = models.ForeignKey(
        Category, related_name="publications",
        on_delete= models.CASCADE
    )
    user = models.ForeignKey(
        User, related_name= "publications",
        on_delete= models.CASCADE
    )
    priority = models.BooleanField(default=False, null=False)

class Offer(models.Model):
    class Meta:
        db_table = "OFFER"
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, null=False, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=False)
    ammount = models.DecimalField(max_digits=13,decimal_places=0)
    available = models.BooleanField(default=True, null=False) 
    user = models.ForeignKey(
        User, related_name= "offers",
        on_delete= models.CASCADE
    )       
    publication = models.ForeignKey(
        Publication, related_name="offers",
        on_delete= models.CASCADE
    )

class PublicationSupport(models.Model):
    class Meta:
        db_table = "PUBLICATIONSUPPORT"
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, null=False, unique=True)
    class TypeChoices(models.TextChoices):
        IMAGE = 'IMAGE'
        VIDEO = 'VIDEO'

    type = models.CharField(
        max_length=45, 
        null=False, 
        choices=TypeChoices.choices,
        db_column="sopType"
    ) 
    data = models.FileField(upload_to= 'publications_support_data', blank=False, null=False, db_column="sopData")
    createdAt = models.DateTimeField(auto_now_add=True, null=False)
    description = models.CharField(max_length=255, null=False)

    publication = models.ForeignKey(
        Publication, related_name="supports",
        on_delete= models.CASCADE
    )
    

    
