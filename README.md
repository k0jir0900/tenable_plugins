# Tenable Plugins Data Retriever

Este proyecto está diseñado para recuperar datos de plugins desde la API de Tenable y guardarlos en un archivo CSV.

## Descripción

El script realiza solicitudes a la API de Tenable para obtener información sobre los plugins. Los datos se guardan en archivos JSON temporales y luego se combinan en un archivo CSV final.

## Requisitos

- La herramienta `jq` instalada en tu sistema
- Claves de API de Tenable

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/k0jir0900/tenable_plugins.git
    cd tenable_plugins
    ```
2. Instalación `JQ`:
    - En Debian/Ubuntu:
      ```bash
      sudo apt-get install jq
      ```
## Uso

1. Define las claves de la API de Tenable en el script:
    ```python
    ACCESS_KEY = 'tu_access_key'
    SECRET_KEY = 'tu_secret_key'
    ```

2. Ejecuta el script:
    ```bash
    python3 plugins_download.py
    ```

3. El archivo CSV se generará con un nombre como `plugins_tenable-YYYYMMDD.csv`, donde `YYYYMMDD` es la fecha actual.

## Funcionamiento

1. El script realiza solicitudes a la API de Tenable, paginando los resultados.
2. Los datos obtenidos se guardan en archivos JSON temporales.
3. Una vez completada la obtención de datos, los archivos JSON se combinan en un archivo CSV usando `jq`.
4. Los archivos JSON temporales se eliminan al finalizar el proceso.

## Notas

- Asegúrate de que las claves de la API sean correctas y tengan los permisos necesarios.
- El tamaño de la página (`SIZE`) y el número de página inicial (`PAGE`) pueden ajustarse según sea necesario.
