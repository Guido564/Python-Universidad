from usuario import Usuario
from logger import log
from cursorDelPool import CursorDelPool



class UsuarioDAO:
    
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY idusuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE idusuario=%s'
    _DELETE = 'DELETE FROM usuario WHERE idusuario=%s'

    @classmethod
    def listar(cls):
        with CursorDelPool() as cursor:
            sentencia = 'SELECT * FROM usuario'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
    
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a aniadir: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario aniadido: {usuario}')
            return cursor.rowcount
            
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.idusuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.idusuario,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'Usuario eliminado: {usuario}')
            return cursor.rowcount