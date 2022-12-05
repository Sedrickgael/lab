from distutils.command.upload import upload
from pydoc import describe
from django.db import models
from django.contrib.auth import get_user_model
from tinymce import HTMLField
# Create your models here.


class BaseModel(models.Model):

    # Standards
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


class Categorie(BaseModel):

    nom = models.CharField(max_length=155)
    description = models.TextField()


class Stack(BaseModel):

    nom = models.CharField(max_length=155)
    description = models.TextField()
    image = models.ImageField(upload_to='stack/images')


class Projet(BaseModel):
    nom = models.CharField(max_length=155)
    description = models.TextField()
    cat = models.ForeignKey(Categorie, related_name="projets_cat", on_delete=models.SET_NULL, null=True)
    presentation = models.FileField(upload_to='projets/documents')
    stack = models.ManyToManyField(Stack, related_name='stack_projects')
    contenu = HTMLField()
    user = models.ForeignKey(get_user_model(), related_name='projets', on_delete=models.CASCADE)


class Commentaire(BaseModel):
    critiq = models.ForeignKey('Critique', related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name='user_comments', on_delete=models.CASCADE)


class Critique(BaseModel):
    project = models.ForeignKey(Projet, related_name='critiques', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name='user_critiques', on_delete=models.CASCADE)
