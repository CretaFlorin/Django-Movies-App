from django.db.models import Model, CharField

# Create your models here.
class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return f'Genre with id={self.id}, name={self.name}'
