from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=50)
    weakTo = models.ManyToManyField('self', symmetrical=False, related_name='weak_against', blank=True)
    strongTo = models.ManyToManyField('self', symmetrical=False, related_name='strong_against', blank=True)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    types = models.ManyToManyField(Type)
    image = models.ImageField(upload_to='pokemon_images/', blank=True, null=True)  # ✅ nouveau champ

    def __str__(self):
        return self.name
