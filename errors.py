# Error handling

class ExceededRequestError(Exception):
    "Could not reach 42matters. The request exceeds what is allowed by the current subscription plan."
    pass

class AccessTokenError(Exception):
    "Could not reach 42Matters. The access token is not valid."
    pass

class RequestRateError(Exception):
    "Could not reach 42Matters. The request rate is over the limit."
    pass

class SecureChannelError(Exception):
    "Could not reach 42Matters. Port 443 could not be accessed."
    pass

class ServerError(Exception):
    "Server Error."
    pass

class RequestNotValid(Exception):
    "Request to 42Matters not valid. Some parameters were rejected by the API."