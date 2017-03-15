from django.shortcuts import render

from .models import ImageSeries

import os


def image_series_list(request):
    return render(request, 'image_series_list.html', {
        'all_image_series': ImageSeries.objects.all(),
    })

def image_slice_viewer(request, uid):
    z = os.listdir('media/png/{}/xy'.format(uid))
    y = os.listdir('media/png/{}/xz'.format(uid))
    x = os.listdir('media/png/{}/yz'.format(uid))
    return render(request, 'image_slice_viewer.html', {
        'uid': uid,
        'png_files': {
            'z_axis': z,
            'y_axis': y,
            'x_axis': x,
        }
    })
