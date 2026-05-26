import arcade 

ALTURA = 600
LARGURA = 800
TITULO = "AURA"

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("player_direita.png", scale=0.5)
        self.textura_direita = arcade.load_texture("player_direita.png")
        self.textura_esquerda = arcade.load_texture("player_esquerda.png")

    def update(self, delta_time):
        pass

class Mainwindow(arcade.Window):
    def __init__(self):
        super().__init__(LARGURA, ALTURA,TITULO)

        arcade.set_background_color((46, 147, 255))

        self.personagem = Player()

        self.personagem.center_x = 400
        self.personagem.center_y = 300

    def on_draw(self):
        self.clear()

        arcade.draw_sprite(self.personagem)
    def on_update(self, delta_time):
        pass

def executar():
    jogo = Mainwindow()
    arcade.run()

if __name__ == "__main__":
    executar()