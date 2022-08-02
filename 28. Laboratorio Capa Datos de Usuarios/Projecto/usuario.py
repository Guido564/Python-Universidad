from logger import log

class Usuario:
    def __init__(self, idusuario=None, username=None, password=None):
        self._idusuario = idusuario
        self._username = username
        self._password = password
        
    def __str__(self):
        return f'''
                ID del usuario: {self._idusuario} 
                Nombre: {self._username} 
                Contrasenia: {self._password}
                '''
    
    @property
    def idusuario(self):
        return self._idusuario
    
    @idusuario.setter 
    def idusuario(self, idusuario):
        self._idusuario = idusuario
        
     
    @property
    def username(self):
        return self._username
    
    @username.setter 
    def username(self, username):
        self._username = username
        
    @property
    def password(self):
        return self._password
    
    @password.setter 
    def password(self, password):
        self._password = password

        
        