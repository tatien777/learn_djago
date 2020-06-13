import json
from django.views.generic import View
from django.http import JsonResponse, HttpResponse


from api_test.mixins import HttpResponseMixin
# from django.core.serializers import serialize
from .mixins import CSRFExemptMixin
## Creating, updateing,deleting, retrieving(10) == update model
from updates.models import Update as UpdateModel
from updates.forms import UpdateModelForm

from .utils import  is_json
class UpdateModelDetailAPIView(HttpResponseMixin,CSRFExemptMixin,View):
    '''
    Retrieve,Update,Delete -> object
    '''
    is_json = True

    def get_object(self,id=None):
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExist:
        #     obj = None
        """
        Below handles a does not exist Exception too 
        """
        qs = UpdateModel.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self,request,id,*arg,**kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message":"Update not found"})
            return self.render_to_response(error_data,status=404)
        json_data = obj.serialize()
        return  self.render_to_response(json_data,status=200) #json ,xml, htm  

    def post(self,request,id,*args,**kwargs):
        json_data = json.dumps({"message": "Not allowed"})
        return  self.render_to_response(json_data,status=403)

    def put(self,request,id,*arg,**kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message":"Update not found"})
            return self.render_to_response(error_data,status=404)
        if not is_json(request.body):
            error_data = json.dumps({"message":"Invalid data sent, please send using Json"})
            return self.render_to_response(error_data,status=400)
        update_data = json.loads(request.body)
        form = UpdateModelForm(update_data)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.serialize()
            return self.render_to_response(obj,status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data,status=400)
        data = {'message':"No allowed"}
        return  self.render_to_response(data,status=400)

    def delete(self,request,id,*args,**kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message":"Update not found"})
            return self.render_to_response(error_data,status=404)
        json_data = json.dumps({'message':"Something delete"})
        return  self.render_to_response(json_data,status=200) 



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
        if not is_json(request.body):
            error_data = json.dumps({"message":"Invalid data sent, please send using Json"})
            return self.render_to_response(error_data,status=400)
        data = json.loads(request.body)
        form = UpdateModelForm(data)
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