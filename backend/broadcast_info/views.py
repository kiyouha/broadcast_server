from django.shortcuts import render
from django.http import JsonResponse
from .models import BroadcastStandard

def list_broadcast_standards(request):
    standards = BroadcastStandard.objects.all()
    data = {standard.country: standard.json_data for standard in standards}
    return JsonResponse(data)

def get_broadcast_standard(request, country):
    try:
        standard = BroadcastStandard.objects.get(country=country)
        return JsonResponse(standard.json_data)
    except BroadcastStandard.DoesNotExist:
        return JsonResponse({'error': 'Country not found'}, status=404)