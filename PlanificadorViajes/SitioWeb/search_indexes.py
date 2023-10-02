from haystack import indexes
from viajes.models import Viaje_General, Viaje_Dia

class Viaje_General_Index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    nombre = indexes.CharField(model_attr='nombreViaje')
    descripcion = indexes.CharField(model_attr='descripcion')
    calificacion = indexes.IntegerField(model_attr='calificacion')

    def get_model(self):
        return Viaje_General

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(esPrivado=False)

class Viaje_Dia_Index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    nombre = indexes.CharField(model_attr='nombreDia')
    notas = indexes.CharField(model_attr='notas')

    def get_model(self):
        return Viaje_Dia