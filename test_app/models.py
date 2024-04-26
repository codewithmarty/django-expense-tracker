from django.db import models

# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=255)  # Expense name
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount in dollars
    date = models.DateField()  # Date of the expense
    description = models.TextField(blank=True, null=True)  # Optional description

    # To define human-readable representation of the object
    def __str__(self):
        return f"{self.name} - ${self.amount:.2f} on {self.date}"