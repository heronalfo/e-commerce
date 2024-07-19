from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

class BaseModelViewSet(ModelViewSet):
    parser_classes = [JSONParser,  XMLParser]
    renderer_classes = [JSONRenderer, XMLRenderer]
    
    def get_object(self):
        '''
        Get the object (user) and apply the appropriate permissions        
        :returns: 

         User.objects whether the object was found
         404 Not found if the object was not found         
        '''
        obj = get_object_or_404(self.get_queryset(), id=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)

        return obj
