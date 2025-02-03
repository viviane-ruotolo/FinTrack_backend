from . import person
from django.db import models

class UserAdmin(person):
    function = models.CharField(max_length=255)
    permissions = models.JSONField()
    is_global_user = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #audit log

    def __str__(self):
        return f"{self.name} (Admin - {self.function})"

    def update_permissions(self, new_permissions):
        self.permissions = new_permissions
        self.save()

    #FAZER MODIFICAÇÕES COM DJANGO ADMIN
