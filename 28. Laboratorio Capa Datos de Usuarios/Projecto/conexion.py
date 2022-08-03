from logger import log
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = '0564'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None
    _MINCON = 1
    _MAXCON = 5
    _pool = None
    
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MINCON, cls._MAXCON,
                                                    host = cls._HOST,
                                                    user = cls._USERNAME,
                                                    password = cls._PASSWORD,
                                                    port = cls._DB_PORT,
                                                    database = cls._DATABASE)
                log.debug(f'La conexcion ha sido un exito y todo marcha bien: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error {e} capoeira, fijate bien que onda')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'La conexion del pool ha estado relativamente bien: {conexion}')
        return conexion
        
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Liberada la conexion correctamente: {conexion}')
        
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()