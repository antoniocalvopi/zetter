# Zetter

Zetter es una aplicación open-source diseñada para gestionar notas basadas en el método Zettelkasten. Su propósito es ofrecer un espacio digital donde las ideas se conectan de forma fluida, facilitando el aprendizaje, la estructuración del pensamiento y la creación de conocimiento.

## 🚀 Características Principales

- **Notas Atómicas**: Crea notas independientes sin la necesidad de una estructura rígida.
- **Enlaces Bidireccionales**: Relaciona notas para construir un mapa de ideas interconectadas.
- **Vista Gráfico**: Navega visualmente a través de la red de notas y sus conexiones.
- **Autenticación Segura**: Utiliza JWT para la autenticación de usuarios, garantizando un inicio de sesión seguro.
- **Backend Robusto**: Desarrollado con **Django** y **Django Rest Framework**, brindando seguridad y escalabilidad.
- **Frontend Moderno**: Construido con **React**, **Vite** y **Tailwind CSS**, ofreciendo una experiencia rápida y fluida.

## 🛠️ Tecnologías Utilizadas

- **Frontend**: React, Vite, Tailwind CSS
- **Backend**: Django, Django Rest Framework, JWT
- **Base de Datos**: PostgreSQL

## 📚 Documentación

### [Guía de Versionado](/docs/versionado.md)
Esta guía describe cómo se utiliza **Semantic Versioning (SemVer)** para asegurar la consistencia en el control de versiones de **Zetter**. Para más detalles, revisa el [documento completo](docs/versionado.md).

### [Roadmap](/docs/django.md)
Un vistazo a los conocimientos necesarios para el desarollo actual y futuro de **Zetter**, incluyendo enlace a recursos, tecnologías utilizadas en el proyecto y otroas tecnologías interesantes relacionadas. Para una visión más detallada, consulta el [roadmap completo](docs/roadmap.md).

### [Reflexiones](/docs/reflexion.md)
Un espacio donde reflexiono sobre la combinación de tecnologías (React, Vite y Tailwind CSS), los cambios de enfoque durante el desarrollo, y las lecciones aprendidas. Puedes leer más en las [reflexiones completas](docs/reflexion.md).

### [Guía de Pull Requests (PRs)](docs/guia-pr.md)
Aquí se detallan las mejores prácticas y convenciones para enviar **Pull Requests** al proyecto. Asegúrate de seguir estas pautas para contribuir de manera efectiva.

### [Guía de Issues](docs/guia-issues.md)
Instrucciones sobre cómo crear y gestionar **issues** dentro del proyecto, asegurando que las solicitudes estén bien documentadas y sean fácilmente manejables.

### [Guía de Commits](docs/guia-commits.md)
Convenciones sobre el formato de mensajes de **commit**, utilizando el estándar **Conventional Commits** para asegurar claridad y coherencia en el historial de cambios.

### [Contribuir al Proyecto](docs/contributing.md)
Si deseas contribuir, revisa esta guía que explica cómo hacer un **fork**, crear ramas, realizar cambios y enviar pull requests.

## 🧑‍💻 Instalación

### Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/zetter.git
cd zetter
```

### Configurar el Entorno del Backend

1. **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Configurar la base de datos**:
    ```bash
    python manage.py migrate
    ```

3. **Crear un superusuario**:
    ```bash
    python manage.py createsuperuser
    ```

4. **Ejecutar el Backend**:
    ```bash
    python manage.py runserver
    ```

### Configurar el Entorno del Frontend

1. **Instalar dependencias**:
    ```bash
    npm install
    ```

2. **Ejecutar el Frontend**:
    ```bash
    npm run dev
    ```

Consulta la [documentación](docs/guias_tecnicas/setup.md) con más detalles.


## 🚀 Uso del Proyecto

Los pasos necesarios para **arrancar** y **probar** el proyecto **Zetter** de manera local los encuentras en la documentación, pero antes de empezar a probar el proyecto debes completar la instalación:

### [Instrucciones de Inslatación](docs/guias_tecnicas/setup.md)

Una vez instalada las dependencias, dentro del archivo [`usage.md`](docs/guias_tecnicas/usage.md) se detallan todos los pasos necesarios para configurar y probar **Zetter** en tu máquina local. Esto incluye:

1. **Clonar el Repositorio**: Instrucciones para obtener el código fuente del proyecto.
2. **Configuración del Entorno Backend**: Cómo preparar el entorno para ejecutar el backend con Django y PostgreSQL.
3. **Configuración del Entorno Frontend**: Instrucciones para ejecutar el frontend usando React y Vite.
4. **Ejecutar el Proyecto**: Pasos para poner en marcha tanto el backend como el frontend, y empezar a usar la aplicación localmente.

Puedes acceder al archivo completo con las instrucciones detalladas aquí:
[Guía de Uso Completo](docs/guias_tecnicas/usage.md)

## 💡 Contribuciones

Si estas leyendo esto, y estas interesado en contribrui: ¡Gracias por tu interés en contribuir en **Zetter**! Para más detalles sobre cómo puedes participar, revisa nuestra [guía de contribuciones](docs/contributing.md).

---

## 📍 Contacto

Si tienes alguna pregunta o sugerencia, no dudes en abrir un **issue** o unirte a nuestras **discusiones** en [GitHub Discussions](https://github.com/tu-usuario/zetter/discussions).

---

**"Zetter: Donde las ideas encuentran su conexión."** 🧠✨