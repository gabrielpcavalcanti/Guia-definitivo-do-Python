from manim import *
import numpy as np

class eixo2(Scene):

    def construct(self):

        eixo2 = NumberPlane()

        funcao = eixo2.plot(lambda x: x**2-1, color= PURE_GREEN)
        funcao_label = MathTex('f(x)=x^2-1', color=PURE_GREEN).next_to(funcao, DOWN)

        ponto00 = np.array([0,0,0])
        ponto01 = np.array([1,1,0])

        vector01 = Arrow(ponto00, ponto01, color=YELLOW)
        
        self.play(Create(eixo2))
        self.wait()
        self.play(Create(funcao), Write(funcao_label))
        self.wait()
        self.play(Create(vector01))
        self.wait(2)
        