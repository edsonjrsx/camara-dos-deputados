import sys
from raw.extrator import Camara_Deputados_Extrator
from src.raw.api import Camara_Deputados_API

if __name__ == "__main__":
    
    if len(sys.argv) <= 2:
        print('Argumentos insuficientes, passe o ano inicial e o ano final que deseja extrair.')
        sys.exit()

    ini_date = sys.argv[1]
    end_date = sys.argv[2]
    
    Camara_Deputados_Extrator().extract_all(ini_date, end_date)
    Camara_Deputados_API().extract_all()