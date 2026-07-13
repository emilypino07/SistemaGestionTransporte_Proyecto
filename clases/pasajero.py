# ============================================================
# INTEGRANTES
# ============================================================
# - ALVAREZ YAGUAL KAREN
# - MACIAS VILLAMAR MARCOS
# - PINO LOOR EMILY
# - RODRIGUEZ CRESPIN DIDDIER
# - VASQUEZ CHILA VALERIA
# ============================================================
#CLASE PASAJERO

class Pasajero:
    """
    Clase que representa un pasajero dentro del sistema.
    Aplica encapsulamiento utilizando atributos privados,
    property y setter.
    """

    def __init__(self,
                 cedula: str,
                 nombre: str,
                 apellido:str,
                 email:str
                 ):
        #ATRIBUTOS PRIVADOS
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.email = email


    #ENCAPSULAMIENTOS
    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, nueva_cedula):
        if nueva_cedula.strip() == "":
            raise ValueError("La cedula no puede estar vacia")
        if not nueva_cedula.isdigit() or len(nueva_cedula) != 10:
            raise ValueError("La cedula debe tener 10 digitos numericos")
        self.__cedula = nueva_cedula


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")
        if not nuevo_nombre.replace(" ", "").isalpha():
            raise ValueError("El nombre solo puede contener letras")
        self.__nombre = nuevo_nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, nuevo_apellido):
        if nuevo_apellido.strip() == "":
            raise ValueError(
                "El apellido no puede estar vacio"
            )

        if not nuevo_apellido.replace(" ", "").isalpha():
            raise ValueError(
                "El apellido solo puede contener letras"
            )

        self.__apellido = nuevo_apellido

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nuevo_email):

        if nuevo_email.strip() == "":
            raise ValueError(
                "El email no puede estar vacio"
            )

        if "@" not in nuevo_email or "." not in nuevo_email:
            raise ValueError(
                "Email invalido"
            )

        self.__email = nuevo_email
    #METODOS
    def mostrar_datos(self):

        print("\n--- PASAJERO ---")
        print(f"Cedula: {self.__cedula}")
        print(f"Nombre: {self.__nombre} {self.__apellido}")
        print (f"Email: {self.__email}")

    #STR
    def __str__(self):
        return (
            f"Cedula: {self.__cedula} | "
            f"Nombre: {self.__nombre} {self.__apellido} | "
            f"Email: {self.__email}"
        )
