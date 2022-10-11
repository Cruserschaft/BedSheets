from django.shortcuts import render
from .models import *


def about_start(request):
    feature_info = FeatureInfo.objects.first()
    feature = Feature.objects.filter(access=True)
    return render(request, 'about.html',
                  context={
                      "feature_info": feature_info,
                      "feature": feature,
                  })
