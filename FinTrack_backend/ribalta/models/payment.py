from django.db import models

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    paid_value = models.FloatField()
    payment_method = models.CharField(max_length=10, choices=[("pix", "Pix"), ("debito", "Débito"), ("credito", "Crédito"), ("money", "Dinheiro")])
    due_date = models.DateField() #Data de vencimento
    pay_date = models.DateField() #Data de pagamento
    status = models.CharField(max_length=12, choices=[("paid", "Pago"), ("is_due_date", "Vence hoje"), ("in_debt", "Atrasado")])

    def __str__(self):
        return f"Student: {self.student_id}: {self.due_date} - {self.status}"

    # CRUD Methods
    @classmethod
    def create_payment(cls, **kwargs):
        return cls.objects.create(**kwargs)

    def update_payment(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
        return self

    def delete_payment(self):
        self.is_active = False  