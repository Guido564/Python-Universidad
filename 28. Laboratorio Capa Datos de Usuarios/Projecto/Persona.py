from logger import log

class Persona:
    def __init__(self, idpersona=None, username=None, password=None):
        self._idpersona = idpersona
        self._username = username
        self._password = password
        
    def __str__(self):
        return f'''
                ID del usuario: {self._idpersona} 
                Nombre: {self._username} 
                Contrasenia: {self._password}
                '''
    
    @property
    def idpersona(self):
        return self._idpersona
    
    @idpersona.setter 
    def idpersona(self, idpersona):
        self._idpersona = idpersona
        
     
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
        
persona1 = Persona(1, "guido", "123")
log.debug(persona1)
        
        