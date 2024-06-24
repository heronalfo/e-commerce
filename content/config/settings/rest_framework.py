REST_FRAMEWORK = {
   'DEFAULT_PARSER_CLASSES':
   
       (
             
       'rest_framework.parsers.JSONParser',      
       'rest_framework_xml.parsers.XMLParser',
       
   ),
          
   'DEFAULT_RENDERER_CLASSES':   
       (
              
       'rest_framework.renderers.JSONRenderer',      
       'rest_framework_xml.renderers.XMLRenderer',
       
   ),
   
   'DEFAULT_THROTTLE_CLASSES': (
   
     'rest_framework.throttling.AnonRateThrottle',     
     'rest_framework.throttling.UserRateThrottle',
     
   ),
   
   'DEFAULT_PERMISSION_CLASSES': (
   
       'rest_framework.permissions.AllowAny',
   
   ),

   'DEFAULT_AUTHENTICATION_CLASSES': (
    
     
       'rest_framework_simplejwt.authentication.JWTAuthentication',
       'rest_framework.authentication.BasicAuthentication',
       'rest_framework.authentication.SessionAuthentication',
        
   ),
    

   'DEFAULT_PAGINATION_CLASS':
        
       'rest_framework.pagination.LimitOffsetPagination',    
       'PAGE_SIZE': 100,
      
   'DEFAULT_THROTTLE_RATES': {
   
       'anon': '100/day',
       'user': '1000/day',
       
                 
   },
                      
}