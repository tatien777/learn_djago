import json 

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.core.serializers import serialize

from api_test.mixins import JsonResponseMixin
from .models import Update
# Create your views here.
# def detail_view(request):
#     return HttpResponse(get_template().render({})) #return JSON data, XML 

# obj = Update.objects.get(id=1)

def json_example_view(request):
    '''
    URI -  -- for a TEST API
    GET -- Retrieve
    '''
    data = {
        "count": 1000,
        "content": "some new content"
    }
    json_data = json.dumps(data)
    # return JsonResponse(data) ## cach 1
    return HttpResponse(json_data,content_type="application/json") ## cach2 

class JsonCBV(View):
    def get(self,request,*arg,**kwargs):
        data = {
        "count": 1000,
        "content": "cbv1"
    }
        return JsonResponse(data) 

class JsonCBV2(JsonResponseMixin,View):
    def get(self,request,*arg,**kwargs):
        data = {
        "count": 2000,
        "content": "cbv2"
    }
        return self.render_to_json_response(data) 

class SerializedDetailView(JsonResponseMixin,View):
    def get(self,request,*arg,**kwargs):
        obj  = Update.objects.get(id=1)
    #     data = {
    #     "user": obj.user.user_name,
    #     "content": obj.content
    # }
        json_data = obj.serialize()
        return HttpResponse(json_data,content_type="application/json")

class SerializedListView(JsonResponseMixin,View):
    def get(self,request,*arg,**kwargs):
        qs  = Update.objects.all()
        # data = serialize("json",qs) # if fields is None => call all fields of data 
        # data = serialize("json",qs,fields=('user','content'))
        # print(data)
    #     data = {
    #     "user": obj.user.user_name,
    #     "content": obj.content
    # }
        # json_data = json.dump(data)
        json_data = Update.objects.get_querySet().serialize()
        return HttpResponse(json_data,content_type="application/json") 