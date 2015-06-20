"""A module for working with ALPR.
Use lpr.get_plates(Path to image), eg: lpr.get_plates('img.jpg')
This will return a list of all plates found in the image
"""
import json
import shlex
import subprocess


def _get_process_results(command):
    """Gets a subprocess result based on the given arguments

    param  - Parameters, including program. Eg: alpr -c eu -j img.jpg
    return - [results, error]
    """
    # Generate and slpit up commands (required by subprocess)
    command_args = shlex.split(command)

    # Execute alpr and get pipe return object
    pipe = subprocess.Popen(command_args, stdout=subprocess.PIPE)

    # Communicate with pipe.
    return pipe.communicate()


def _get_json(command):
    """Get a JSON object containing the license plate results

    param  - Parameters, including program. Eg: alpr -c eu -j img.jpg
    return - JSON, or None
    """
    result, error = _get_process_results(command)
    
    # Handle potential errors
    if error is not None:
        print error
        return None
    elif 'No license plates found.' in result:
        print 'No license plates found.'
        return None
    elif not result:
        print 'Unknown error (perhaps wrong file path)!'
        return None
    
    try:
        return json.loads(result)
    except ValueError:
        print 'JSON ValueError!'
        return None


def get_plates(path, args="-c eu -j"):
    """Get a list of all the plate numbers in the given image
    
    params - Full path to file. Optionally, args= command line arguments
             Defaults args are: -c eu -j
    return - Tuple of strings representing licens plate numbers
    """
    # Make sure is working with JSON
    if args.find('-j') == -1:
        print 'Error! -j parameter necessary as this library only works\
               with JSON'
        raise ValueError
    
    # Build args and get JSON return value
    command = 'alpr ' + args + ' ' + path
    result = _get_json(command)

    # Generate a list of plates and return in
    plates = []
    for r in result['results']:
        plates.append(r['plate'])
    return plates
