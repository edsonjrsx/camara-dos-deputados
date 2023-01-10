import requests
from pathlib import Path


class Camara_Deputados_Extrator:
    def __init__(self) -> None:
        self.url_base = "http://dadosabertos.camara.leg.br/arquivos/"
    
    def extract_table(self, name, append=False, year=None):
        if year:
            url = f'{self.url_base}/{name}/csv/{name}-{year}.csv'
        else:
            url = f'{self.url_base}/{name}/csv/{name}.csv'
            
        r = requests.get(url, allow_redirects=True)
        path = "data/extrator_files"
        if append:
            content = r.content[r.content.find(b'\n')+1:]
            open(Path(f'{path}/{name}.csv'), 'ab').write(content)
        else:
            open(Path(f'{path}/{name}.csv'), 'wb').write(r.content)
    
    def extract_table_by_year(self, name, start_year=2019, end_year=2022):
        for year in range(start_year, end_year+1):
            if year == start_year:
                append = False
            else:
                append = True
                
            self.extract_table(
                name=name,
                append=append,
                year=year,
            )
    
    def extract_table_by_legislature(self, name, legislature):
        self.extract_table(name=name, append=False, year=legislature)
    
    def get_deputados(self):
        self.extract_table(name='deputados')
        print("Deputados extraídos com sucesso!")
           
    def get_deputados_profissoes(self):
        self.extract_table(name='deputadosProfissoes')
        print("Profissões dos deputados extraídas com sucesso!")
    
    def get_legislaturas(self):
        self.extract_table(name='legislaturas')
        print("Legislaturas extraídas com sucesso!")
    
    def get_orgaos(self):
        self.extract_table(name='orgaos')
        print("Órgãos extraídos com sucesso!")
        
    def get_orgaos_deputados(self, legislature='L56'):
        self.extract_table_by_legislature(name='orgaosDeputados', legislature=legislature)
        print("Relação órgão/deputados extraídas com sucesso!")
        
    def get_frentes_parlamentares(self):
        self.extract_table(name='frentes')
        print("Frentes parlamentares extraídas com sucesso!")
    
    def get_frentes_deputados(self):
        self.extract_table(name='frentesDeputados')
        print("Relação frentes/deputados extraídas com sucesso!")

    def get_eventos(self, start_year, end_year):
        self.extract_table_by_year(name='eventos',
                                   start_year=start_year,
                                   end_year=end_year
                                )
        print(f"Eventos entre {start_year}-{end_year} extraídos com sucesso!")
        
    def get_eventos_presenca_deputados(self, start_year, end_year):
        self.extract_table_by_year(name='eventosPresencaDeputados',
                                   start_year=start_year,
                                   end_year=end_year
                                )
        print(f"Presenca em eventos entre {start_year}-{end_year} extraídos com sucesso!")
    
    def get_proposicoes(self, start_year, end_year):
        self.extract_table_by_year(name='proposicoes',
                                   start_year=start_year,
                                   end_year=end_year
                                )
        print(f"Proposições entre {start_year}-{end_year} extraídas com sucesso!")
    
    def get_proposicoes_temas(self, start_year, end_year):
        self.extract_table_by_year(name='proposicoesTemas',
                                   start_year=start_year,
                                   end_year=end_year
                                )
        print(f"Classificação das proposições entre {start_year}-{end_year} extraídas com sucesso!")
        
    def get_proposicoes_autores(self, start_year, end_year):
        self.extract_table_by_year(name='proposicoesAutores',
                                   start_year=start_year,
                                   end_year=end_year
                                )
        print(f"Autores das proposições entre {start_year}-{end_year} extraídas com sucesso!")
        
    def get_votacoes(self, start_year, end_year):
        self.extract_table_by_year(name='votacoes',
                                   start_year=start_year,
                                   end_year=end_year
                                )
        print(f"Votações entre {start_year}-{end_year} extraídas com sucesso!")
    
        
    def get_votacoes_orientacao_partido(self, start_year, end_year):
        self.extract_table_by_year(name='votacoesOrientacoes',
                                   start_year=start_year,
                                   end_year=end_year
                                )
        print(f"Orientações partidos votações entre {start_year}-{end_year} extraídas com sucesso!")
    
    
    def get_votacoes_deputados(self, start_year, end_year):
        self.extract_table_by_year(name='votacoesVotos',
                                   start_year=start_year,
                                   end_year=end_year
                                )
        print(f"Votos dos deputados entre {start_year}-{end_year} extraídas com sucesso!")
    
    
    def extract_all(self, start_year, end_year):
        self.get_deputados()
        self.get_deputados_profissoes()
        self.get_legislaturas()
        self.get_orgaos()
        self.get_orgaos_deputados(legislature='L56')
        self.get_frentes_parlamentares()
        self.get_frentes_deputados()
        self.get_eventos(start_year=start_year, end_year=end_year)
        self.get_eventos_presenca_deputados(start_year=start_year, end_year=end_year)
        self.get_proposicoes(start_year=start_year, end_year=end_year)
        self.get_proposicoes_temas(start_year=start_year, end_year=end_year)
        self.get_proposicoes_autores(start_year=start_year, end_year=end_year)
        self.get_votacoes(start_year=start_year, end_year=end_year)
        self.get_votacoes_orientacao_partido(start_year=start_year, end_year=end_year)
        self.get_votacoes_deputados(start_year=start_year, end_year=end_year)
        
