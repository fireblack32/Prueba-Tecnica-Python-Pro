class DevelopmentConfig(): #Configuracion de desarrollo
    #conexion con MySQL
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '1234'
    MYSQL_DB = 'base_de_datos'
#Diccionario
config = {  
    'development': DevelopmentConfig
}