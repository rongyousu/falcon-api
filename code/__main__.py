"""
Example Application

Usage:
    falcon-example [options]

Options:
    -h --help                   Show this screen.
"""
import aumbry
from docopt import docopt
from gunicorn.app.base import BaseApplication
#from gunicorn.workers.sync import SyncWorker

from app import MyService
from src.util import sysconfig
from src.util import configmanager

from meinheld.gmeinheld import MeinheldWorker

class CustomWorker(MeinheldWorker):
     def handle_quit(self,sig,frame):
         self.app.application.stop(sig)
         super(CustomWorker, self).handle_quit(sig, frame)

     def run(self):
         self.app.application.start()
         super(CustomWorker, self).run()




#class CustomWorker(SyncWorker):
#    def handle_quit(self, sig, frame):
#        self.app.application.stop(sig)
#        super(CustomWorker, self).handle_quit(sig, frame)
#
#    def run(self):
#        self.app.application.start()
#        super(CustomWorker, self).run()


class GunicornApp(BaseApplication):
    """ Custom Gunicorn application

    This allows for us to load gunicorn settings from an external source
    """
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(GunicornApp, self).__init__()

    def load_config(self):
        for key, value in self.options.items():
            self.cfg.set(key.lower(), value)

        self.cfg.set('worker_class', '__main__.CustomWorker')

    def load(self):
        return self.application


def main():
    docopt(__doc__)

    cfg = aumbry.load(
        aumbry.FILE,
        sysconfig.AppConfig,
        {
            'CONFIG_FILE_PATH': './config/platform/config.yml'
        }
    )
    
    managercfg={}
    managerConfig= configmanager.ConfigManager('./config/manager.conf')
    managercfg['manager']=managerConfig
    
    triggerConfig= configmanager.ConfigManager('./config/triggermanager.conf')
    managercfg['trigger']=triggerConfig
    #print triggerConfig.get_key('trigger','test_dis')
   
    displayConfig = configmanager.ConfigManager('./config/display.conf') 
    managercfg['display']=displayConfig    

    api_app = MyService(managercfg)
    gunicorn_app = GunicornApp(api_app, cfg.gunicorn)

    gunicorn_app.run()
if __name__ ==  '__main__':
         
        main()   
