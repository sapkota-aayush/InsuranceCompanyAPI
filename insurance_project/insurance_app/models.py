from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Policy(models.Model):
    POLICY_TYPE_CHOICES = [
        ('LIFE', 'Life Insurance'),
        ('AUTO', 'Auto Insurance'),
        ('HOME', 'Home Insurance'),
    ]
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='policies')
    policy_type = models.CharField(max_length=10, choices=POLICY_TYPE_CHOICES)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    coverage_amount = models.DecimalField(max_digits=15, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.policy_type} - {self.customer.first_name}"
