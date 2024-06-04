import random

class Player:
     
    def __init__(self, name, hp = 100):
        self.name = name
        self.hp = hp
        self.p_points = 0
        
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
           # Prints the random question and sets the solution
           solution = ks3_questions[question]
           print(f"\n{self.name}, {question}")
           # Checks if the question has multiple options and sets the answer
           if type(ks3_questions[question]) is list:
            for i, answer in enumerate(ks3_questions[question]):
                print(f"{(i+1)}.- {answer[0]}")
                if answer[1]:
                    solution = f"{(i+1)}"
           seen_values.add(question)
           round_question.append(question)
         ans = input("Enter your answer: ")
         self.ans = ans
         #If the answer is an integer: Checks if the player entered a digit and sets the answer as int.
         if type(ks3_questions[question]) is int:
            if self.ans.isdigit():
                self.ans = int(self.ans)
         if self.ans == solution:
             self.gain_points()
             # Announces the result
             print('\nCorrect!\n')

    def gain_points(self):
        self.hp += 250
        self.p_points = self.p_points + (4 ** 4)

    
    def heal_attack(self, other_player):
        # Gets the player's answer and sets the input as lowercase with .lower()
        response = input(self.name + " you have " + str(self.p_points) + " action points, would you like to heal or attack?\n").lower()
        if response == 'heal':
            self.hp += self.p_points

        elif response == "attack":
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
    print("We need players to continue.\n")


ks3_questions = {
    "Which of the following is not in an animal cell?": [
        ["Cell Membrane", False],
        ["Cell Wall", True],
        ["Cytoplasm", False],
        ["Nucleus", False]
        ],
    "Which of the folowing about veins is not true?": [
        ["Substances cannot pass through their walls", False],
        ["They carry blood to the heart", False],
        ["They have no valves", True],
        ["They have thin walls", False]
        ],
    "How many faces does a square-based pyramid have?": 5,
    "The earth is made up of how many layers?": 5,
    "What is the capital of Brazil?": "Brasilia",
    "Spell Synagogue": "Synagogue",
    "Spell Isosceles": "Isosceles",
    "What is the collective noun for a group of crows?\n": "Murder",
    "What is the plural of chief?": "Chiefs",
    "What is 15 times 17?": 405,
    "What is the most suitable adjective to complete this sentence:\n 'This cake tastes horrible, but that one tastes...": [
        ["Horribler", False],
        ["Horrible", False],
        ["More horible", True],
        ["Most horrible", False]]
    }

round_question = []


p1.answer_question()
p2.answer_question()
p1.heal_attack(p2)
p2.heal_attack(p1)
p1.say_winner()
p2.say_winner()