
from django.conf import settings

def global_vars(request):
    """ Add settings as global variables to the template context """
    return {'GA_CODE': settings.GA_CODE}