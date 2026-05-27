# Flora_Fauna – Sistema de Gestión de Fauna y Flora

Aplicación de escritorio desarrollada en Python utilizando Tkinter y MySQL para la gestión de especies de fauna y flora.

---

# Descripción

Flora_Fauna es un sistema CRUD desarrollado como proyecto académico, orientado a la administración de registros biológicos mediante una interfaz gráfica conectada a una base de datos MySQL.

La aplicación permite:

* Agregar registros
* Mostrar información almacenada
* Actualizar registros existentes
* Eliminar registros
* Gestionar especies de fauna y flora mediante una interfaz visual amigable

---

# Tecnologías Utilizadas

* Python 3
* Tkinter
* MySQL / MariaDB
* mysql-connector-python
* XAMPP
* Visual Studio Code

---

# Funcionalidades del Sistema

El sistema permite administrar información relacionada con:

* Código de identificación
* Nombre científico
* Hábitat
* Estado de conservación
* Región geográfica

---

# Operaciones CRUD Implementadas

| Operación | Descripción                      |
| --------- | -------------------------------- |
| CREATE    | Agregar nuevos registros         |
| READ      | Mostrar registros almacenados    |
| UPDATE    | Actualizar información existente |
| DELETE    | Eliminar registros               |

---

# Base de Datos

La aplicación utiliza una base de datos MySQL llamada:

```sql
gestion_fauna_flora
```

Tabla principal:

```sql
faunaflora
```

El sistema incorpora:

* PRIMARY KEY
* AUTO_INCREMENT
* UNIQUE KEY
* Inserción de datos de prueba

---

# Estructura de la Tabla

```sql
CREATE TABLE `faunaflora` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `CodigoIdentificacion` varchar(20) DEFAULT NULL,
  `NombreCientifico` varchar(100) DEFAULT NULL,
  `Habitat` varchar(50) DEFAULT NULL,
  `EstadoConservacion` varchar(50) DEFAULT NULL,
  `RegionGeografica` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `CodigoIdentificacion` (`CodigoIdentificacion`)
);
```

---

# Ejemplos de Registros

| Código    | Nombre Científico     | Hábitat                             | Región           |
| --------- | --------------------- | ----------------------------------- | ---------------- |
| FAUNA-001 | Panthera leo          | Sabana                              | África           |
| FAUNA-002 | Puma concolor         | Cordillera y Zonas precordilleranas | Chile            |
| FLORA-003 | Phalaenopsis amabilis | Selva Tropical                      | Sudeste Asiático |

---

# Instalación del Proyecto

## 1. Instalar XAMPP

Descargar XAMPP desde:

https://www.apachefriends.org/

---

## 2. Iniciar Servicios

Desde el panel de control de XAMPP iniciar:

* Apache
* MySQL

---

## 3. Importar Base de Datos

Importar el archivo:

```text
gestion_fauna_flora.sql
```

utilizando phpMyAdmin.

---

# Instalación de Dependencias

Instalar el conector MySQL para Python:

```bash
pip install mysql-connector-python
```

---

# Ejecución del Programa

Ejecutar desde terminal o Visual Studio Code:

```bash
python flora_fauna.py
```

---

# Características de la Interfaz Gráfica

La interfaz fue desarrollada utilizando Tkinter e incorpora:

* LabelFrame
* Entry
* Buttons
* Listbox
* Scrollbar
* Validación de datos
* Mensajes emergentes
* Gestión dinámica de registros

---

# Manejo de Conexión MySQL

El sistema implementa cierre correcto de conexión y cursor mediante:

```python
finally:
    cursor.close()
    conexion.close()
```

Esto permite liberar correctamente los recursos utilizados por MySQL.

---

# Autor

Proyecto desarrollado como práctica académica de programación en Python, interfaces gráficas y bases de datos relacionales.
