
from django.shortcuts import render, redirect, get_object_or_404
from .models import Property
from django.db.models import Q

def home(request):
    all_properties = Property.objects.all()
    properties = {
        'all_houses_count' : all_properties.count(),
        'all_properties' : all_properties[:3]

    }
    return render(request, 'core/home.html', {'properties':properties})
def properties(request):
    
    price_search_param = request.GET.get('price')
    availability_search_param = request.GET.get('status')
    text_search_param = request.GET.get('search', '').strip()
    

    filters = Q()

    try:
        price = int(price_search_param)
    except (ValueError, TypeError):
        price = None

    if price is not None:
        filters &= Q(price__lte=int(price_search_param))
    if availability_search_param:
        filters &= Q(status=availability_search_param)
    if text_search_param:
        filters &= Q(title__icontains=text_search_param) | Q(description=text_search_param)

    Properties = Property.objects.filter(filters)

    return render(request, 'core/all_properties.html', {'Properties':Properties})

def properties_detail(request, slug):
    property = get_object_or_404(Property, slug=slug)
    return render(request, 'core/properties_detail.html', {'property':property})


def contact_us(request):
    return render(request, 'core/contact.html', {})