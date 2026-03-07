# Supply Chain ETL Pipeline
![Status](https://img.shields.io/badge/STATUS-EN_DESARROLLO-yellow?style=for-the-badge)

Pipeline ETL construido en Python para procesar un dataset de Supply Chain.  
El proyecto sigue una arquitectura clásica **Bronze → Silver → Gold**, utilizando **Pandas** para las transformaciones y preparando las tablas Gold
para cargarlas en una base de datos (Supabase) y despues realizar un Dashboard interactivo.

## 🧱 Estructura del Pipeline

- **Bronze:** datos crudos en CSV.
- **Silver:** limpieza, estandarización y validaciones con Pandas.
- **Gold:** construcción de tablas finales (dimensiones y hechos) como DataFrames listos para subir a la base de datos.

## 📂 Organización del Proyecto (Actualmente)

```
Proyecto_Supply_Chain/
│
├── data/                        
│   ├── logs/                     
│   ├── raw/                 
│   └── silver/  
│
├── DB/                        
│   └── DER/                     
│
├── notebooks/                   
│   └── etl_notebook.ipynb
│
├── src/                         
│   ├── etl/
│   │   ├── extract/           
│   │   │   ├── __init__.py
│   │   │   └── extract_files.py         
│   │   │
│   │   ├── transform/         
│   │   │   ├── silver/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── cleaning.py    
│   │   │   │   ├── normalize.py     
│   │   │   │   └── validate.py     
│   │   │   │
│   │   │   └── gold/
│   │   │       ├── __init__.py
│   │   │       └── build.py
│   │   │ 
│   │   ├── load/                
│   │   │   ├── __init__.py
│   │   │   └── save_files.py    
│   │   │
│   │   └── pipelines/           
│   │       ├── __init__.py
│   │       └── pipeline.py
│   │   
│   └── utils/               
│       ├── __init__.py
│       └── logger.py
│               
├── requirements.txt
└── README.md

```

## ⚙ Tecnologías

- Python 3  
- Pandas    
- Supabase (PostgreSQL)
- Power BI

## 🚧 Estado

Proyecto en desarrollo.  
Actualmente implementado:
- Extracción desde CSV  
- Transformaciones Silver
- Validaciones Silver

Próximos pasos:
- Construcción de tablas Gold en Pandas  
- Validaciones Gold  
- Carga automática a Supabase  

## 📌 Objetivo

Crear un ETL modular, claro y fácil de mantener, con tablas Gold listas para análisis o BI.
