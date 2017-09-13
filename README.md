# Gif Catalog

Este repositiorio contiene el código fuente que sirvió de ejemplo en la charla sobre Vue y Django que di en [el meetup de Vue.js el 12/Sep/2017](https://www.meetup.com/es-ES/VueJS-Madrid/events/242801402/).

Las etiquetas step1 hasta step6 marcan los distintos pasos:

* `step1`: aplicación Django vacía tal y como se crea con el asistente de nuevo proyecto de PyCharm (equivalente a `django-admin startproject gif_catalog`)
* `step2`: aplicación clásica de Django, sirviendo la vista de '/' mediante una plantilla de Django. No se usa Javascript
* `step3`: instalado webpack-bundle-tracker (plugin de webpack) y django-webpack-loader (módulo de Django). Configurado webpack y Django para que funcionen conjuntamente.
* `step4`: una API sencilla para servir JSON desde Django y consumirla desde la app de Vue.js
* `step5`: autenticación por sesiones de Django
* `step6`: rutas (página de detalle)


## Instalación

Recomiendo primero hacer checkout de `master`, instalar las dependencias, etc y luego ir revisando el ejemplo paso por paso

Para ejecutar la parte de Django:

1. crear un entorno virtual (`mkvirtualenv gif_catalog`)
2. instalar las dependencias (`cd gif_catalog; pip install -r requirements.txt`)
3. ejecutar las migraciones de bbdd (`python manage.py migrate`)
4. crear un usuario (`python manage.py createsuperuser`)
5. arrancar django (`python manage.py runserver`)
6. añadir datos de prueba usando [la consola de administración](http://localhost:8000/admin)

Para ejecutar la parte de Vue/webpack:

1. instalar las dependencias (`cd frontend; npm install`)
2. levantar el servidor de desarrollo de webpack (`npm run dev`)

La presentación se puede encontrar [en slideshare](https://www.slideshare.net/secret/vnPNtyKLS7Ku7b)
