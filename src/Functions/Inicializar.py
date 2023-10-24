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
        User = "Sprint3@test.com"
        Password = "S3CR37"
        ProductNameCorrect = "VX"
        ProductNameIncorrect= "AAAAAA"
