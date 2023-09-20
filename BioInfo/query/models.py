from django.db import models

# Model fields that mimics the structure of the elastic search server in order to retrive the data. 

class GeneDiseaseAssociation(models.Model):
    geneSymbol_text = models.CharField(max_length=255, verbose_name="geneSymbol_text")
    diseaseName = models.CharField(max_length=255, verbose_name="diseaseName")
    score = models.FloatField()
