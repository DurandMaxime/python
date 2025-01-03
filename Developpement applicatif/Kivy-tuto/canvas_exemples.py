from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.properties import Clock
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("canvas_exemples.kv")

class CanvasExemple1(Widget):
    pass

class CanvasExemple2(Widget):
    pass

class CanvasExemple3(Widget):
    pass

class CanvasExemple4(Widget):                   # Exemple d'utilisation du canvas dans le code (aussi faisable depuis le fichier kv)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100,100,400,500), width=2)
            Color(0,1,0)
            Line(circle=(400,200,80), width=2)
            Line(rectangle=(700,500,150,100), width=5)
            self.rect = Rectangle(pos=(700,200), size=(150,100))
        
    def on_button_a_click(self):
        #print("toto")
        x, y = self.rect.pos
        width, height = self.rect.size
        # bord droit : x + width
        inc = dp(10)   
        diff = self.width - (x + width)
        if diff < inc:
            inc = diff
        x += inc
        self.rect.pos = (x,y)

class CanvasExemple5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)                     # vitesse horizontale 
        self.vy = dp(4)                     # vitesse vertical
        with self.canvas:
            self.ball = Ellipse(pos=(100,100), size=(self.ball_size,self.ball_size))
        Clock.schedule_interval(self.update, 1/60)
    
    def on_size(self, *args):                                               # Détecter le retaillement de la fenètre
        print("on_size : " + str(self.width) + ", " + str(self.height))
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)
    
    def update(self, dt):
        #print("update")
        x, y = self.ball.pos

        x += self.vx
        y += self.vy

        # si y + self.ball_size > self.height:
        # self.vy = -self.vy
        if y + self.ball_size > self.height:
            y = self.height-self.ball_size
            self.vy = -self.vy

        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = -self.vx

        if y < 0:
            y = 0
            self.vy = -self.vy
        
        if x < 0:
            x = 0
            self.vx = -self.vy
            

        self.ball.pos = (x, y)

class CanvasExemple6(Widget):
    pass

class CanvasExemple7(BoxLayout):
    pass