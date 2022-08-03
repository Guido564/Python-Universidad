from logger import log
from conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, tipoExc, valorExc, tbExc):
        if valorExc:
            self._conexion.rollback()
            log.error(f'Cagamo gente: {valorExc}, {tipoExc}, {tbExc}')
        else:
            self._conexion.commit()
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)