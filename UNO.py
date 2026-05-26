import flet as ft
import random

colors = ["Red", "Blue", "Green", "Yellow"]
values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip" , "+2"]

class card:
    def __init__(self, color, value):
         self.color = color
         self.value = value

    # check if card can be played
    def can_play(self, other):

        if self.color == other.color:
            return True

        if self.value == other.value:
            return True

        return False
    
    def __str__(self):

        return self.color + " " + self.value


class game:
    
    def __init__(self, page):
        self.page = page

        page.title = "UNO by Oliver, Leanned, Mia and Luisa"

        page.window_width = 1400
        
        page.window_height = 850

        page.bgcolor = "#1E1E1E"

        self.new_game()

        self.title_text = ft.Text("UNO", size=40, weight="bold", color="white",)

        self.top_card_text = ft.Text("", size=20, color="white",)

        self.ai_text = ft.Text("", size=20, color="white",)

        self.top_card_image = ft.Image(src=self.get_image_path(self.top_card), width=250, height=350, fit="contain",)

        self.player_cards_row = ft.Row(wrap=True, spacing=10, run_spacing=10, alignment="center",)#fdsijn

        self.draw_button = ft.Button(content=ft.Text("Draw Card", size=20, color="white",), width=200, height=60,on_click=self.draw_card_button,)
            
        self.restart_button = ft.Button(content=ft.Text("Restart", size=20, color="white",),width=200, height=60, on_click=self.restart_game,)
    
    def new_game(self):
        self.deck = []

        for color in colors:
            for value in values:
                self.deck.append(card(color,value))
                self.deck.append(card(color,value))#insdfjkm
        
        random.shuffle(self.deck)#fdnjic

        self.player_hand = []#sbfudhjni
        self.ai_hand = []

        for i in range(7):
            self.player_hand.append(self.draw_card())
            self.ai_hand.append(self.draw_card())
        
        self.top_card = self.draw_card()

    def draw_card(self):
        if len(self.deck) == 0:
            return None
        return self.deck.pop()#fdjsok
    
    def get_image_path(self, card): #dsinjkm
        value = card.value
        if value =="+2":
            value = "Draw_2"
        
        filename = (card.color + "_" + value + ".jpg")
        return "cards/" + filename
    
    def update_screen(self): #fgnuij
        self.top_card_text.value = ("Top Card: " + str(self.top_card))
        self.ai_text.value = ("AI has " + str(len(self.ai_hand))+ " cards")

        self.top_card_image.src = (self.get_image_path(self.top_card))
        self.player_cards_row.controls.clear()

        for index, card in enumerate(self.player_hand):#dsfuihj

            card_button = ft.Container(width=140, height=210, border_radius=15, ink=True,on_click=lambda e,i=index:self.play_card(i),content=ft.Image(src=self.get_image_path(card),fit="contain",),)#gdhufijo

            self.player_cards_row.controls.append(card_button)

        self.page.update()

    def play_card(self, index):#fsndijk
        chosen_card = (self.player_hand[index])#fsijndk

        # Invalid move
        if not chosen_card.can_play(self.top_card):
            self.show_message("Invalid move!")
            return

        
        self.player_hand.pop(index)#fsdjk
        self.top_card = chosen_card

        if chosen_card.value == "+2":
            for i in range(2):
                new_card = (self.draw_card())#gjfdn

                if new_card:
                    self.ai_hand.append(new_card)

 
        if chosen_card.value == "Skip":

            self.show_message("AI skipped!")

        if len(self.player_hand) == 0:
            self.show_message("YOU WIN!")
            self.restart_game(None)
            return
        
        self.update_screen()
        self.ai_turn()

        def draw_card_button(self, e):#fdgshjk
            new_card = self.draw_card()

            if new_card:
                self.player_hand.append(new_card)

            self.update_screen()

            self.ai_turn()

        def ai_turn(self):
            playable_cards = []

            for card1 in self.ai_hand:
                if card1.can_play(self.top_card):
                    playable_cards.append(card1)

        
        if len(playable_cards) > 0:
            chosen_card = random.choice(playable_cards)
            self.ai_hand.remove(chosen_card)
            self.top_card = chosen_card

            if chosen_card.value == "+2":
                for i in range(2):
                    new_card = self.draw_card()

                    if new_card:
                        self.player_hand.append(new_card)
            
            if chosen_card.value == "Skip":

                self.show_message("You skipped!")

            self.show_message("AI played "+ str(chosen_card))

            # ai win
            if len(self.ai_hand) == 0:
                self.show_message("AI WINS!")
                self.restart_game(None)
                return
            
        else: 
            new_card = self.draw_card()

            if new_card:
                self.ai_hand.append("AI drew a casd")
        
        self.update_screen()
        

        

                    


        

        




    
        
