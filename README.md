# Segundo Parcial
## Programación Web III - MVC WEB APP

### Antes de Empezar:

1. Realiza un **Fork** de este repositorio:

![Repositorio del Segundo Parcial](https://live.staticflickr.com/65535/53738608284_706405e96e_z.jpg)

2. Si vas a trabajar en tu equipo local clona el nuevo repositorio resultado del **Fork** y ábrelo con **VSCode** o el editor de tu preferencia para trabajar tu solución. También puedes trabajar tu solución en **GitHub Codespaces**.

3. Completa tus datos personales en la siguiente tabla:
    | Nombre   | Apellido   | CI   |
    | -------- | ---------- | ---- |
    | `Jonathan Gerson` | `Gutierrez Condori` | `8295962` |

4. Realiza un commit de esta modificación y sube los cambios a tu repositorio remoto ejecutando los siguientes comandos desde la terminal de tu equipo local o desde **GitHub Codespaces**:
    ```bash
    git add .
    git commit -m "datos actualizados"
    git push origin main
    ```
5. En la terminal ejecuta el siguiente comando para instalar las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

### Contexto:

Eres el **Back-End Developer** de la Caja Nacional de Salud, el directo General de la Caja te ha pedido realizar una demo de un sistema para gestionar la información de los pacientes.

Se debe almacenar en **Base de Datos** los siguientes datos de los **Pacientes**:
- **id**: Identificador único de la paciente. De tipo **entero y autoincremental**.
- **name**: Nombres del paciente. De tipo **cadena de texto**.
- **lastname**: Apellidos del paciente. De tipo **cadena de texto**.
- **ci**: Cédula de identidad del paciente. De tipo **cadena de texto**.
- **birth_date**: Fecha de nacimiento del paciente. De tipo **cadena de texto**

Se debe almacenar en **Base de Datos** los siguientes datos de los **Usuarios**:
- **id**: Identificador único del usuario. De tipo **entero y autoincremental**.
- **username**: Nombre del usuario. De tipo **cadena de texto**.
- **password**: Contraseña del usuario. De tipo **cadena de texto**.
- **role**: Rol del usuario (admin, doctor). De tipo **cadena de texto**.

Existe un usuario administrador (`admin`) puede realizar las siguientes acciones:
- **Listar a los pacientes**: Listar todos las pacientes.
- **Crear un paciente**: Crear un nuevo paciente.
- **Actualizar un paciente**: Actualizar un paciente existente.
- **Eliminar un paciente**: Eliminar un paciente existente. 

Existe un usuario doctor (`doctor`) que puede realizar las siguientes acciones:
- **Listar a los pacientes**: Listar todos las pacientes del equipo.

Los usuarios deben autenticarse en la API para poder realizar las acciones permitidas. Se debe utilizar **Cookies** para mantener la sesión del usuario en la aplicación.

### Tareas:

Construye una **Web App MVC** que permita realizar las operaciones **CRUD** sobre los pacientes y debes enlazarlas con las plantillas **HTML** construidas en **Jinja** que proporciono el equipo de Front-end. Puedes encontrar las plantillas en la carpeta [templates](app/templates/).
 
La aplicación debe contar con las siguientes rutas:
- **/**: Ruta de inicio de la aplicación. Debe mostrar un formulario de inicio de sesión.
- **/users**: Ruta para registrar un nuevo usuario. Debe mostrar un formulario para registrar un nuevo usuario.
- **/login**: Ruta para autenticar a un usuario. Debe mostrar un formulario para autenticar a un usuario.
- **/logout**: Ruta para cerrar la sesión de un usuario. Debe cerrar la sesión del usuario y redirigirlo a la página de inicio.
- **/patients**: Ruta para listar a los pacientes. Debe mostrar una lista de pacientes. Es lo primero que se debe mostrar al autenticarse en la aplicación.
- **/patients/create**: Ruta para crear un nuevo paciente. Debe mostrar un formulario para crear un nuevo paciente.
- **/patients/{id}/update**: Ruta para actualizar un paciente existente. Debe mostrar un formulario para actualizar la información del paciente.
- **/patients/{id}/delete**: Ruta para eliminar un paciente existente. Debe mostrar un mensaje de confirmación para eliminar al paciente.

### Restricciones:
1. Debes utilizar **Python** como lenguaje de programación.
2. Debes utilizar el framework **Flask** para el desarrollo de la API.
3. Debes utilizar **SQLAlchemy** como ORM para la conexión con la Base de Datos.
4. Debes utilizar **SQLite** como motor de Base de Datos.
6. Debes utilizar **Flask Login** para la autenticación de los usuarios.
7. Las respuestas de la API deben ser en formato **JSON**.
8. Debes utilizar el patrón de diseño **MVC** para la estructura de tu proyecto.
9. Debes manejar los errores y excepciones que puedan ocurrir en la API con los códigos de estado HTTP correspondientes.

## Entrega:
1. La estructura de carpetas de tu solución debe estar dentro de la carpeta `app`
2. Una vez tengas tu solución debes realizar un **Commit** y un **Push** a tu repositorio en **GitHub** ejecutando los siguientes comandos desde la terminal de tu equipo local o desde **GitHub Codespaces**:
    ```bash
    git add .
    git commit -m "Entrega Final"
    git push origin main
    ```
3. Una vez completado el paso anterior adjunta la **URL** de tu repositorio de **GitHub** en la paciente asignada en **Google Classroom**. 


### Restricciones:

Durante el examen solo puede consultar los siguientes recursos:
- [Documentación de Python](https://docs.python.org/3/)
- [Documentación de Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Documentación de SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
- [Documentación de Flask Login](https://flask-login.readthedocs.io/en/latest/)
- [Documentación de SQLite](https://www.sqlite.org/docs.html)
- [Documentación de Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
- [Documentación de Bulma](https://bulma.io/documentation/)
