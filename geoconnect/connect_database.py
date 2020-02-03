import os
import argparse
from geoserver.catalog import Catalog

#env
def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

#get env
GEOSERVER_URL = get_env_variable("GEOSERVER_URL")
LAB_NAME = get_env_variable("LAB_NAME")
LAB_URI = get_env_variable("LAB_URI")
POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_PORT = get_env_variable("POSTGRES_PORT")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")

#connect databse function
def connect_database( database_name ):

    #connect catalog
    cat = Catalog(GEOSERVER_URL + '/rest')

    #create workspace
    ws = cat.create_workspace(LAB_NAME, LAB_URI)

    #create datastore
    ds = cat.create_datastore(LAB_NAME+'_Datastore', LAB_NAME)

    #connect database
    ds.connection_parameters.update(host=POSTGRES_URL, port=POSTGRES_PORT, database=database_name, user=POSTGRES_USER, passwd=POSTGRES_PW, dbtype='postgis', schema='public')

    #save
    cat.save(ds)

#parse argument
parser = argparse.ArgumentParser()
parser.add_argument("database_name", help="connect the given database")
args = parser.parse_args()

#connect
connect_database(args.database_name)
