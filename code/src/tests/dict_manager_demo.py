
import sys
sys.path.append("../..")


from src.schemas import defines
from src.db.treenode import annoy_dict
from src.db.dict_manager import dict_manager


if __name__ == '__main__':
    """
    # dict manager conf

    [img_tests_annoy_dict]
    dict_type=annoy_dict
    reload_cmd=reload_annoy_dict
    full_path=./data/img_tests_annoy_dict
    search_k=200
    top_k=60
    dimension=100
    n_trees=10

    [txt_tests_annoy_dict]
    dict_type=annoy_dict
    reload_cmd=reload_annoy_dict
    full_path=./data/txt_tests_annoy_dict
    search_k=200
    top_k=60
    dimension=100
    n_trees=10

    """
    all_dicts = dict_manager.DictManager()

    if defines.ReturnCode.SUCC != all_dicts.load_dicts('./tests_conf/dict_manager.conf'):
        print "Fail to load all dicts"
        sys.exit()

    for d in all_dicts:
        print d

    #dict_manager.reload('123')

    #new_dict = dict_manager.get_dict('1')
    #print "dict[%s],type[%s]" %(new_dict.dict_name, new_dict.dict_type)
    #print "All dicts loaded"
    #for d in dict_manager:
    #    print d

