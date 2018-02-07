
import sys
sys.path.append("../..")

from src.systemlog import accesslog

if __name__ == '__main__':

    log = accesslog.AccessLog('./logs/access.log')

    log.info("Hello")
    log.error("Oops")
    log.warning("OMG")

    log.push_info("key1", "value1")
    log.push_info("key2", 32)
    log.push_info("key3", "value3")

    log.print_info()
