from sys import prefix
from fastapi import FastAPI
from collections import defaultdict
from fastapi import status
from fastapi.exceptions import RequestValidationError
from public import *
from src import *


app = FastAPI(title=NAME,version=VERSION)


@app.exception_handler(RequestValidationError)
async def custom_form_validation_error(request, exc):
    reformatted_message = defaultdict(list)
    for pydantic_error in exc.errors():
        loc, msg = pydantic_error["loc"], pydantic_error["msg"]
        filtered_loc = loc[1:] if loc[0] in ("body", "query", "path") else loc
        field_string = ".".join(filtered_loc)  # nested fields with dot-notation
        reformatted_message[field_string].append(msg)
    return raise_error(False,Response.INVALID_REQUEST,reformatted_message,status.HTTP_400_BAD_REQUEST)



app.include_router(addressbook.router,prefix=Urls.ADDRESS_URL,tags=["Address Book"])

@app.get("/")
def index():
    return make_response(True,Response.WELCOME_TO_ADDRESS_BOOK,[])
