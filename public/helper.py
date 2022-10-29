from fastapi.responses import JSONResponse
from math import sin, cos, sqrt, atan2, radians

def make_response(status,message,payload):
    response = {
        'status': status,
        'message': message,
        'payload': payload
    }
    return response

def failed_response():
    return JSONResponse(
    status_code=400,
        content={
            'status': False,
            'message': "Something Went Wrong, Please Try Again Later",
            'error': []
        }
    )

def raise_error(status, message, payload, error_code):
    return JSONResponse(
        status_code=error_code,
        content={
            'status': status,
            'message': message,
            'error': payload
        }
    )


def check_spacial_distance(lat1,lon1, lat2, lon2):
    R = 6373.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    distance = distance * 1000
    return distance