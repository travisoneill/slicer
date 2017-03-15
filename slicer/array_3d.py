def slice_2d(array_3d, axis):
    '''Returns a generator that yields all slices of array_3d along
    the specified axis. Generator yielda a series of 2D arrays'''
    generators = {
        'x': _slice_yz(array_3d),
        'y': _slice_xz(array_3d),
        'z': _slice_xy(array_3d),
    }
    return generators[axis]

def _slice_xy(array_3d):
    '''returns a generator that will yield all xy slices of array_3d'''
    return (array_2d for array_2d in array_3d)

def _slice_yz(array_3d):
    '''returns a generator that will yield all yz slices of array_3d'''
    x_range = range( len(array_3d[0][0]) )
    y_range = range( len(array_3d[0]) )
    z_range = range( len(array_3d) )
    return ( [ [array_3d[z][y][x] for y in y_range] for z in z_range ] for x in x_range )

def _slice_xz(array_3d):
    '''returns a generator that will yield all xz slices of array_3d'''
    x_range = range( len(array_3d[0][0]) )
    y_range = range( len(array_3d[0]) )
    z_range = range( len(array_3d) )
    return ( [ [array_3d[z][y][x] for z in z_range] for x in x_range ] for y in y_range )
