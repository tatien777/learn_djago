import json
from django.views.generic import View
from django.http import JsonResponse, HttpResponse


from api_test.mixins import HttpResponseMixin
# from django.core.serializers import serialize
from .mixins import CSRFExemptMixin
## Creating, updateing,deleting, retrieving(10) == update model
from updates.models import Update as UpdateModel
from updates.forms import UpdateModelForm


class UpdateModelDetailAPIView(HttpResponseMixin,CSRFExemptMixin,View):
    '''
    Retrieve,Update,Delete -> object
    '''
    is_json = True
    def get(self,request,id,*arg,**kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return  self.render_to_response(json_data,status=200) #json ,xml, htm  
    def post(self,request,*args,**kwargs):
        json_data = json.dumps({"message": "Not allowed"})
        return  self.render_to_response(json_data,status=403)   
    def put(self,request,*arg,**kwargs):
        json_data = {}
        return  self.render_to_response(json_data,status=403)   
    def delete(self,request,*args,**kwargs):
        json_data = {}
        return  self.render_to_response(json_data,status=403)   



class UpdateModelListAPIView(HttpResponseMixin,CSRFExemptMixin,View):
    is_json = True
    # def render_to_response(data,status=200):
    #     return HttpResponse(data,content_type="application/content",status=status) remove
    def get(self,request,*arg,**kwargs):
        qs = UpdateModel.objects.get_querySet()
        json_data = qs.serialize()
        return  self.render_to_response(json_data)
    def post(self,request,*args,**kwargs):
        # print(request.post)
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.serialize()
            return self.render_to_response(obj,status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data,status=400)
        data = {'message':"No allowed"}
        return  self.render_to_response(data,status=400)
    
    def delete(self,request,*args,**kwargs):
        data = json.dumps({'message':"You can not delete an entire list"})
        return  self.render_to_response(data,status=403)