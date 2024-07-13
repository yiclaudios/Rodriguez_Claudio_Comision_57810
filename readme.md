# Rodriguez_Claudio_Comision_57810

Proyecto final - RODRIGUEZ CLAUDIO - COMISION 57810

Tabla de contenido.

	- Información general del Proyecto
	- Nombre del Proyecto
	- Objetivo
	- Modelos
    
- Información general del Proyecto

Proyecto final del curso de Python, de Claudio Rodriguez - Comisi{on 57810
Se desarrolla una web utilizando Django y Python, aplicando todo lo aprendido en el curso.
La aplicación web, es un proyecto para administración de flotas de vehículos (T.A.F - Te Administramos la Flota).

Ingresando a la web, se tiene un menú lateral izquierdo con las opciones:
Vehículos, Clientes, Proveedores, Empleados, y Acerca de mi

En cada opción al ingresar, se listan los datos de esa opción.
Se cuenta con una opción de formulario, que indica la posibilidad de ingresar nuevos registros. 
Para ello se accede haciendo clic en la opción "Formulario ingreso de..."

En la opción de vehículos, se cuenta con un buscador, el cual nos permite buscar una matrícula.

- Nombre del proyecto

El proyecto se llama ProyectoSAF, y tiene una aplicación llamada appSAF

Administrador
Usuario: admin
Password: Admin1234.

Otro
Usuario: profesor
Password: comision57810

- Objetivo

El objetivo de esta web, es que el usuario logueado, pueda realizra todas las acciones de ingreso, modificación, búsqueda - lectura y borrado (CRUD), de los Vehículos, Clientes, Proveedores, y Empleados, los cuales son las bases de la administración.

*** A este proyecto le falta todo lo relacionado a los reportes e ingresos de información como ser gastos, los cuales brindarían la información necesaria para una empresa.


- Modelos

	** Vehiculo:
	Aquí se ingresa la información de cada vehículo.
	
	marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    matricula = models.CharField(max_length=20)
    
	
	** Cliente:
	Infomración básica de un cliente
	
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email  = models.EmailField()

	** Proveedor:
	Información relativa al proveedor
	
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email  = models.EmailField()
    direccion = models.CharField(max_length=100)

    -- Se agrega la clase Meta para configurar el pluran en lugar de poner ProveedorS, ponga Proveedores
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ["nombre", "apellido"]

	** Empleado:
	Información básica de los empleados
	
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    documento = models.CharField(max_length=20)

	** Avatar:
	Model del avatar del usuario
	
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
	