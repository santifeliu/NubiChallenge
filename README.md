Nubi Users Challenge
=============

Antes de iniciar se debe generar el archivo con la configuración inicial *.envs/.django* se puede copiar de *.envs/.django_sample*

Comandos importantes a saber

Build docker-compose
       
    docker-compose -f local.yml build
        
Para levantar docker
    
    docker-compose -f local.yml up

Ejecutar pruebas

    python manage.py test

Cargar fixture de prueba

    python manage.py loaddata nubi/tests/test_users.json

Descargar collection de postman desde

    http://localhost:8000/swagger.json

Filtros exactos posibles

    /users/?email=<string>
    /users/?sex_type=male
    /users/?sex_type=female

Sorting posibles

    /users/?ordering=email
    /users/?ordering=-email
