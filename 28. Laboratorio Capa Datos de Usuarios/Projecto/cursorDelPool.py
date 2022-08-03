from logger import log
from conexion import Conexion

class cursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del metodo enter')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, tipoExc, valorExc, tbExc):
        log.debug('Se ejecuta el metodo exit')
        if valorExc:
            self._conexion.rollback()
            log.error(f'Cagamo gente: {valorExc}, {tipoExc}, {tbExc}')
        else:
            self._conexion.commit()
            log.debug('Ha salido todo bien')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)