# proyecto_coder
proyecto final coderhouse

#Para crear base de datos, ingresar a la terminal: 

    python manage.py migrate
    
#Para dar de alta el panel de Administrador, ingresar en la terminal:

    python manage.py createsuperuser
    
#Para crear y administrar los modelos en la base de datos:

1- En admin.py hacer importación de models:

    from django.contrib import admin
    from .models import*
   
2- En admin.py agregar todos los modelos de la siguiente forma:

    admin.site.register(Nombre_de_objeto)

#Navegación 

1 - Al abrir el proyecto, la primera template que se visualiza es la del inicio del proyecto.
    1.1 - En ella, tenemos una barra de navegación con botones que permiten acceder a inicio, appnegocio, admin (login de administrador del proyecto) y FAQ (este readme)
    1.2 - También podemos encontrar dos botones cerca del centro de la pantalla, que también nos permite acceder a la AppNegocio o al Login del Administrador

2 - Barra de navegación (común para todas las templates)
    2.1- Mediante ella podemos acceder a los sitios más importantes del proyecto, para facilitar el uso del mismo.
    2.2 - INICIO 
        Este botón nos direcciona a la template de inicio del proyecto
    2.3 - APPNEGOCIO 
        Este botón nos direcciona a la template de inicio de la aplicación (AppNegocio)
    2.4 - ADMIN
        Este botón nos direcciona a la página de login del administrador del proyecto, generada automáticamente por Django.
    2.5 - FAQ
        Este botón nos direcciona a un link de Github, donde está alojado el proyecto. Específicamente, nos direcciona a este readme con la intención de resolver alguna duda de funcionalidad. 

#APPNEGOCIO
    1 - APPNEGOCIO - Página de Inicio
        En esta template podemos observar un menú con un listado de opciones para operar sobre la base de datos del proyecto.
        
        1.1 - NEGOCIOS
            Bajo el apartado de negocios, podemos acceder a dos funcionalidades para operar sobre la base de datos, agregar un negocio o buscar negocios.
        
        1.2 - PRODUCTOS
            Bajo el apartado de productos, podemos acceder a dos funcionalidades para operar sobre la base de datos, agregar un producto o buscar productos.

        1.3 - EMPLEADOS
            Bajo el apartado de empleados, podemos acceder a dos funcionalidades para operar sobre la base de datos, agregar un empleado o buscar empleados.
    
    1.2 - APPNEGOCIO - Agregar un negocio/producto/empleado
        En este template nos encontramos un formulario con espacios para completar con los datos requeridos. Dicho formulario solicitará distintos datos según el modelo sobre el cual estamos operando (negocio, producto o empleado).
        Al apretar el botón de enviar, este formulario creará un nuevo objeto con los atributos que fueron cargados en dicho formulario, luego lo guardará en la base de datos.
    
    1.3 - APPNEGOCIO - Buscar negocios/productos/empleados
        En este template nos encontramos un formulario con un solo campo para rellenar. Dicho formulario solicita el nombre de un negocio, producto o empleado respectivamente. 
        Al apretar el botón enviar, este formulario buscará en la base de datos un objeto de tipo negocio, producto o empleado que CONTENGA en su atributo NOMBRE las letras o palabras ingresadas en el formulario. Por ejemplo, si ingresamos 'A' en el buscador de productos, retornará todos los productos cuyo nombre contenga 'A'.

#MODELOS 
    1- En cuanto a los modelos, nuestra aplicación utiliza tres modelos:
        1.1 - NEGOCIO
            Atributos: nombre, rubro, direccion, codigo_postal 
        1.2 - PRODUCTO
            Atributos: nombre, precio, cantidad, categoría
        1.3 - EMPLEADO
            Atributos: nombre, apellido, sector, edad
    
