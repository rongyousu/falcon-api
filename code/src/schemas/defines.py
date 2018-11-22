


class ReturnCode(object):
    """
    code for response status
    """

    ERROR   = -1
    SUCC    = 0
    FAIL    = 1


class FeatureType(object):
    """
    feature identity code
    """

    UNKNOWN         = 0
    KNN_TEST        = 1
    STUDENT_INFO    = 2
    COURSE_INFO     = 4


class DictConf(object):
    """
    configure for dicts
    """

    # conf name
    DICT_TYPE = 'dict_type'
    DICT_NAME = 'dict_name'
    RELOAD_CMD = 'reload_cmd'
    FULL_PATH = 'full_path'

    # required option
    dict_type = ''
    dict_name = ''
    dict_md5 = ''
    reload_cmd = ''
    full_path = ''
    # optional option, <name, value>
    option_items = None

    def __init__(self, t, n, rc, fn, oi):
        self.dict_type = t
        self.dict_name = n
        self.reload_cmd = rc
        self.full_path = fn
        self.option_items = oi

    def valid(self):
        return (self.dict_type != '' \
                and self.dict_name != '' \
                and self.reload_cmd != '' \
                and self.full_path != '' \
                and self.option_items is not None)

    def reset(self):
        self.dict_type = ''
        self.dict_name = ''
        self.dict_md5 = ''
        self.reload_cmd = ''
        self.full_path = ''
        if self.option_items is not None:
            self.option_items.clear()

    def __str__(self):
        return "%s|%s|%s|%s|%s" \
                %(self.dict_type, self.dict_name, \
                  self.dict_md5, self.reload_cmd, \
                  self.full_path)
