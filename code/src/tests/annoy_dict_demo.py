
import sys
sys.path.append("../..")


from src.schemas import defines
from src.db.treenode import annoy_dict


if __name__ == '__main__':
    """
    annoy dict conf
    [img_tests_annoy_dict]
    dict_type = annoy_dict
    reload_cmd = reload_annoy_dict
    full_path = ./data/img_tests_annoy_dict
    dimension = 10
    metric = euclidean
    search_k = -1
    """

    dict_conf = defines.DictConf(
            'annoy_dict', 'img_tests_annoy_dict', 'reload_annoy_dict',
            './tests_data/img_tests_annoy_dict',
            {
                "dimension":10,
                "metric":"euclidean",
                "search_k":-1
            })

    img_tests_annoy_dict = annoy_dict.AnnoyDict()
    if defines.ReturnCode.SUCC != img_tests_annoy_dict.load(dict_conf):
        print "Fail to load img_tests_annoy_dict"
        sys.exit()

    # find by index
    # [0, 85, 42, 11, 54, 38, 53, 66, 19, 31]
    id_list, weight_list = img_tests_annoy_dict.find_by_key(0, 10)

    print id_list
    print weight_list

    # find by vector
    #print img_tests_annoy_dict.find_by_vector([0, 85, 42, 11, 54, 38, 53, 66, 19, 30], 10)
