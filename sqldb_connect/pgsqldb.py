import psycopg2
from sqlalchemy import URL, create_engine
from sshtunnel import SSHTunnelForwarder

class PgSQLDb: 

    def __init__(self): 

        self.server = None 
        self.conn   = None 

        return 
    
    def connect_ssh(
            self,
            remote_host         = None, 
            remote_ssh_port     = 22, 
            remote_username     = None, 
            remote_password     = None, 
            remote_bind_address = "127.0.0.1", 
            remote_bind_port    = 5432, 
            local_bind_address  = "127.0.0.145", 
            local_bind_port     = 12345): 
        """
        """
        self.server = SSHTunnelForwarder(
            (remote_host, remote_ssh_port), 
            ssh_username = remote_username, 
            ssh_password = remote_password, 
            remote_bind_address = (remote_bind_address, remote_bind_port), 
            local_bind_address  = (local_bind_address, local_bind_port))
        self.server.start()
        return 
    
    def connect_database(
            self, 
            database_name = None, 
            database_user = "postgres", 
            database_pwd  = None, 
            local_host_address = "127.0.0.1", 
            local_host_port    = 5432, 
            sqlalchemy = True):
        
        if self.server is not None: 
            if sqlalchemy: 
                url_object = URL.create(
                    "postgresql", 
                    username = database_user, 
                    password = database_pwd, 
                    host = self.server.local_bind_host, 
                    port = self.server.local_bind_port, 
                    database = database_name)
                self.conn = create_engine(url_object)
                
            else: 
                self.conn = psycopg2.connect(
                    database = database_name, 
                    user = database_user, 
                    password = database_pwd, 
                    host = self.server.local_bind_host, 
                    port = self.server.local_bind_port)
        
        else: 
            self.conn = psycopg2.connect(
                database = database_name, 
                user = database_user, 
                password = database_pwd, 
                host = local_host_address, 
                port = local_host_port)
        
        return self.conn 