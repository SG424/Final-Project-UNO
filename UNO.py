import flet as ft
import random

colors = ["Red", "Blue", "Green", "Yellow"]
values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip" , "+2"]

class card:
    def __init__(self, color, value):
        self.color = color
        self.value = value
    
    def can_play(self, top_card):
        same_color = (self.color == top_card.color)
        same_value = (self.value == top_card.value)
        
        return same_color or same_value
    
    def __str__(self):

        return (
            self.color
            + " "
            + self.value
        )

class game:
    
    def __init__(self, page):
        self.page = page

        page.title = "UNO by Oliver, Leanned, Mia and Luisa"

        page.window_width = 1400
        
        page.window_height = 850

        page.bgcolor = "#1E1E1E"

        self.start_new_game()

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