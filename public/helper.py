from fastapi.responses import JSONResponse

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
