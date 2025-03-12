# Roadmap Django

## 1. Introducción al Roadmap

Este roadmap describe las tecnologías de *Django* utilizadas en el desarrollo de Zetter, una aplicación open-source para la organización y conexión de ideas mediante el método Zettelkasten. El proyecto se desarrolla con un backend basado en **Django** y un frontend con **React** + **Vite** + **Tailwind**. La arquitectura está pensada para ser escalable y modular, utilizando microservicios para facilitar el mantenimiento y la evolución.

## 2. **Estructura y Tecnología de Django en el Backend**

### **Django Framework**

- **¿Qué es Django?**  
    Django es un framework web de alto nivel basado en Python, conocido por su agilidad en el desarrollo de aplicaciones web seguras y escalables. En este proyecto, Django gestiona el backend de la aplicación, incluyendo la lógica de negocio, la gestión de usuarios y las interacciones con la base de datos.

#### **Principales Características:**

- **Seguridad**: Protección contra amenazas comunes como inyecciones SQL, XSS, y CSRF.
- **Reutilización de código**: Enfoque **DRY** (Don’t Repeat Yourself) para evitar código duplicado.
- **Escalabilidad**: Ideal para proyectos de cualquier tamaño, desde MVP hasta aplicaciones grandes.

#### **Tecnologías Clave de Django:**

- **Django ORM (Object-Relational Mapping)**:  
    El ORM de Django facilita la interacción con la base de datos utilizando modelos de Python en lugar de escribir SQL directamente. Permite realizar operaciones CRUD de manera eficiente y segura, aprovechando las capacidades avanzadas de bases de datos como **PostgreSQL**.

---

### **Django Rest Framework (DRF)**

- **¿Qué es DRF?**  
    [Django Rest Framework](https://www.django-rest-framework.org/) (DRF) es una librería para crear APIs RESTful dentro de Django. En **Zetter**, se utiliza para gestionar la comunicación entre el frontend y el backend, especialmente para gestionar la creación, lectura, actualización y eliminación de notas, además del *crud* de usuarios.

#### **Ventajas de DRF:**

- Facilita la creación de APIs RESTful de manera sencilla y escalable.
- Ofrece herramientas como autenticación, permisos, y serialización de datos.
- Optimización para trabajar con JSON y otras estructuras de datos.

#### **Flujos Clave de DRF:**

1. **Serialización de Modelos**: Convierte los objetos de los modelos de Django en JSON y viceversa.
2. **Autenticación y Autorización**: Facilita el manejo de usuarios y permisos.
3. **Visualización de Datos**: Permite la representación de los datos de manera legible y accesible a través de vistas y APIs.

---

### **JWT (JSON Web Tokens)**

- **¿Qué es JWT?**  
    En el proyecto **Zetter**, **JWT** se utiliza para manejar la autenticación de usuarios de manera segura. Cada vez que un usuario inicia sesión, se genera un token que se utiliza para validar futuras solicitudes.

#### **Flujo de Autenticación con JWT:**

1. **Registro**: Al registrar un usuario, se genera un JWT que incluye información básica del usuario.
2. **Inicio de sesión**: Al iniciar sesión, el sistema valida las credenciales y genera un par de tokens JWT (Access Token y Refresh Token).
3. **Acceso a recursos protegidos**: Para acceder a rutas protegidas, el usuario debe incluir el Access Token en el encabezado de las solicitudes.

#### **Ventajas de JWT:**

- **Escalabilidad**: No requiere mantener sesión en el servidor, ideal para aplicaciones distribuidas.
- **Seguridad**: Permite verificar la autenticidad de las solicitudes y asegura la integridad de los datos.

---

### **PostgreSQL**

- **¿Por qué PostgreSQL?**  
    **PostgreSQL** es una base de datos relacional robusta y escalable. En **Zetter**, se utiliza para gestionar la información crítica como las notas de los usuarios, sus relaciones y categorías.

#### **Ventajas de PostgreSQL:**

- Soporta transacciones **ACID** (Atomicidad, Consistencia, Aislamiento, Durabilidad).
- Es ideal para manejar datos complejos y consultas avanzadas.
- Escalable para manejar grandes volúmenes de datos y múltiples usuarios.

#### **Relación con Django**:

Django está completamente integrado con PostgreSQL a través de su ORM, permitiendo la creación de modelos de datos que se traducen automáticamente en tablas de bases de datos.

---

## 3. **Arquitectura del Proyecto Zetter**

La arquitectura de **Zetter** sigue un enfoque **modular** y **escalable**, utilizando **microservicios** para manejar diferentes aspectos del backend. Esto permite que cada parte del sistema sea independiente y se pueda desarrollar, probar y escalar por separado.

### **Estructura del Backend en Django**:

```bash
backend/
├── auth_service/
│   ├── models.py         # Definición de modelos relacionados con la autenticación
│   ├── views.py          # Vistas de autenticación y autorización
│   ├── serializers.py    # Serializadores de datos para JWT
│   ├── urls.py           # Rutas de autenticación
├── notes_service/
│   ├── models.py         # Definición de modelos de notas
│   ├── views.py          # Vistas para gestionar notas
│   ├── serializers.py    # Serializadores de datos de notas
│   ├── urls.py           # Rutas de notas
├── backend/
│   ├── settings.py       # Configuración global del proyecto
│   ├── urls.py           # Rutas generales del proyecto
│   ├── wsgi.py           # Configuración para producción
```

### **Servicios y Microbackends**:

- **`auth_service/`**: Maneja la autenticación de usuarios, incluyendo la creación de tokens JWT.
- **`notes_service/`**: Gestiona las notas, su creación, actualización y lectura a través de APIs.

---

## 4. **Roadmap de Desarrollo de Funcionalidades**

### **Fase 1: Autenticación y Autorización**

1. Implementación del sistema de registro de usuarios.
2. Creación de APIs para inicio de sesión y generación de JWT.
3. Configuración de autenticación JWT en DRF.

### **Fase 2: Gestión de Notas**

1. Desarrollo de modelos para notas, categorías y etiquetas.
2. Implementación de APIs CRUD para notas.
3. Configuración de vistas y serializadores de notas en **notes_service**.

### **Fase 3: Integración y Escalabilidad**

1. Integración de microservicios con la interfaz de usuario (frontend en React).
2. Configuración de Docker para contenedores de la base de datos.
3. Pruebas de carga y rendimiento.
4. Dockerizar el backend, BD y frontend.
---

## 5. **Conclusión**

El roadmap de **Zetter** detalla el desarrollo de las principales funcionalidades del backend utilizando **Django**. El uso de tecnologías como **Django Rest Framework**, **JWT** y **PostgreSQL** garantiza un backend seguro, escalable y eficiente para gestionar las notas y la autenticación de los usuarios. El enfoque modular con microservicios facilita la evolución del proyecto y su integración con el frontend basado en **React**.

Este roadmap proporciona una visión simplificada y clara de los pasos a seguir y las tecnologías clave para llevar a cabo el desarrollo de esta propuesta: **Zetter** de manera efectiva y con un enfoque en la calidad y no en la cantidad.

Para tener un roadmap más claro y detallado he reacdo un script *.sh* donde se puede visualizar el roadmap en detalle y con sus referencias para poder aprender estas tecnologías.