from django.shortcuts import render_to_response
from django.template import RequestContext

from uploader.models import Image
from uploader.forms import ImageForm

import uuid


def image(request):
    def get_uuid_file_name(filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return filename

    new_image = None
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            original_filename = request.FILES['file'].name
            new_image = Image(file=request.FILES['file'],
                              name=original_filename,
                              description=request.POST['description'])
            new_image.file.name = get_uuid_file_name(original_filename)
            new_image.save()
    else:
        form = ImageForm()

    return render_to_response(
        'image.html',
        {'image': new_image, 'form': form},
        context_instance=RequestContext(request)
    )
