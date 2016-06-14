import socket

#My laptop is name 'Guinsly-thinkpad-lenovo'
if 'guinsly' in socket.gethostname():
    from .development import *
    from django.core.urlresolvers import reverse_lazy
    LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
    LOGIN_URL = reverse_lazy('login')
    LOGOUT_URL = reverse_lazy('logout')
    print('--dev--settings--')
else:
    from .production import *
    #print('prod--settings')
#this file won't be load in git and in the
