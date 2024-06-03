import random

class Player:
     
    def __init__(self, name, hp = 100):
        self.name = name
        self.hp = hp
        self.p_points = 0
        #self.op_points = self.points
        

    def __repr__(self):
        return "Welcome to Academia Kaisen {name}! You have {health} health points.".format(name=self.name, health=self.hp)
    
    def answer_question(self):
        for x in range(5):
         num_list = []
         num_list.append(x)
         seen_values = set()
         question = random.choice(list(ks3_questions))
         if question in round_question and x in num_list:
            continue
         else:   
           print(self.name + ", " + question)
           seen_values.add(question)
           #round_question.append(question)
         ans = input("The answer is: ")
         self.ans = ans
         if self.ans == ks3_questions[question]:
             self.gain_points()



    def gain_points(self):
        self.hp += 250
        self.p_points = self.p_points + (4 ** 4)

    
    def heal_attack(self, other_player):
        response = input(self.name + " you have " + str(self.p_points) + " action points, would you like to heal or attack?\n")
        if response == "Heal" or response == 'heal':
            self.hp += self.p_points

        elif response == "Attack" or response == "attack":
            other_player.take_damage(self.p_points)

        else:
            print("Make sure your response is spelt correctly")
        

    def take_damage(self, damage):
        self.hp -= damage

    def say_winner(self):
        print(self.name + " your final score is " + str(self.hp))
        
    
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
    print("\nWelcome to Academia Kaisen! \n{Player1} your opponent is {Player2} \nThe game is simple. Each one of you will answer a question, starting with {Player1} \nYou both will add points to your total Health Points \nYou both also have Action Points which allow you to to heal \nand add to your Health Points or attack your opponent, \ndraining some of their Health Points \nLet's Begin!".format(Player1=list_of_players[0], Player2=list_of_players[1]))
else:
    print("We need players to continue.")


ks3_questions = {"Which of the following is not in an animal cell?\nCell Membrane\nCell Wall\nCytoplasm\nNucleus\n": "Cell wall", "Which of the folowing about veins is not true?\nSubstances cannot pass through their walls\nThey carry blood to the heart\nThey have no valves\nThey have thin walls\n": "They have no valves", "How many faces does a square-based pyramid have?\n": 5, "The earth is made up of how many layers?\n": 5, "What is the capital of Brazil?\n": "Brasilia", "Spell Synagogue\n": "Synagogue", "Spell Isosceles\n": "Isosceles", "What is the collective noun for a group of crows?\n": "Murder", "What is the plural of chief?\n": "Chiefs", "What is 15 times 17?\n": 255, "What is the most suitable adjective to complete this sentence:\n 'This cake tastes horrible, but that one tastes....'\nHorribler\nHorrible\nMore horible\nMost horrible": "More horrible"}

round_question = []


p1.answer_question()
p2.answer_question()
p1.heal_attack(p2)
p2.heal_attack(p1)
p1.say_winner()
p2.say_winner()

#print(points)      
#ask_answer("yaron")
#print(list_of_players)
#print(p1)
#print(p2)