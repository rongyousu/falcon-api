import sys
sys.path.append("..")


from util.defines import *
from util.unit_dict import *
from util.dual_dict import *
from util.dict_manager import DictManager


if __name__ == '__main__':

    #dd = DualDict()
    #dd.unit_dict


    conf_list = []

    udc = DictConf('annoy_dict', '1', '1', '123')
    conf_list.append(udc)

    udc = DictConf('annoy_dict', '2', '1', '123')
    conf_list.append(udc)

    udc = DictConf('annoy_dict', '1', '1', '123')
    conf_list.append(udc)

    udc = DictConf('error_dict', '3', '1', '123')
    conf_list.append(udc)

    dict_manager = DictManager()

    dict_manager.load_dicts(conf_list)

    dict_manager.reload('123')

    new_dict = dict_manager.get_dict('1')
    print id(new_dict)
    new_dict.identity
