from django.views import View
from numpy import delete
from .models import Company
from django.http import JsonResponse
from django.forms.models import model_to_dict


# Create your views here.
class SistemaListaVista(View): #Me da la lsita de los objetos en formato JSON 
    def get(self, request):
        Slist = Company.objects.all()
        return JsonResponse(list(Slist.values()), safe = False)

    def post(self,request):
        pass
    
    def put(self,request):
        pass
    
    def delete(self,request):
        pass

class SistemaDetailVista(View): #Me solicita un unico objeto  
    def get(self, request, id):
        Slist = Company.objects.get( id = id)
        return JsonResponse(model_to_dict (Slist))

    def post(self,request):
        pass
    
    def put(self,request):
        pass
    
    def delete(self,request):
        pass    