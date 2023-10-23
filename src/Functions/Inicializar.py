import os

class Inicializar():
    """Directorio Base"""
    basedir = os.path.abspath(os.path.join(__file__, "../../"))
    
    DateFormat = "%d/%m/&Y"
    HourFormat = "%H%M%S"
    
    """JsonData"""
    Json = basedir + "/Pages"
    
    Environment = "Dev"
    NAVEGADOR = 'CHROME'
    Path_evidencias = basedir + '/Data/Evidencia'
    
    if Environment == "Dev":
        URL = "https://shop.thonet-vander.com/"
        User = "hola.rogallardo@gmail.com"
        Password = "Formula1!"
        ProductName = "xv75"