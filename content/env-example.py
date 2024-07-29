'''
env.py

This module is responsible for defining universal variables for the 
entire Django project and configuration.
'''


SECRET_KEY = 'django-insecure-s44o_bc@y)n$wkqbigp4(z-dmndb7nj)wm(!!bzr2$1he$^k#@'

#Important: If you use a specific SGBD, first install the client for this engine
DJANGO = {

    'DATABASE': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'e-commerce',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'host',
        'PORT': '3306',
    }

}

#Email: main method for sending emails
EMAIL = {
    'SELLERS': [
        {
          'USER': 'your_email',
          'PASSWORD': 'password',
        },
    ]
}