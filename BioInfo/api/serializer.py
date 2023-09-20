from query.models import GeneDiseaseAssociation
from rest_framework import serializers


class GeneDiseaseAssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model= GeneDiseaseAssociation
        fields = ['geneSymbol_text', 'diseaseName', 'score']

