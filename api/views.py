from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_info(request):
    if request.method=='POST':
        json_data=request.body
        print("Received JSON data:", json_data) 
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        print("Parsed data:", parsed_data)  
        serializer=StudentSerializer(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('Data Saved')
        return HttpResponse('Error')
    
    
