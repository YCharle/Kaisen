class Player:
    
    def __init__(self, name, hp = 100):
        self.name = name
        self.hp = hp

    def __repr__(self):
        return "Welcome to Academia Kaisen {name}! You have {health} health points.".format(name=self.name, health=self.hp)
    
    def gain_points(self):
        pass
    
    
player_1 = input("Player 1, input your name: ")
player_2 = input("Player 2, input your name: ")
p1 = Player(player_1)
p2 = Player(player_2)

list_of_players = []
if player_1 and player_2 != None:
    list_of_players.append(player_1)
    list_of_players.append(player_2)
    print(p1)
    print(p2)
else:
    print("We need players to continue.")

if list_of_players != []:
    print("{Player1} your opponent is {Player2} and visa versa".format(Player1=list_of_players[0], Player2=list_of_players[1]))
else:
    print("We need players to continue.")


ks3_questions = {"Which of the following is not in an animal cell?\nCell Membrane\nCell Wall\nCytoplasm\nNucleus": "Cell wall", "Which of the folowing about veins is not true?\nSubstances cannot pass through their walls\nThey carry blood to the heart\nThey have no valves\nThey have thin walls": "They have no valves", "How many faces does a square-based pyramid have?": 5, "The earth is made up of how many layers?": 5, "What is the capital of Brazil?": "Brasilia", "Spell Synagogue": "Synagogue", "Spell Isosceles": "Isosceles", "What is the collective noun for a group of crows?": "Murder", "What is the plural of chief?": "Chiefs", "What is 15 times 17?": 255}
#print(list_of_players)
#print(p1)
#print(p2)