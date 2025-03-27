from django.db.models import Model, CharField, TextField, IntegerField, DateField, ForeignKey, DO_NOTHING, DateTimeField, CASCADE

# Create your models here.
class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return f'Genre #{self.id} name={self.name}'


class Movie(Model):
    title = CharField(max_length=128)
    description = TextField()
    rating = IntegerField()
    released = DateField()
    created = DateTimeField(auto_now_add=True)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)

    def __str__(self):
        return f'Movie #{self.id} title={self.title}, rating={self.rating}, genre={self.genre.name}'