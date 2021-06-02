from ball import Ball
from button import Button
from player import Player
from scene import Scene
from graphics import *
from abstractui import AbstractUi
from score import Score
from vector import Vector
from highscore import HighScore


class Gameplay(Scene):

    def __init__(self, window: GraphWin, unpause_function, back_to_menu_function, exit_function, restart_function, highscore: HighScore):
        self.window = window

        self.lives = 3
        self.paused = False
        self.lost = False
        self.started = False

        self.score = Score(self.window)

        self.ball = Ball(self.window, Vector(400, 15), 10, 10, Vector(1, -1).normalized(), self.score, self.lose_life)
        self.player = Player(Vector(400, 500), Vector(50, 3), 10)

        self.score_ui = ScoreUi(self.window, restart_function, back_to_menu_function, exit_function, self.score, highscore)
        self.pause_ui = PauseUi(self.window, unpause_function, back_to_menu_function, exit_function)
        self.lives_ui = LivesUi(self.window, self.lives, Vector(10, 10), Vector(20, 0))

        self.linha_esquerda = Line(Point(0, 50), Point(0, 550))
        self.linha_direita = Line(Point(800, 50), Point(800, 550))
        self.linha_inferior = Line(Point(0, 575), Point(800, 575))
        self.linha_superior = Line(Point(0, 25), Point(800, 25))

        self.diabins = [Image(Point(200, 555), '_imagens/diabin.PNG'), Image(Point(600, 560), '_imagens/diabin.PNG')]
        self.clouds = []
        self.fogos = []

        self.linha_superior.setWidth(50)
        self.linha_superior.setFill(color_rgb(50, 50, 180))

        self.linha_inferior.setWidth(50)
        self.linha_inferior.setFill(color_rgb(250, 80, 80))

        self.linha_direita.setWidth(25)
        self.linha_direita.setFill(color_rgb(50, 50, 50))

        self.linha_esquerda.setWidth(25)
        self.linha_esquerda.setFill(color_rgb(50, 50, 50))

        for i in range(3):
            self.fogos.append(Image(Point(150 + (300 * i), 575), '_imagens/fogo.PNG'))

        for i in range(4):
            self.clouds.append(Image(Point(110 + (200 * i), 25), '_imagens/cloud.JPG'))

        self.window.setBackground('gray')

    def draw(self):
        self.restart()

        self.linha_superior.draw(self.window)
        self.linha_inferior.draw(self.window)
        self.linha_direita.draw(self.window)
        self.linha_esquerda.draw(self.window)

        for i in range(3):
            self.fogos[i].draw(self.window)

        for i in range(4):
            self.clouds[i].draw(self.window)

        for i in range(len(self.diabins)):
            self.diabins[i].draw(self.window)

        self.lives_ui.show()

        self.player.draw(self.window)
        self.ball.draw(self.window)
        self.score.draw()


    def undraw(self):
        self.paused = False

        self.player.undraw()
        self.ball.undraw()
        self.score.undraw()

        self.pause_ui.hide()
        self.score_ui.hide()
        self.lives_ui.hide()

        self.linha_superior.undraw()
        self.linha_inferior.undraw()
        self.linha_direita.undraw()
        self.linha_esquerda.undraw()

        for i in range(3):
            self.fogos[i].undraw()

        for i in range(4):
            self.clouds[i].undraw()

        for i in range(len(self.diabins)):
            self.diabins[i].undraw()

    def tick(self, mouse_position: Vector, mouse_click_position):
        if self.lost:
            self.score_ui.update(mouse_position, mouse_click_position)
        elif self.paused:
            self.pause_ui.update(mouse_position, mouse_click_position)
        else:
            self.player.update(self.window)
            self.ball.update(self.player)

    def move_player(self, direction: str):
        if self.paused:
            return

        if direction == "right":
            self.player.move_right()
        elif direction == "left":
            self.player.move_left()

    def pause(self):
        self.paused = not self.paused

        if self.paused:
            self.pause_ui.show()
        else:
            self.pause_ui.hide()

    def restart(self):
        self.lives = 3
        self.lives_ui.current_lives = self.lives

        self.lost = False
        self.paused = False
        self.started = False

        self.score.reset()
        self.ball.reset()

    def lose_life(self):
        self.lives -= 1
        self.ball.reset()
        self.lives_ui.update_lives(self.lives)

        if self.lives <= 0:
            self.lost = True
            self.score_ui.show()

    def start_game(self):
        self.started = True
        self.ball.release()


