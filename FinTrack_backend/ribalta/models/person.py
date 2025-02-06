from django.db import models

class Person(models.Model):

    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    cpf = models.CharField(max_length=14, unique=True)
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    address = models.TextField()
    telephone = models.CharField(max_length=15)

    #Utilizado quando é chamado printf(person) para personalizar a saída String de um objeto
    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True #Defines as abstract class, wich does not creates a db table

    # CRUD Methods
    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
        return self

    def delete(self):
        self.is_active = False

#Configurar rotas, views e serializers para testes 
#testes

#Parei no passo 5 - django rest framework