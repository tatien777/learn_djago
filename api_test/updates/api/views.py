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
        """
        data = {
            "user": obj.user,
            "content": obj.content
        }"""
        data = json.loads(obj.serialize())
        passed_data = json.loads(request.body)
        for key,value in passed_data.items():
            data[key] = value
        print(passed_data)
        form = UpdateModelForm(passed_data)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data,status=201)
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
        deleted = obj.delete()
        print(deleted)
        json_data = json.dumps({"message":"successfully deleted."})
        return  self.render_to_response(json_data,status=200) 

# AUTH/ Permission --- DJANGO REST FRAMEWORK
class UpdateModelListAPIView(HttpResponseMixin,CSRFExemptMixin,View):
    '''
         LIST VIEW -> RETRIEVE 
         create view
         update
         delete
    '''
    is_json = True
    queryset = None 

    def get_querySet(self):
        qs = UpdateModel.objects.get_querySet()
        self.queryset = qs 
        return qs 

    def get_object(self,id=None):
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExist:
        #     obj = None
        """
        Below handles a does not exist Exception too 
        """
        print('id',id)
        if id is None :
            return None
        qs = self.get_querySet().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    # def render_to_response(data,status=200):
    #     return HttpResponse(data,content_type="application/content",status=status) remove
    def get(self,request,*arg,**kwargs):
        data = json.loads(request.body)
        passed_id = data.get("id",None)
        if passed_id is not None:
            obj = self.get_object(id=passed_id)
            print("obj",obj)
            if obj is None :
                error_data = json.dumps({"message":"Update Not found"})
                return self.render_to_response(error_data,status=400) 
            qs = obj
            json_data = qs.serialize()
            return  self.render_to_response(json_data)            
        else:
            qs = self.get_querySet()
            json_data = qs.serialize()
            return  self.render_to_response(json_data)
        
    def post(self,request,*args,**kwargs):
        # print(request.post)
        valid_json = is_json(request.body)
        if not valid_json:
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
    
    def put(self,request,*arg,**kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message":"Invalid data sent, please send using Json"})
            return self.render_to_response(error_data,status=400)
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message":"Update not found"})
            return self.render_to_response(error_data,status=404)
        if not is_json(request.body):
            error_data = json.dumps({"message":"Invalid data sent, please send using Json"})
            return self.render_to_response(error_data,status=400)
        """
        data = {
            "user": obj.user,
            "content": obj.content
        }"""
        data = json.loads(obj.serialize())
        passed_data = json.loads(request.body)
        passed_id  = passed_data.get('id',None)
        if not passed_id:
            error_data = json.dumps({"id":"this is a required item "})
            return self.render_to_response(error_data,status=400)
        obj = self.get_object(id=passed_id)
        for key,value in passed_data.items():
            data[key] = value
        print(passed_data)

        form = UpdateModelForm(passed_data)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data,status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data,status=400)
        data = {'message':"No allowed"}
        return  self.render_to_response(data,status=400)

    def delete(self,request,*args,**kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message":"Update not found"})
            return self.render_to_response(error_data,status=404)
        if not is_json(request.body):
            error_data = json.dumps({"message":"Invalid data sent, please send using Json"})
            return self.render_to_response(error_data,status=400)
        """
        data = {
            "user": obj.user,
            "content": obj.content
        }"""
        data = json.loads(obj.serialize())
        passed_data = json.loads(request.body)
        passed_id  = passed_data.get('id',None)
        obj = self.get_object(id=passed_id)

        if obj is None:
            error_data = json.dumps({"message":"Update not found"})
            return self.render_to_response(error_data,status=404)
        deleted = obj.delete()
        print(deleted)
        json_data = json.dumps({"message":"successfully deleted."})
        return  self.render_to_response(json_data,status=200) 
