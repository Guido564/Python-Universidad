from usuario import Usuario
from usuarioDao import UsuarioDAO

def menu():
    while(True):
        try:
            print("1. Listar usuarios")
            print("2. Agregar usuario")
            print("3. Actualizar usuario")
            print("4. Eliminar usuario")
            print("5. Salir")
            print()
            
            c = int(input("Seleccione a continuacion que opcione le sienta mejor: "))
            if c == 1:
                UsuarioDAO.listar()
            elif c == 2:
                a = input("Ingrese el nuevo usuario: ")
                b = input("Ingrese la nueva password: ")
                nuevoUser = Usuario(username=a, password=b)
                UsuarioDAO.insertar(nuevoUser)
            elif c == 3:
                id = int(input('Identifique el usuario a modificar: '))
                a = input("Ingrese el nuevo usuario: ")
                b = input("Ingrese la nueva password: ")
                usuarioReconfig = Usuario(id, a, b)
                UsuarioDAO.actualizar(usuarioReconfig)
            elif c == 4:
                id = int(input('Identifique el usuario a eliminar: '))
                userDelete = Usuario(idusuario=id,)
                UsuarioDAO.eliminar(userDelete)
            elif c == 5:
                print("Adios gente")
                exit(0)
        except Exception:
            print("Eliga un caracter valido porque de otro modo programa boom")

menu()