from django.shortcuts import render_to_response
from django.template import RequestContext

from rest_framework import viewsets

from piklserver.uploader.models import Image
from piklserver.uploader.serializers import ImageSerializer
from piklserver.uploader.forms import ImageForm


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


def image(request):
    new_image = None
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = Image(file=request.FILES['file'],
                              description=request.POST['description'])
            new_image.save()
    else:
        form = ImageForm()

    return render_to_response(
        'image.html',
        {'image': new_image, 'form': form},
        context_instance=RequestContext(request)
    )
