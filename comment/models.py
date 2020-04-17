from django.db import models
from account.models import Account

class Comment(models.Model):
        username = models.ForeignKey(Account, on_delete=models.CASCADE)
        comment = models.TextField(max_length = 400)
        updated_at = models.DateTimeField(auto_now = True)
        created_at = models.DateTimeField(auto_now_add = True)

        class Meta:
                db_table = 'comment'
