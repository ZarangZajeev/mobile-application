from django.shortcuts import render
from rest_framework.views import APIView, Response


class MobileListCreateView(APIView):
    def get(self,request,*args,**kwargs):
        return Response(data={"message":"Listing all mobiles"})
    
    def post(self,request,*args,**kwargs):
        return Response(data={"message":"creating mobiles"})