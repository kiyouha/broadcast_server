from django.shortcuts import render
from django.http import JsonResponse
from .models import StreamInfo
from .tasks import process_file

def list_streams(request):
    streams = StreamInfo.objects.all()
    data = [{"name": stream.name, "hls_url": stream.hls_url, "created_at": stream.created_at} for stream in streams]
    return JsonResponse(data, safe=False)

def upload_stream(request):
    if request.method == 'POST':
        file = request.FILES['file']
        name = file.name
        stream = StreamInfo.objects.create(name=name)
        process_file(stream.id)
        return JsonResponse({'message': 'File uploaded and processing started'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)