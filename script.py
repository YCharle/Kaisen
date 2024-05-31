import random

class Player:
    
    def __init__(self, name, hp = 100):
        self.name = name
        self.hp = hp
        

    def __repr__(self):
        return "Welcome to Academia Kaisen {name}! You have {health} health points.".format(name=self.name, health=self.hp)
    
    def Answer_question(self):
        return answer_question()


    def gain_points(self):
        pass
    
    def heal(self):
        pass

    def attack(self):
        pass
    
player_1 = input("Player 1, input your name: ")
player_2 = input("Player 2, input your name: ")
p1 = Player(player_1)
p2 = Player(player_2)

list_of_players = []
if player_1 and player_2 != " ":
    list_of_players.append(player_1)
    list_of_players.append(player_2)
else:
    print("We need players to continue.")

if list_of_players != []:
    print("Welcome to Academia Kaisen! \n{Player1} your opponent is {Player2} \nThe game is simple. Each one of you will answer a question, starting with {Player1} \nYou both will add points to your total Health Points \nYou both also have Action Points which allow you to to heal \nand add to your Health Points and/or attack your opponent, \ndraining some of their Health Points \nLet's Begin!".format(Player1=list_of_players[0], Player2=list_of_players[1]))
else:
    print("We need players to continue.")


ks3_questions = {"Which of the following is not in an animal cell?\nCell Membrane\nCell Wall\nCytoplasm\nNucleus\n": "Cell wall", "Which of the folowing about veins is not true?\nSubstances cannot pass through their walls\nThey carry blood to the heart\nThey have no valves\nThey have thin walls\n": "They have no valves", "How many faces does a square-based pyramid have?\n": 5, "The earth is made up of how many layers?\n": 5, "What is the capital of Brazil?\n": "Brasilia", "Spell Synagogue\n": "Synagogue", "Spell Isosceles\n": "Isosceles", "What is the collective noun for a group of crows?\n": "Murder", "What is the plural of chief?": "Chiefs", "What is 15 times 17?\n": 255}

points = 0
p_points = 0
round_question = []

def answer_question():
    for i in range(20):
       question = random.choice(list(ks3_questions))
       if question in round_question:
           continue
       else:   
           print(question)
       round_question.append(question)
       ans = input("The answer is: ")
       


answer_question()
#print(points)      
#ask_answer("yaron")
#print(list_of_players)
#print(p1)
#print(p2)