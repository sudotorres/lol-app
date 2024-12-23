import requests

class DataDragon:
    def __init__(self):
        self.version_url = 'https://ddragon.leagueoflegends.com/api/versions.json' 
        self.champions_list_url = 'https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json'
        self.individual_champion_url =  'https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion/{name}.json'

    def get_version(self):
        response = requests.get(self.version_url)
        return response.json()[0]
    
    def get_champions_list(self, version):
        response = requests.get(self.champions_list_url.format(version=version))
        return response.json()['data']

    def get_champion_data(self, version, name):
        response = requests.get(self.individual_champion_url.format(version=version, name=name))
        return response.json()['data'][name]