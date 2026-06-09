import arcade

ALTURA = 600
LARGURA = 800
TITULO = "AURA"

class Moeda(arcade.Sprite):
    def __init__(self):
        super().__init__("moeda.png", scale=0.1)
    
    def update(self, delta_time):
        self.center_x += self.change_x
        self.center_y += self.change_y


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("player_direita.png", scale=0.5)
        self.textura_direita = arcade.load_texture("player_direita.png")
        self.textura_esquerda = arcade.load_texture("player_esquerda.png")


def update(self, delta_time):
        if self.change_x > 0:
            self.texture = self.textura_direita
        elif self.change_x < 0:
            self.texture = self.textura_esquerda


class Mainwindow(arcade.Window):
    def __init__(self):


        super().__init__(LARGURA, ALTURA, TITULO)

        arcade.set_background_color((46, 147, 255))

        self.personagem = Player()

        self.personagem.center_x = 400
        self.personagem.center_y = 300

        self.sprite_jogador = arcade.SpriteList()
        self.sprite_jogador.append(self.personagem)

        self.moeda = Moeda()
        self.moeda.center_x = 600
        self.moeda.center_y = 500

        self.sprite_moedas = arcade.SpriteList()
        self.sprite_moedas.append(self.moeda)


    def on_draw(self):


        self.clear()
        self.sprite_jogador.draw()
        self.sprite_moedas.draw()


    def on_update(self, delta_time):


        self.sprite_jogador.update(delta_time)
        self.sprite_moedas.update(delta_time)


    def executar():


        jogo = Mainwindow()
        arcade.run()

        
    if __name__ == "__main__":
        executar()
