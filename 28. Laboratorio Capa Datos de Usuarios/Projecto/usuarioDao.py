from conexion import Conexion
from usuario import Usuario
from logger import log
import psycopg2


class UsuarioDAO:
    
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY idusuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SER username=%s, password=%s WHERE idusuario=%s'
    _DELETE = 'DELETE FROM usuario WHERE idusuario=%s'
    
    @classmethod
    def seleccionar(cls):
        cursor = Conexion.obtenerCursor()
        cursor.execute(cls._SELECCIONAR)
        registros = cursor.fetchall()
        usuarios = []
        for registro in registros:
            usuario = Usuario(registro[0], registro[1], registro[2])
            usuarios.append(usuario)
        return usuarios
        
usuarios = UsuarioDAO.seleccionar()
for usuario in usuarios:
    log.debug(usuario)
        