# 📊 Pipeline End-to-End: Análisis de Negocio y Cadena de Suministro

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white)
![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)


## 📝 Descripción General
Este proyecto demuestra la implementación de un pipeline completo (end-to-end) de ingeniería de datos e inteligencia de negocios. Transforma datos crudos y transaccionales de una cadena de suministro en insights estratégicos accionables a través de tres áreas clave del negocio: **Ventas (Sales)**, **Logística (Logistics)** y **Retención de Clientes (Customer Retention)**.

El pipeline utiliza una **Arquitectura Medallion** (Bronce, Plata, Oro) desarrollada en Python, persiste los datos estructurados en una base de datos relacional en la nube (**Supabase**) y se conecta a **Power BI** para el modelado semántico y la visualización interactiva.

Dataset: https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis

## 🛠️ Tecnologías y Arquitectura
* **Fuente de Datos:** Kaggle (Dataset DataCo Smart Supply Chain - formato CSV).
* **Procesamiento de Datos (ETL):** Python (Pandas) aplicando la Arquitectura Medallion:
    * 🥉 **Capa Bronce (Bronze):** Ingesta de datos crudos sin procesar.
    * 🥈 **Capa Plata (Silver):** Limpieza de datos, tratamiento de valores nulos y estandarización de formatos.
    * 🥇 **Capa Oro (Gold):** Agregaciones orientadas a métricas de negocio y modelado dimensional.
* **Base de Datos en la Nube:** Supabase (PostgreSQL) para un almacenamiento seguro y escalable.
* **Inteligencia de Negocios (BI):** Power BI Desktop (Modelado de Datos, UI/UX y Storytelling).

<img width="1536" height="1024" alt="arquitectura" src="https://github.com/user-attachments/assets/6d45453d-c2be-4ec5-8c55-75542b71d279" />

---

## 🗄️ Diseño de la Base de Datos (Modelo Dimensional)

Los datos procesados en la Capa Oro (Gold Layer) se estructuraron bajo un **Modelo de Estrella (Star Schema)** y se implementaron en Supabase (PostgreSQL). Este diseño está optimizado para cargas de trabajo analíticas, garantizando un alto rendimiento en las consultas de Power BI:

* **Tabla de Hechos (Fact Table):**
    * `fact_sales`: Contiene las métricas cuantitativas (ingresos, costos, tiempos de envío) y las llaves foráneas (Foreign Keys) que conectan con las dimensiones.
* **Tablas de Dimensiones (Dimension Tables):**
    * `dim_customer`: Atributos de los clientes (segmento, nombre, apellido, etc).
    * `dim_product`: Jerarquía del catálogo (categoría, nombre del producto, precio unitario, etc).
    * `dim_location`: Jerarquía espacial para envíos (mercado, región, país, etc).
    * `dim_calendar`: Dimensión de fechas generada para soportar análisis de inteligencia de tiempo (tendencias interanuales y variaciones mensuales).

---

## 🖥️ Resumen de las Páginas del Dashboard

1.  **Ventas (Sales):** Monitorea la salud financiera general, comparando ingresos y ganancias por segmento, e identificando las categorías de productos de mayor rendimiento.

![dashboard_page-0001](https://github.com/user-attachments/assets/6d6ac527-b738-4b87-a6b3-3cfd001c503d)

2.  **Logística (Logistics):** Profundiza en el 57% de entregas tardías, analizando los retrasos por método de envío, mercado geográfico y categoría de producto para aislar la causa raíz del cuello de botella.

![dashboard_page-0002](https://github.com/user-attachments/assets/78905390-51be-44b1-bccb-679ff6bc5a12)

3.  **Clientes (Customers):** Se enfoca en el comportamiento del usuario, mostrando la tendencia anual de tráfico y analizando la frecuencia de compra.

![dashboard_page-0003](https://github.com/user-attachments/assets/15118b72-0103-4e1b-a4cf-193f457044ae)

---

## 📂 Cómo explorar este proyecto

En este repositorio encontrarás todo el código que respalda la arquitectura de datos, así como el resultado final interactivo:

* **`/src`:** Contiene los scripts de Python donde se realizó el proceso ETL y la estructuración de la Arquitectura Medallion.
* **`/database`:** Scripts de creación de tablas y diseño del Modelo de Estrella para Supabase (PostgreSQL).
* **`/powerbi`:** Archivo de Power BI y creacion de canvas background. Puedes descargarlo y abrirlo con Power BI Desktop para interactuar con los datos y explorar el modelo semántico.

---

## 📬 Contacto
Creado por **Marco Ortega** | Data Analyst / Analytics Engineer  
🔗 [LinkedIn](https://www.linkedin.com/in/ortegamarco03/) | 💻 [Portfolio](https://portfolio-ortega-marco.vercel.app/)
