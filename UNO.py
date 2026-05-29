import flet as ft
import flet_audio as fta
import random

colors = ["Red", "Blue", "Green", "Yellow"]
values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip" , "+2"]

class card:
    def __init__(self, color, value):
         self.color = color
         self.value = value
        
    def can_play(self, other):

        if self.color == other.color:
            return True

        if self.value == other.value:
            return True

        return False
    
    def __str__(self):

        return self.color + " " + self.value


class game:
    
    def __init__(self, page, mode):
        self.page = page
        self.mode = mode
        self.current_player = 1
   
        self.page.controls.clear()

        page.title = "UNO by Oliver, Leanned, Mia and Luisa"

        page.window_width = 1400
        
        page.window_height = 850

        page.bgcolor = "#1E1E1E"

        self.new_game()

        self.title_text = ft.Text("UNO Saint Tropez", size=40, weight="bold", color="white",)
        
        self.top_card_text = ft.Text("", size=20, color="white",)
        self.turn_text = ft.Text("", size=22, color="white")

        self.ai_text = ft.Text("", size=20, color="white",)

        self.top_card_image = ft.Image(src=self.get_image_path(self.top_card), width=250, height=350, fit="contain",)
        self.player_cards_row = ft.Row(wrap=True, spacing=10, run_spacing=10, alignment="center",)#fdsijn

        self.draw_button = ft.Button(content=ft.Text("Draw Card", size=20, color="white",), width=200, height=60,on_click=self.draw_card_button,)
            
        self.restart_button = ft.Button(content=ft.Text("Restart", size=20, color="white",),width=200, height=60, on_click=self.restart_game,)

        

        self.songs = [

            {
                "src": "music/Future - WAIT FOR U (Instrumental) ft. Drake, Tems.mp3",
            },

            {
                "src": "music/SZA - Good Days (Instrumental).mp3",
            },

            {
                "src": "music/SZA - Snooze (Instrumental (Audio)).mp3",
            },
        ]

        self.song_index = 0

        self.audio = fta.Audio(
        src=self.songs[self.song_index]["src"],
        autoplay=True,
        volume=0.5,
    )

        self.page.add(self.audio)

        self.is_muted = False

        self.next_button = ft.IconButton(
            icon=ft.Icons.SKIP_NEXT,
            icon_color="white",
            icon_size=35,
            on_click=self.next_song,
        )

        self.mute_button = ft.IconButton(
            icon=ft.Icons.VOLUME_UP,
            icon_color="white",
            icon_size=35,
            on_click=self.toggle_mute,
        )


        page.add(
            ft.Row(controls=[ft.Column(controls=[self.title_text, self.turn_text, self.top_card_text, self.ai_text, self.top_card_image,
                                ft.Text(
                                    "YOUR CARDS",
                                    size=30,
                                    color="white",
                                ),

                                self.player_cards_row,
                            ],

                            horizontal_alignment="center",
                            spacing=20,
                            expand=True,
                        ),

                        ft.Container(

                            content=ft.Column(

                                controls=[

                                    self.draw_button,
                                    self.restart_button,

                                    ft.Container(height=50),

                                ],

                                horizontal_alignment="center",
                                spacing=25,
                            ),

                            padding=ft.Padding.only(right=40, top=120),
                        ),
                    ],

                    expand=True,
                    alignment="spaceBetween",
                    vertical_alignment="start",
                )
            )
        self.update_screen()

    def new_game(self):
        self.deck = []

        for color in colors:
            for value in values:
                self.deck.append(card(color,value))
                self.deck.append(card(color,value))#insdfjkm
        
        random.shuffle(self.deck)#fdnjic

        self.player1_hand = []
        self.player2_hand = []

        for i in range(7):
            self.player1_hand.append(self.draw_card())
            self.player2_hand.append(self.draw_card())
        
        self.top_card = self.draw_card()

    def draw_card(self):
        if len(self.deck) == 0:
            return None
        return self.deck.pop()#fdjsok
    
    def get_current_hand(self):

        if self.current_player == 1:
            return self.player1_hand

        return self.player2_hand
        
    def switch_turn(self):

        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    
    def get_image_path(self, card): #dsinjkm
        value = card.value
        if value =="+2":
            value = "Draw_2"
        
        filename = (card.color + "_" + value + ".jpg")
        return "cards/" + filename
    
    def update_screen(self): #fgnuij
        self.top_card_text.value = ("Top Card: " + str(self.top_card))
        if self.mode == "ai":
            self.ai_text.value = ("AI has " + str(len(self.player2_hand)) + " cards")
        else:
            self.ai_text.value = ("Player 2 has " + str(len(self.player2_hand)) + " cards")

        self.top_card_image.src = (self.get_image_path(self.top_card))
        self.player_cards_row.controls.clear()

        current_hand = self.get_current_hand()

        for index, card in enumerate(current_hand):#sfdnjkm

            card_button = ft.Container(width=140, height=210, border_radius=15, ink=True,on_click=lambda e,i=index:self.play_card(i),content=ft.Image(src=self.get_image_path(card),fit="contain",),)#gdhufijo

            self.player_cards_row.controls.append(card_button)

        self.page.update()

    def play_card(self, index):#fsndijk
        hand = self.get_current_hand()
        chosen_card = hand[index]
        if not chosen_card.can_play(self.top_card):
            self.show_message("Invalid move!")
            return

        
        hand.pop(index)#fsdjk
        self.top_card = chosen_card

        if chosen_card.value == "+2":#sdnjfik
            for i in range(2):
                new_card = (self.draw_card())#gjfdn

                if new_card:
                    if chosen_card.value == "+2":
                        target_hand = (
                            self.player2_hand
                            if self.current_player == 1
                            else self.player1_hand
                        )

                        for i in range(2):

                            new_card = self.draw_card()

                            if new_card:
                                target_hand.append(new_card)

 
        if chosen_card.value == "Skip":

            self.show_message("AI skipped!")

        if len(hand) == 0:
            self.show_message("YOU WIN!")
            self.restart_game(None)
            return
        
        self.switch_turn()

        self.update_screen()

        if self.mode == "ai" and self.current_player == 2:
            self.ai_turn()

    def draw_card_button(self, e):

        hand = self.get_current_hand()

        new_card = self.draw_card()

        if new_card:
            hand.append(new_card)

        self.switch_turn()

        self.update_screen()

        if self.mode == "ai" and self.current_player == 2:
            self.ai_turn()

    def ai_turn(self):
            playable_cards = []

            for card1 in self.player2_hand:
                if card1.can_play(self.top_card):
                    playable_cards.append(card1)

        
            if len(playable_cards) > 0:
                chosen_card = random.choice(playable_cards)
                self.player2_hand.remove(chosen_card)
                self.top_card = chosen_card

                if chosen_card.value == "+2":
                    for i in range(2):
                        new_card = self.draw_card()

                        if new_card:
                            self.player1_hand.append(new_card)
                
                if chosen_card.value == "Skip":

                    self.show_message("You skipped!")

                self.show_message("AI played "+ str(chosen_card))

                
                if len(self.player2_hand) == 0:
                    self.show_message("AI WINS!")
                    self.restart_game(None)
                    return
                
            else:
                new_card = self.draw_card()
                if new_card:
                    self.player2_hand.append(new_card)
                    self.show_message("AI drew a card")
            self.switch_turn()
            self.update_screen()

    def restart_game(self, e):
        self.new_game()
        self.update_screen()
        
    def show_message(self, text):
        
        self.page.snack_bar = ft.SnackBar(content=ft.Text(text))

        self.page.snack_bar.open = True

        self.page.update()


    def next_song(self, e):
        self.song_index += 1

        if self.song_index >= len(self.songs):
            self.song_index = 0

        self.audio.src = self.songs[self.song_index]["src"]

        self.audio.play()

        self.page.update()
    
    def toggle_mute(self, e):

        self.is_muted = not self.is_muted

        if self.is_muted:

            self.audio.volume = 0

            self.mute_button.icon = ft.Icons.VOLUME_OFF

        else:

            self.audio.volume = 0.5

            self.mute_button.icon = ft.Icons.VOLUME_UP

        self.page.update()

