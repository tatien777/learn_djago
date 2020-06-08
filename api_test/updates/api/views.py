import json
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from updates.models import Update as UpdateModel
from api_test.mixins import HttpResponseMixin
# from django.core.serializers import serialize
from .mixins import CSRFExemptMixin
## Creating, updateing,deleting, retrieving(10) == update model
class UpdateModelDetailAPIView(CSRFExemptMixin,View):
    '''
    Retrieve,Update,Delete -> object
    '''
    def get(self,request,id,*arg,**kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return  HttpResponse(json_data,content_type='application/json') #json ,xml, htm  
    def post(self,request,*args,**kwargs):
        return  HttpResponse({},content_type='application/json') #json ,xml, htm   
    def put(self,request,*arg,**kwargs):
        return  HttpResponse({},content_type='application/json') #json ,xml, htm   
    def delete(self,request,*args,**kwargs):
        return  HttpResponse({},content_type='application/json') #json ,xml, htm  



class UpdateModelListAPIView(HttpResponseMixin,CSRFExemptMixin,View):
    is_json = True
    # def render_to_response(data,status=200):
    #     return HttpResponse(data,content_type="application/content",status=status) remove
    def get(self,request,*arg,**kwargs):
        qs = UpdateModel.objects.get_querySet()
        json_data = qs.serialize()
        return  self.render_to_response(json_data)
    def post(self,request,*args,**kwargs):
        data = json.dumps({'message':"No data"})
        return  self.render_to_response(data,status=400)
    
    def delete(self,request,*args,**kwargs):
        data = json.dumps({'message':"You can not delete an entire list"})
        return  self.render_to_response(data,status=403)