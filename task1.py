import requests

class Superheroes:
    base_url = 'https://akabab.github.io/superhero-api/api'
    def get_all_superheroes(self):
        list_heroes = ["Hulk", "Captain America", "Thanos"]
        
        list_heroes_intelligence = []
        url_all = '/all.json'
        request_url = self.base_url + url_all
        response = requests.get(request_url)
        res = response.json()
        for hero in list_heroes:
            for heroes in res:
                if heroes['name'] == hero:
                    list_heroes_intelligence.append(heroes["powerstats"]["intelligence"])
                    print(f'{hero} {heroes["powerstats"]["intelligence"]}')
        max_value = max(list_heroes_intelligence)
        print()
        print(f'Самый умный супергерой: {max_value}')

if __name__ == '__main__':
    Sh = Superheroes()
    Sh.get_all_superheroes()