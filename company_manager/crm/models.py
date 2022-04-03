from django.db import models
from django.contrib.auth.models import User as User


class Address(models.Model):
    street = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'addresses'

    def __str__(self):
        return f'{self.street}, {self.zip_code} {self.city}'


class CompanyStatusType(models.TextChoices):
    N = "New"
    L = "Lead"
    O = "Opportunity"
    C = "Active Customer"
    FC = "Former Customer"
    I = "Inactive"


class Company(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=CompanyStatusType.choices, default="New")
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    identification_number = models.CharField(max_length=100)
    address = models.ForeignKey("Address", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


class Contact(models.Model):
    primary_company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Opportunity(models.Model):
    status_choices = (
        ("1", "Prospecting"),
        ("2", "Analysis"),
        ("3", "Proposal"),
        ("4", "Negotiation"),
        ("5", "Closed Won"),
        ("0", "Closed Lost")
    )

    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    sales_manager = models.ForeignKey(User, on_delete=models.RESTRICT)
    primary_contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=2, default="1", choices=status_choices)
    value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'opportunities'

    def __str__(self):
        return f'{self.company} {self.description}'[:20] + '...'