class PauseUi(AbstractUi):
    def __init__(self, window: GraphWin, unpause_function, back_to_menu_function, exit_function):
        self.window = window

        self.panel = Rectangle(Point(200, 100), Point(600, 500))
        self.panel.setFill(color_rgb(190, 190, 190))
        self.panel.setOutline("black")
        self.panel.setWidth(10)

        self.resume_button = Button(window, unpause_function, Vector(400, 275), Vector(75, 25), "Resume")
        self.menu_button = Button(window, back_to_menu_function, Vector(400, 350), Vector(70, 20), "Menu")
        self.exit_button = Button(window, exit_function, Vector(400, 425), Vector(70, 20), "Exit")

        self.title = Text(Point(405, 150), "Pause!")
        self.title.setSize(30)

    def show(self):
        self.panel.draw(self.window)
        self.resume_button.draw()
        self.menu_button.draw()
        self.exit_button.draw()
        self.title.draw(self.window)

    def hide(self):
        self.panel.undraw()
        self.resume_button.undraw()
        self.menu_button.undraw()
        self.exit_button.undraw()
        self.title.undraw()

    def update(self, mouse_position: Vector, mouse_click_position):
        self.resume_button.tick(mouse_position, mouse_click_position)
        self.menu_button.tick(mouse_position, mouse_click_position)
        self.exit_button.tick(mouse_position, mouse_click_position)


class ScoreUi(AbstractUi):
    def __init__(self,
                 window: GraphWin,
                 restart_function,
                 back_to_menu_function,
                 exit_function,
                 score: Score,
                 high_score: HighScore):
        self.window = window

        self.score = score
        self.highscore = high_score

        self.panel = Rectangle(Point(200, 100), Point(600, 500))
        self.panel.setFill(color_rgb(190, 190, 190))
        self.panel.setOutline("black")
        self.panel.setWidth(10)

        self.restart_button = Button(window, restart_function, Vector(400, 275), Vector(75, 25), "Resume")
        self.menu_button = Button(window, back_to_menu_function, Vector(400, 350), Vector(70, 20), "Menu")
        self.exit_button = Button(window, exit_function, Vector(400, 425), Vector(70, 20), "Exit")

        self.title = Text(Point(405, 150), "Score:")
        self.title.setSize(30)

        self.score_text = Text(Point(405, 175), "0")
        self.score_text.setSize(30)

        self.highscore_text = Text(Point(405, 200), "0")
        self.highscore_text.setSize(30)

    def show(self):
        self.panel.draw(self.window)
        self.restart_button.draw()
        self.menu_button.draw()
        self.exit_button.draw()
        self.title.draw(self.window)
        self.score_text.setText(f"{self.score.pts}")
        self.score_text.draw(self.window)
        self.highscore.set_high_score(self.score.pts)
        self.highscore_text.setText(f"HighScore: {self.highscore.high_score}")
        self.highscore_text.draw(self.window)

    def hide(self):
        self.panel.undraw()
        self.restart_button.undraw()
        self.menu_button.undraw()
        self.exit_button.undraw()
        self.title.undraw()
        self.score_text.undraw()
        self.highscore_text.undraw()

    def update(self, mouse_position: Vector, mouse_click_position):
        self.restart_button.tick(mouse_position, mouse_click_position)
        self.menu_button.tick(mouse_position, mouse_click_position)
        self.exit_button.tick(mouse_position, mouse_click_position)


class LivesUi:
    def __init__(self, window: GraphWin, max_lives: int, initial_position: Vector, spacing: Vector):
        self.window = window

        self.max_lives = max_lives
        self.current_lives = max_lives

        self.lives_sprites = []
        for i in range(self.max_lives):
            self.lives_sprites.append(Circle((initial_position + (spacing * i)).to_point(), 10))
            self.lives_sprites[i].setFill("green")

    def update_lives(self, lives: int):
        self.hide()
        self.current_lives = lives
        self.show()

    def show(self):
        for i in range(self.current_lives):
            if i < self.current_lives:
                self.lives_sprites[i].draw(self.window)
            else:
                self.lives_sprites[i].undraw()

    def hide(self):
        for i in range(self.max_lives):
            self.lives_sprites[i].undraw()
