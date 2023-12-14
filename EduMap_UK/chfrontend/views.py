from django.shortcuts import render


# Create your views here.
def placesListMap(request):
    return render(request, 'chfrontend/places_base.html')
