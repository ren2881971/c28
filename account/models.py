from django.db import models
class Account(models.Model):
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    status = models.IntegerField(max_length=2, default=0)
    photo = models.CharField(max_length=500)
    birthday = models.DateTimeField()
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.email
    class Meta:
        db_table = 'account'
