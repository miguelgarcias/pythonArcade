import arcade 

ALTURA = 600
LARGURA = 800
TITULO = "GAME"

class Player(arcade.Sprite):
    def __init___(self):
        super().__init__("personagem.png",scale=1)
        self.texture_direita
    def update(self, delta_time):
        pass    

class Mainwindow(arcade.Window):
    def __init__(self):
        super().__init__(LARGURA, ALTURA,TITULO)
        arcade.set_background_color((46, 147, 255))
    def on_draw(self):
        arcade.start_render()

    
    def on_update(self, delta_time):
        pass

def executar():
    jogo = Mainwindow()
    arcade.run()

if __name__ == "__main__":
    executar()