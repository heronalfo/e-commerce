# Error and exception monitoring  
LOGGING = {
      'version': 1,
      'disable_existing_loggers': False,
      'handlers': {
          'file': {
              'level': 'ERROR',
              'class': 'logging.FileHandler',
              'filename': 'logs/errors.log',
          },
      },
      'loggers': {
          'django': {
              'handlers': ['file'],
              'level': 'ERROR',
              'propagate': True,
          },
      },
}