import argparse
import configparser
import logging
import os

from dotenv import load_dotenv

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()

if args.verbose:
    logging.basicConfig(level=logging.DEBUG)

# load env file
env_path = os.path.join(os.getcwd(), '.env')
load_dotenv(dotenv_path=env_path)

logging.debug("Grabbing password from .env file")
secret = os.getenv('client')
if not secret:
    raise Exception("Missing password from .env file")

# read the config file
conf = configparser.ConfigParser()
conf_path = os.path.join(os.getcwd(), "conf.ini")
conf.read(conf_path)

client_id = conf['Info']['client_id']
