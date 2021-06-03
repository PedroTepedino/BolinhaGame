import random

from ball import Ball
from button import Button
from player import Player
from scene import Scene
from graphics import *
from abstractui import AbstractUi
from score import Score
from vector import Vector
from highscore import HighScore
from pointsquare import PointSquare
from helperfunctions import get_random_color


class Gameplay(Scene):

    def __init__(self, window: GraphWin, unpause_function, back_to_menu_function, exit_function, restart_function,
                 highscore: HighScore):
        self.window = window

        self.lives = 3
        self.paused = False
        self.lost = False
        self.started = False

        self.score = Score(self.window)

        self.ball = Ball(self.window, Vector(400, 300), 10, 5, Vector(1, -1).normalized(), self.score, self.lose_life)
        self.player = Player(Vector(400, 500), Vector(50, 3), 10)

        self.squares = []

        for j in range(8):
            for i in range(15):
                self.squares.append(PointSquare(self.window, Vector(50 * (i + 1), 250 - (j * 25)), Vector(25, 12.5), get_random_color()))

        self.score_ui = ScoreUi(self.window, restart_function, back_to_menu_function, exit_function, self.score,
                                highscore)
        self.pause_ui = PauseUi(self.window, unpause_function, back_to_menu_function, exit_function)
        self.lives_ui = LivesUi(self.window, self.lives, Vector(15, 15), Vector(25, 0))

        self.background = Image(Point(400, 300), "_imagens/fundozozin.png")

        self.window.setBackground('gray')

    def draw(self):
        self.background.draw(self.window)

        self.lives_ui.show()

        for square in self.squares:
            square.show()

        self.player.draw(self.window)
        self.ball.draw(self.window)
        self.score.draw()

        self.restart()

    def undraw(self):
        self.paused = False

        self.player.undraw()
        self.ball.undraw()
        self.score.undraw()

        for square in self.squares:
            square.hide()

        self.pause_ui.hide()
        self.score_ui.hide()
        self.lives_ui.hide()

        self.background.undraw()

    def tick(self, mouse_position: Vector, mouse_click_position):
        if self.lost:
            self.score_ui.update(mouse_position, mouse_click_position)
        elif self.paused:
            self.pause_ui.update(mouse_position, mouse_click_position)
        else:
            self.player.update(self.window)
            self.ball.update(self.player, self.squares)
            self.player.change_speed((self.ball.current_speed - self.ball.initial_speed) / 2)

            has_active_square = False
            for squares in self.squares:
                if squares.is_active:
                    has_active_square = True
                    break
                    
            if not has_active_square:
                self.lose_life(3)

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
        self.player.reset()

        for square in self.squares:
            square.reset()
            square.hide()
            square.show()

        self.score_ui.hide()
        self.pause_ui.hide()
        self.lives_ui.hide()

        self.lives_ui.show()

    def lose_life(self, l: int = 1):
        self.lives -= l
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

        self.restart_button = Button(window, restart_function, Vector(400, 300), Vector(75, 25), "Restart")
        self.menu_button = Button(window, back_to_menu_function, Vector(400, 375), Vector(70, 20), "Menu")
        self.exit_button = Button(window, exit_function, Vector(400, 450), Vector(70, 20), "Exit")

        self.title = Text(Point(405, 125), "Score:")
        self.title.setSize(30)

        self.score_text = Text(Point(405, 175), "0")
        self.score_text.setSize(30)

        self.highscore_text = Text(Point(405, 225), "0")
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
            self.lives_sprites.append(Image((initial_position + (spacing * i)).to_point(), "_imagens/coracao.png"))

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
