from .base import *
from .base import _
import json

def clean(obj):
    if isinstance(obj, dict):
        return {str(key): val for key, val in obj.iteritems()}

    if isinstance(obj, list):
        return [clean(val) for val in obj]

    if isinstance(obj, basestring):
        return str(obj)

    return obj

def load_config(obj, into):
    for key in obj:
        into[str(key)] = clean(obj[key])

with open(os.environ.get('WHS_CONFIG'), 'r') as config:
    load_config(json.loads(config.read()), locals())

TEMPLATE_DEBUG = False
DEBUG = False
