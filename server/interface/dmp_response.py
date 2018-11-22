


from util import defines
from interface import test_feature


class DmpResponse(object):
    """
    Represents an HTTP response to a client request
    """

    """ response status """
    # response status
    status = True           # required
    # response status msg
    msg = ''                # optional

    """ response data """
    request_id = ''         # required
    # test feature list
    _test_features = []     # optional

    def __init__(self):
        pass

