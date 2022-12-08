import json
import requests
from pathlib import Path

class Camara_Deputados_API:
    def __init__(self):
        self.url_default = "https://dadosabertos.camara.leg.br/api/v2/"
    
    def _get(self, endpoint, params=None):
        if params is None:
            params = {}
        
        url = self.url_default + endpoint
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
        
    def get_all(self, endpoint, params=None):
        if params is None:
            params = {}
            
        params["itens"] = 100
        params["pagina"] = 1
        data = []
        
        while True:
            has_more = False
            response = self._get(endpoint, params)
            data += response["dados"]
            
            for link in response["links"]:
                if link["rel"] == "next":
                    has_more = True
                    params["pagina"] += 1
                    continue
            
            if not has_more:
                break

        return data

    def save_json(self, name, json_file):
        json_object = json.dumps(json_file, indent=4, ensure_ascii=False)
        path = "data/api_files"

        with open(Path(f"{path}/{name}.json"), "w") as outfile:
            outfile.write(json_object)
        
    def get_all_deputados(self):
        json_data = self.get_all("deputados")
        self.save_json("deputados", json_data)
    
    def get_all_partidos(self):
        json_data = self.get_all("partidos")
        self.save_json("partidos", json_data)
    
    def get_all_proposicoes(self):
        json_data = self.get_all("proposicoes")
        self.save_json("proposicoes", json_data)
    
    def extract_all(self):
        self.get_all_deputados()
        self.get_all_proposicoes()
        self.get_all_partidos()
    
