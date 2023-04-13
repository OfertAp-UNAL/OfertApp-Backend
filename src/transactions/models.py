from django.db import models
from auth.models import User, Admin
from publications.models import Offer
import uuid

class Account(models.Model):
    # User account info
    class Meta:
        db_table = "ACCOUNT"
    
    id = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE,
        db_column="usrId",
        related_name="account"
    )
    balance = models.DecimalField(
        max_digits=13,
        decimal_places=0,
        null=False,
        db_column="accBalance"
    )
    frozen = models.DecimalField(
        max_digits=13,
        decimal_places=0,
        null=False,
        db_column="accFrozen"
    )

class Payment(models.Model):

    class PaymentTypeChoices(models.TextChoices):
        CREDIT_CARD = 'CC' # Credit Card
        PAY_PAL = 'PP' # PayPal
        NEQUI = 'NQ' # Nequi
        DAVIPLATA = 'DV' # Daviplata
        VIRTUAL_CURRENCY = 'VC' # Virtual Currency
    
    class PaymentFlowChoices(models.TextChoices):
        INFLOW = 'I'
        OUTFLOW = 'O'

    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        null=False,
        db_column="payId"
    )
    type = models.CharField(
        max_length=2,
        null=False,
        db_column="payType",
        choices=PaymentTypeChoices.choices
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        null=False,
        db_column="payTimestamp"
    )
    amount = models.DecimalField(
        max_digits=13,
        decimal_places=0,
        null=False,
        db_column="payAmount"
    )
    receipt = models.FileField(
        upload_to="receipts/",
        null=False,
        db_column="payReceipt"
    )
    flow = models.CharField(
        max_length=1,
        null=False,
        db_column="payFlow",
        choices=PaymentFlowChoices.choices
    )

class Transaction(models.Model):

    class TransactionTypeChoices(models.TextChoices):
        BID_PLACED = 'BP' # Bid Placed
        COST_PER_SALE = "CS" # Cost due to sale (auction)
        BID_REVOKED = "BC" # Bid Revoked (Another user placed a higher bid)
        ACCOUNT_RECHARGE = "AR" # Account recharge
        ACCOUNT_WITHDRAWAL = "AW" # Account withdrawal
        ADMIN_ADJUSTMENT = "AA" # Admin Adjustment
        OTHER = "OT" # Other
    
    class TransactionFlowChoices(models.TextChoices):
        INFLOW = 'I' # Over balance
        OUTFLOW = 'O' # Over balance
        INFREEZE = 'F'
        OUTFREEZE = 'U'
    
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        null=False,
        db_column="tranId"
    )
    type = models.CharField(
        max_length=2,
        null=False,
        db_column="tranType",
        choices=TransactionTypeChoices.choices
    )
    description = models.CharField(
        max_length=45,
        null=True,
        db_column="tranDescription",
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        null=False,
        db_column="tranTimestamp"
    )
    amount = models.DecimalField(
        max_digits=13,
        decimal_places=0,
        null=False,
        db_column="tranAmount"
    )
    prevBalance = models.DecimalField(
        max_digits=13,
        decimal_places=0,
        null=False,
        db_column="tranPrevBalance"
    )
    postBalance = models.DecimalField(
        max_digits=13,
        decimal_places=0,
        null=False,
        db_column="tranPostBalance"
    )
    prevFrozen = models.DecimalField(
        max_digits=13,
        decimal_places=0,
        null=False,
        db_column="tranPrevFrozen"
    )
    postFrozen = models.DecimalField(
        max_digits=13,
        decimal_places=0,
        null=False,
        db_column="tranPostFrozen"
    )
    flow = models.CharField(
        max_length=1,
        null=False,
        db_column="tranFlow",
        choices=TransactionFlowChoices.choices
    )
    offer = models.ForeignKey(
        Offer,
        on_delete=models.CASCADE,
        null=True,
        db_column="offId"
    )
    payment = models.ForeignKey(
        Payment,
        on_delete=models.CASCADE,
        null=True,
        db_column="payId"
    )
    admin = models.ForeignKey(
        Admin,
        on_delete=models.CASCADE,
        null=True,
        db_column="admId"
    )

