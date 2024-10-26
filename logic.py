from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.moves = self.get_moves()

        self.hp = randint(150, 250)
        self.power = randint(30, 60)
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{self.pokemon_number}.png")
        else:
            return "Pikachu"

    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def get_moves(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['moves'][0]['move']['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}. Здоровье: {self.hp}, сила: {self.power}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def show_moves(self):
        return f'Первая способность - {self.moves}'

    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            shield = randint(1,5)
            if shield == 1:
                return "Покемон-волшебник применил щит в сражении"
            else:
                if enemy.hp > self.power:
                    enemy.hp -= self.power
                    return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
                else:
                    enemy.hp = 0
                    return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
        else:
            if enemy.hp > self.power:
                enemy.hp -= self.power
                return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
            else:
                enemy.hp = 0
                return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

class Wizard(Pokemon):
    def info(self):
        return 'У тебя покемон-волшебник'
        
class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        end = super().attack(enemy)
        self.power -= super_power
        return end + f"\nБоец применил супер-атаку силой:{super_power} "

    def info(self):
        return 'У тебя покемон-боец' + super().info(self)
