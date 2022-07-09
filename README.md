# DJangoRestAPI
Creación de Rest API con Django, transforma los datos de una base de datos(SQLLite3) en formato JSON y los maneja en la WEB  


## Pasos para dar pie al acceso de la rest API con Django

Installamos corsheaders


python -m pip install django-cors-headers

### En settings configuramos los accesos


Añadimos corsheaders al installed APPS

INSTALLED_APPS = [ 
    
    'django.contrib.admin', 
    ... 
    'corsheaders',
    ... 
]


Añadimos corsheaders al middleware


MIDDLEWARE = [

    ...
    'corsheaders.middleware.CorsMiddleware',
    ...

]


Añadimos las rutas que tendran acceso a la API

CORS_ALLOWED_ORIGINS = [

    'http://127.0.0.1:3000',
    'http://localhost:3030',
    'yoursite.com'

]