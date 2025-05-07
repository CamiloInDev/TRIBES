# 👕 Tribes - Tienda de Ropa Online

**Tribes** es una página web para vender ropa. Por ahora permite que las personas se registren, inicien sesión con unos campos totalmente personalizados haciendo uso del override de usuarios y añadiendo campos como telefono y direccion,  y accedan a una zona donde en el futuro se mostrarán productos. El proyecto está hecho con Django (Python) y usa una base de datos para guardar los datos de los usuarios.

## ✨ ¿Qué tiene esta web?

- Registro de usuarios  
- Override de los usuarios por defecto que añade campos de telefono y direccion
- Inicio de sesión  
- Organización del proyecto en módulos  
- Conexión a base de datos (PostgreSQL o SQLite)  
- Diseño con HTML y CSS  

## 🧰 Lo que se usó

- Python y Django  
- Base de datos PostgreSQL  
- HTML y CSS básicos  
- Entorno virtual (venv)  

## ▶️ Cómo usarlo

1. **Abir el proyecto**  
   Abrir el proyrvtp
2. **Crear y activar el entorno virtual**  
   - En Windows:  
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```  
   - En Mac/Linux:  
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
3. **Instalar lo necesario**  
   ```bash
   pip install -r requirements.txt
   ```
4. **Configurar la base de datos** (en `settings.py`)  
   Cambia el nombre de la base de datos, usuario y contraseña si usas PostgreSQL.
5. **Crear las tablas**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. **Iniciar el servidor**  
   ```bash
   python manage.py runserver
   ```  
   Abre el navegador y entra a: http://127.0.0.1:8000

## 📁 Carpetas principales

- `usuarios`: todo lo relacionado al registro e inicio de sesión  
- `tiendaapp`: para mostrar productos más adelante  
- `templates`: archivos HTML  
- `static`: estilos (CSS)  

## 👤 Autor

Desarrollado por Camilo Infante  


---

Proyecto en desarrollo. Próximamente se agregará catálogo de productos, carrito y pagos.
