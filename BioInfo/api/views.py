
from rest_framework.decorators import api_view
from rest_framework.response import Response
from elasticsearch_dsl import Search,connections
from rest_framework_csv.renderers import CSVRenderer
from .serializer import GeneDiseaseAssociationSerializer
from rest_framework import generics


# Config of the connection the elastic search server 

connections.configure( 
    default= {
        'hosts': 'https://es.public.main.medbioinformatics.com:443',
        'http_auth': ('tech_test_user', '_dGH58-P4;a.d="'),
    },
)

#The Routes of the API
@api_view(["GET"])
def getRoutes(request):
    routes = [
            
                {"GET": "api/gda"},
                {"GET": "api/gda/csv"},
                #This route i for filtering/searching elements according to thier scores
                #Change the "score" by a floating number between 0-1
                {"GET": "api/gda/?search=socre"},
              
              ]
    return Response(routes)


# This class is for rendering the serialized data in Json format
class GeneDiseaseAssociationListView(generics.ListAPIView):
    serializer_class = GeneDiseaseAssociationSerializer
      
    def get_queryset(self):
        #  Elasticsearch query to fetch data from the index
        s = Search(index='dgnplus_gene_disease_assoc_summary_janet',using="default")
        s = s.source(['geneSymbol_text', 'diseaseName', 'score'])
        # object to apply the match filter
        score_filter = self.request.query_params.get("search")
        if score_filter:
            s = s.query('match', score=float(score_filter))
            results = list(s.execute())
            return results
        return s.scan()
    
#This class is for rendering the serialized data in CSV
class GeneDiseaseAssociationListViewCsv(generics.ListAPIView):
    serializer_class = GeneDiseaseAssociationSerializer
    renderer_classes=[CSVRenderer]
    def get_queryset(self):
        # Elasticsearch query to fetch data from the index
        s = Search(index='dgnplus_gene_disease_assoc_summary_janet',using="default")
        s = s.source(['geneSymbol_text', 'diseaseName', 'score'])

        return s.scan()
