import os
import png
import dicom
import matplotlib
import threading

matplotlib.use('TkAgg')
import matplotlib.pylab as pylab

from slicer.array_3d import slice_2d

def png_from_voxel(voxel, path_to_directory):
    '''Slices voxel along all axes and saves slices as PNG's to the specified
    directory.  Voxel is a 3d array.  Creates nested directories from
    path_to_directory if they do not exist already'''
    _make_directory(path_to_directory + '/xy')
    _make_directory(path_to_directory + '/xz')
    _make_directory(path_to_directory + '/yz')
    for idx, xy_slice in enumerate(slice_2d(voxel, 'z')):
        # png_from_array(xy_slice, path_to_directory + '/xy', _make_filename(6, idx))
        threading.Thread(None, png_from_array, None, (xy_slice, path_to_directory + '/xy', _make_filename(6, idx)) ).run()
    for idx, xz_slice in enumerate(slice_2d(voxel, 'y')):
        # png_from_array(xz_slice, path_to_directory + '/xz', _make_filename(6, idx))
        threading.Thread(None, png_from_array, None, (xz_slice, path_to_directory + '/xz', _make_filename(6, idx)) ).run()
    for idx, yz_slice in enumerate(slice_2d(voxel, 'x')):
        # png_from_array(yz_slice, path_to_directory + '/yz', _make_filename(6, idx))
        threading.Thread(None, png_from_array, None, (yz_slice, path_to_directory + '/yz', _make_filename(6, idx)) ).run()

# def _worker(voxel, path_to_directory):
#     png_from_array


def png_from_array(array_slice, path_to_directory, name):
    '''Takes 2D array and saves it at the specified path with the specified name'''
    png = pylab.imshow(array_slice, cmap=pylab.cm.bone)
    png.write_png('./{}/{}.png'.format(path_to_directory, name))

def _make_directory(path_to_directory):
    '''Makes directory at specified path.  Nests down creating directories
    if they do not exist yet'''
    path = path_to_directory.split('/')
    for idx in range(1, len(path) + 1):
        os.system( 'mkdir {}'.format('/'.join(path[:idx])) )

def _make_filename(filename_length, idx):
    '''Returns filename with the specifed length by adding leading zeroes'''
    leading_zeroes = (filename_length - len(str(idx))) * '0'
    return leading_zeroes + str(idx)


#NOT USED
# def convert_dicom_to_png(dicom_files):
#     '''Takes list of dicom files and returns list of png_files'''
#     png_files = []
#     for dcm in dicom_files:
#         png = pylab.imshow(dcm.pixel_array, cmap=pylab.cm.bone)
#         png_files.append({'data': png, 'idx': str(dcm.InstanceNumber)})
#     return png_files
#
# def save_png_files(png_files, path_to_directory):
#'''saves array of png_file objects at the specified location'''
#     _make_directory(path_to_directory)
#     for png in png_files:
#         name = _make_filename(6, png['idx'])
#         png['data'].write_png('./{}/{}.png'.format(path_to_directory, name))
