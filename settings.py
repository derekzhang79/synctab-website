
import os

if os.environ['DEVELOPMENT']:
    from settings_dev import *
else:
    from settings_prod import *