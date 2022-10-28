#from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['GET'])
def getData(request):
    person = JsonResponse({"slackUsername":"cchimdindu","backend":True,"age":22,"bio":"i am junior software developer currently taking part in zuri\'s HNG9 program"})
    person["access-control-allow-origin"] = "*"
    person["access-control-allow-methods"] = "GET, OPTIONS"
    person["access-control-max-age"] = "1000"
    person["access-control-allow-headers"] = "X-Requested-With, Content-Type"
    return person