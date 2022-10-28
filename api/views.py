#from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['GET'])
def getData(request):
    person = {"slackUsername":"cchimdindu","backend":True,"age":22,"bio":"i am junior software developer currently taking part in zuri\'s HNG9 program"}
    return JsonResponse(person)