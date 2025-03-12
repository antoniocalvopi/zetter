# FAQs - Zetter (Django + React + Vite + Tailwind)

## Django - Backend

1. ¿Por qué usar Django para Zetter?

Django es un framework robusto y escalable que facilita la creación de aplicaciones web seguras y eficientes. Su sistema de ORM, autenticación integrada y modularidad lo hacen ideal para gestionar el backend de Zetter.

2. ¿Cómo configuro Django en un entorno de desarrollo?

Ejecuta los siguientes comandos:

```BASH
    python -m venv venv  # Crear entorno virtual
    source venv/bin/activate  # Activar en Linux/Mac
    venv\Scripts\activate  # Activar en Windows
    pip install -r requirements.txt  # Instalar dependencias
    python manage.py migrate  # Aplicar migraciones
    python manage.py runserver  # Iniciar el servidor
```

3. ¿Cómo administro la base de datos en Django?

Django usa ORM para manejar bases de datos. Puedes definir modelos en models.py y aplicar migraciones con:

```BASH
    python manage.py makemigrations
    python manage.py migrate
```

Para acceder a la base de datos puedes usar:

```BASH
    python manage.py dbshell  # Si usas PostgreSQL o SQLite
```

4. ¿Cómo protejo mi API en Django?

Puedes usar Django Rest Framework (DRF) con autenticación por tokens o JWT. Ejemplo con SimpleJWT:

```PYTHON
    pip install djangorestframework-simplejwt
```

Configura settings.py:

```PYTHON
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```
Genera tokens:

```BASH
python manage.py createsuperuser  # Crear usuario admin
python manage.py shell
```
``` PYTHON
from rest_framework_simplejwt.tokens import RefreshToken
refresh = RefreshToken.for_user(user)
print(refresh.access_token)  # Token JWT
```

5. ¿Cómo manejar CORS en Django?

Si el frontend consume la API desde otro dominio, instala y configura django-cors-headers:

```BASH
pip install django-cors-headers
```

Añádelo en INSTALLED_APPS y en MIDDLEWARE:

```PYTHON
INSTALLED_APPS = [
    'corsheaders',
    ...
]
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]
CORS_ALLOWED_ORIGINS = ["http://localhost:5173"]  # Dominio del frontend
```

## React + Vite + Tailwind - Frontend

6. ¿Por qué usar Vite en lugar de Create React App?

Vite ofrece:

- Mayor velocidad en el arranque del proyecto.

- HMR (Hot Module Replacement) eficiente.

- Menos consumo de recursos en desarrollo.

- Optimización automática para producción.


7. ¿Cómo configuro un nuevo proyecto con Vite y React?

Ejecuta:

```BASH
npm create vite@latest my-app --template react
cd my-app
npm install
npm run dev
```

8. ¿Cómo configuro Tailwind CSS en Vite?

Instala Tailwind:
```BASH
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Configura tailwind.config.js:

```JAVASCRIPT
/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
};
```

Importa Tailwind en index.css:

```CSS
@tailwind base;
@tailwind components;
@tailwind utilities;
```

9. ¿Cómo consumo la API de Django en React?

Usa fetch o Axios para obtener datos desde el backend:

```BASH
npm install axios
```

Ejemplo de petición con Axios:

```TYPESCRIPT
import axios from "axios";

const fetchData = async () => {
  try {
    const response = await axios.get("http://localhost:8000/api/notas/");
    console.log(response.data);
  } catch (error) {
    console.error("Error al obtener datos", error);
  }
};
```

10. ¿Cómo manejo autenticación con JWT en React?

Al recibir un token JWT desde Django, guárdalo en localStorage o sessionStorage:

```TYPESCRIPT
localStorage.setItem("token", accessToken);
``` 

Para incluirlo en peticiones:

```TYPESCRIPT
axios.get("http://localhost:8000/api/protegido/", {
  headers: { Authorization: `Bearer ${localStorage.getItem("token")}` }
})
```

11. ¿Cómo implementar rutas protegidas en React con React Router?

Instala React Router:

```BASH
npm install react-router-dom
```

Ejemplo de una ruta protegida:

```TYPESCRIPT
import { Navigate } from "react-router-dom";

const PrivateRoute = ({ children }) => {
  const token = localStorage.getItem("token");
  return token ? children : <Navigate to="/login" />;
};
```

Uso en el router:
```TYPESCRIPT
<Route path="/dashboard" element={<PrivateRoute><Dashboard /></PrivateRoute>} />
```

12. ¿Cómo hago despliegue de backend (Django) y fronted (vite)?

Existen numerosas opciones pero las dos más sencillas para un primer despliegue o entorno de producción so:


1. **Integrarlo con Django**: Mover los archivos de React dentro del proyecto de Django y servir la aplicación.

    Frontend: Genera la versión de producción:

    ```BASH
    npm run build
    ```
    Backend: Sirve los archivos estáticos en Django.
    Configura settings.py:
    
    ```PYTHON
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [BASE_DIR / "frontend/build"]
    ```
    
    Mueve los archivos de React dentro del proyecto de Django y sirve la       aplicación.

2. **Desplegarlo como servicios separados**: Mantener backend y frontend en servidores distintos (o el mismo), configurando correctamente la API en el frontend de Zetter mediante el archivo environment de Vite, lo que facilita cambios sin modificar el código fuente. Muy recomendable usar [Docker](https://www.docker.com/) o [Kubernetes](https://kubernetes.io/).
