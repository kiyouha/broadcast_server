from django.shortcuts import render
from django.http import JsonResponse
from .models import TunerConfig

def create_tuner_config(request):
    if request.method == 'POST':
        data = request.POST
        config = TunerConfig.objects.create(
            name=data.get('name'),
            frequency=data.get('frequency'),
            bandwidth=data.get('bandwidth'),
            modulation=data.get('modulation')
        )
        return JsonResponse({'message': 'Tuner config created', 'config': {
            'name': config.name,
            'frequency': config.frequency,
            'bandwidth': config.bandwidth,
            'modulation': config.modulation
        }})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def list_tuner_configs(request):
    configs = TunerConfig.objects.all()
    data = [{"name": config.name, "frequency": config.frequency, "bandwidth": config.bandwidth, "modulation": config.modulation} for config in configs]
    return JsonResponse(data, safe=False)
