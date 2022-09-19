import os
from dotenv import load_dotenv
import logging


def init_logger(context_name):
    load_dotenv()
    logging.basicConfig(filename='data-loaders.log', encoding='utf-8', level=os.environ.get("LOGLEVEL", "INFO"),
                        format='{0}: %(levelname)s: %(asctime)s: %(message)s'.format(context_name))
    logging.getLogger().addHandler(logging.StreamHandler())
    return logging
