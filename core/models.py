from django.db import models

# MODELOS

class Tipo_Bicicleta(models.Model):
    id_tipo_bicicleta = models.IntegerField(primary_key=True)
    descripcion_bicicleta = models.CharField(max_length=30)

    def __str__(self):
        return self.descripcion_bicicleta

class Marca_Bicicleta(models.Model):
    id_marca = models.IntegerField(primary_key=True)
    nombre_marca = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_marca

class Bicicleta(models.Model):
    id_bicicleta = models.IntegerField(primary_key=True)
    modelo = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    aro = models.IntegerField()
    nro_cambios = models.IntegerField()
    tipo_bicicleta = models.ForeignKey(Tipo_Bicicleta, on_delete=models.PROTECT)
    marca_bicicleta = models.ForeignKey(Marca_Bicicleta, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="bicicletas", null=True)

    def __str__(self):
        return self.modelo

class Arriendo(models.Model):
    id_arriendo = models.AutoField(primary_key=True)
    bicicleta = models.ForeignKey(Bicicleta,on_delete=models.PROTECT)
    stock = models.IntegerField(null=True)
    precio_dia = models.IntegerField()
    

    def __str__(self):
        return self.bicicleta.modelo
