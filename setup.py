from setuptools import setup, find_packages 

setup(
    name = "sqldb_connect", 
    version = "0.0.1", 
    description = "A connector tool for PgSQL database accessed through SSH tunnel.", 
    url = "https://github.com/data-components/remote_sqldb_connector", 
    author = "Loann Brahimi", 
    author_email = "loann.datasciences@gmail.com", 
    license = "MIT", 
    zip_safe = False, 
    requires = ["psycopg2", "sqlalchemy", "sshtunnel"] 
)