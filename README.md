# geoconnect
Simple script written in python to connect a PostGIS database and a Geoserver instance

## run

To run on your machine, use the  script.

```sh
python publish_database.py [database_name]

python publish_database.py -h
```

The following environment variables are required.

* `GEOSERVER_URL`Geoserver Address, with port (e.g. http://172.19.0.4:8080/geoserver/)
* `POSTGRES_URL` Database Address (e.g. 172.19.0.2)
* `POSTGRES_PORT` Database Port (e.g. 5432)
* `POSTGRES_USER`  Database user (e.g. geonetwork)
* `POSTGRES_PW` Database password (e.g. geonetwork)
* `LAB_NAME` Laboratory name (e.g. LabTeste)
* `LAB_URI` Laboratory URI (e.g. www.tbrd.dpi.br/LabTeste)
