from django.shortcuts import render
from .models import *
from about.models import *


def start_home(request):
    banner = Banner.objects.filter(access=True).values('title', 'about', 'image', 'button')
    feature_info = FeatureInfo.objects.first()
    feature = Feature.objects.filter(access=True)
    return render(request, "home.html",
                  context={
                      'banner': banner,
                      "feature_info": feature_info,
                      "feature": feature,
                  })
