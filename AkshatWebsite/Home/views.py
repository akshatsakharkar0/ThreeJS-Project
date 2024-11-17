from django.shortcuts import render
from .models import Shape
import json
# Create your views here.
def mainpage(request):
    shapes = [{"type":int(x.type), "color":x.color} for x in Shape.objects.all()]
    shape_json = json.dumps(shapes)
    context={'shapes':shape_json,}
    return render(request,'header.html',context)