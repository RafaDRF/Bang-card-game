class Card:
    def __init__(self, value, club):
        self.value = value
        self.club = club
    
    def __str__(self):
        return f"{self.value} {self.club}"


class Deck:
    def __init__(self, discart):
        self.cards = []
        if not discart:
            self.build()
    
    def build(self):
        value = 14
        club = ["♥","♦","♣","♠"]
        for v in range(1,value):
            for c in club:
                self.cards.append(Card(v, c)) 
    
    def show(self):
        for c in self.cards:
            print(c)
    
    def draw(self):
        return self.cards.pop()
    
    def pull(self, card):
        self.cards.append(card)


class Player:
    def __init__(self, id, craft, character_id):
        self.id = id
        self.craft = craft
        self.character = Character(character_id)
        self.hand = []
        self.board = []
    
    def show_hand(self):
        i = 1
        for c in self.hand:
        print(i, end="")
        print(" : ", end="")
        print(c)
        i += 1
        
    def draw(self, deck):  
        self.hand.append(deck.draw())
    
    def discart(self, index):
        return self.hand.pop(index)


class Character:
    def __init__(self, id):
        self.id = id

class Bang:
    def __init__(self, players_amount):
        self.players_amount = players_amount
        self.players = []
        craft_distribute()
        character_distribute()                                                                                                                                                                                                                                                                                                                                                                                                            
    
    def init(self, ):
        craft = ["outLaw", "renegade", "sheriff", "vice"]                                                                                                                                                                                                                                                                                                                                                                                     
        
        for i in range(1, self.players_amount+1):                                                                                                                                                                              
            self.players.append(Player(i, craft[i]),)
        
        
       
