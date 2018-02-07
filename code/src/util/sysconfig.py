import aumbry




class AppConfig(aumbry.YamlConfig):
    __mapping__ = {
        'gunicorn': ['gunicorn', dict],
    }

    gunicorn = {}