def show_menu(page):

    page.controls.clear()

    title = ft.Text(
        "UNO Saint Tropez",
        size=40,
        weight="bold",
    )

    play_button = ft.Button(
        content=ft.Text("Start Game"),
        on_click=lambda e: show_mode_selection(page),
    )

    instructions_button = ft.Button(
        content=ft.Text("Instructions"),
        on_click=lambda e: show_instructions(page),
    )

    layout = ft.Column(
        controls=[
            title,
            play_button,
            instructions_button,
        ],

        alignment="center",
        horizontal_alignment="center",
        spacing=20,
    )

    page.add(layout)

    page.update()



def show_instructions(page):

    page.controls.clear()

    title = ft.Text(
        "Instructions",
        size=30,
        weight="bold",
    )

    text = ft.Text(
        "- Match color or number.\n\n"
        "- Draw if you can't play.\n\n"
        "- Skip skips the next turn.\n\n"
        "- +2 makes opponent draw 2 cards.\n\n"
        "- First player with 0 cards wins.",
        size=18,
    )

    back_button = ft.Button(
        content=ft.Text("Back"),
        on_click=lambda e: show_menu(page),
    )

    layout = ft.Column(
        controls=[
            title,
            text,
            back_button,
        ],

        alignment="center",
        horizontal_alignment="center",
        spacing=20,
    )

    page.add(layout)

    page.update()


def show_mode_selection(page):

    page.controls.clear()

    title = ft.Text(
        "Select Game Mode",
        size=30,
        weight="bold",
    )

    ai_button = ft.Button(
        content=ft.Text("1 Player vs AI"),
        bgcolor="red",
        color="white",
        on_click=lambda e: game(page, "ai"),
    )

    two_player_button = ft.Button(
        content=ft.Text("2 Players"),
        bgcolor="orange",
        color="white",
        on_click=lambda e: game(page, "2p"),
    )

    back_button = ft.Button(
        content=ft.Text("Back"),
        on_click=lambda e: show_menu(page),
    )

    layout = ft.Column(
        controls=[
            title,

            ft.Row(
                controls=[
                    ai_button,
                    two_player_button,
                ],
                alignment="center",
            ),

            back_button,
        ],

        alignment="center",
        horizontal_alignment="center",
        spacing=20,
    )

    page.add(layout)

    page.update()

    
def main(page):

    page.window_width = 1400
    page.window_height = 850

    show_menu(page)



ft.run(main,assets_dir="assets")


    

        

                    


        

        




    
        
