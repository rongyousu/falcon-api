

from src.db.treenode import annoy_dict


class DictCreator(object):
    """
    dict factory
    create dict by type
    """

    @staticmethod
    def create_dict(dict_conf):
        if dict_conf.dict_type == 'annoy_dict':
            return annoy_dict.AnnoyDict(dict_conf)
        else:
            return None

