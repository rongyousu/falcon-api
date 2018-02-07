import uuid
import falcon
import hashlib


from src.systemlog import accesslog

def token_is_valid(token, user_id):
    result = False
    
    list_key = ['8230a87c338dbe7bcebd947214c5a83e']
    key = str(token)+str(user_id)
    psw = check(key)
    if psw in list_key:
           result = True

    return result  # Suuuuuure it's valid...
 
def check(key):
    m = hashlib.md5()
    m.update(key)
    psw = m.hexdigest()
    return psw
 
def auth(req, resp, accesslogger):
    # Alternatively, use Talons or do this in WSGI middleware...
    token = req.get_param('appid') 
    apikey = req.get_param('appkey')    

    
    if token is None or apikey is None:
        description = ('Please provide an auth token  and  apikey '
                       'as part of the request.')

        
        #accesslogger.logger.error('please provide an auth token and apikey as part of the request:  ')
        raise falcon.HTTPUnauthorized('Auth token required',
                                      description,
                                      href='http://docs.example.com/auth')
 
    if not token_is_valid(token, apikey):
        description = ('The provided auth token is not valid. '
                       'Please request a new token and try again.')
 
        raise falcon.HTTPUnauthorized('Authentication required',
                                      description,
                                      href='http://docs.example.com/auth')


class AuthMiddleware(object):
    
    def __init__(self):
        self.accesslogger=accesslog.AccessLog(__file__)
        
         
    def process_request(self, req, resp):
        auth(req, resp , self.accesslogger)
