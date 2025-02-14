from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def replace_intensity(source : Image, destination : Image = None, value_to_replace : float = 0, value_replacement : float = 1) -> Image:
    """Replaces a specific intensity in an image with a given new value. 
    
    Parameters
    ----------
    source : Image
    destination : Image, optional
    value_to_replace : Number, optional
    value_replacement : Number, optional
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.replace_intensity(input, destination, value_to_replace, value_replacement)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_replaceIntensity
    """


    parameters = {
        "dst": destination,
        "src":source,
        "in":float(value_to_replace),
        "out":float(value_replacement)
    }

    execute(__file__, '../clij-opencl-kernels/kernels/replace_intensity_x.cl', 'replace_intensity', destination.shape, parameters)
    return destination
