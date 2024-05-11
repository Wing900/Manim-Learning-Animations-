from manim import *
import numpy as np
class EulerNumber(Scene):
    def construct(self):
        #chapter3 ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        #make the objects
        chapter_3_title = Text("二、级数(无穷和)",font_size=36)
        chapter_3_text1=Text("你可能并不知道级数，但你肯定理解无穷和",font_size=29).shift(np.array([-2,2.7,0]))
        chapter_3_text2=Text("即无穷多个数相加,听上去似乎都是越加越大,比如说:",font_size=29).next_to(chapter_3_text1,DOWN,buff=0.4).align_to(chapter_3_text1,LEFT)
        chapter_3_text3=Tex(r"$S=1+2+3+...+n=\frac{n(n+1)}{2}$",font_size=42,color=YELLOW).next_to(chapter_3_text2,DOWN,buff=0.4).align_to(chapter_3_text2,LEFT)
        chapter_3_text4=Text("但如果你学过Taylor公式,你应该知道:",font_size=29).next_to(chapter_3_text3,DOWN,buff=0.4).align_to(chapter_3_text3,LEFT)
        chapter_3_text5=MathTex(r"e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+ \cdots +\frac{x^n}{n!}\quad (n \to \infty)",color=RED,font_size=42).next_to(chapter_3_text4,DOWN,buff=0.4).align_to(chapter_3_text4,LEFT)


        #change x to 1 2  #pay ateetion to color
        chapter_3_text5_change_1=MathTex(r"e^1=1+1+\frac{1^2}{2!}+\frac{1^3}{3!}+\cdots+\frac{1^n}{n!} \quad (n\to\infty)",  color=RED,font_size=45).next_to(chapter_3_text4,DOWN,buff=0.4).align_to(chapter_3_text4,LEFT)
        chapter_3_text5_change_2=MathTex(r"e^2=1+2+\frac{2^2}{2!}+\frac{2^3}{3!}+\cdots+\frac{2^n}{n!} \quad (n\to\infty)",  color=RED,font_size=45).next_to(chapter_3_text4,DOWN,buff=0.4).align_to(chapter_3_text4,LEFT)

        chapter_3_text6=Text("当你变换x为1或2时,你会得到不同的无穷和,它们都是趋于一个常数的(如e)",font_size=29).next_to(chapter_3_text5,DOWN,buff=0.4).align_to(chapter_3_text5,LEFT)
        chapter_3_text7=Text("像这样趋于一个常数的无穷和,我们称它是收敛的",font_size=29).next_to(chapter_3_text6,DOWN,buff=0.4).align_to(chapter_3_text6,LEFT)


        #———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        #add animation
        self.play(Write(chapter_3_title,run_time=2))
        self.wait(2)
        self.play(chapter_3_title.animate.shift(np.array([-4.8,3.5,0])))
        self.wait(2)

        #succession of text

        self.play(Write(chapter_3_text1,run_time=2))
        self.wait(3)
        self.play(Write(chapter_3_text2,run_time=5))
        self.wait(3)
        self.play(Write(chapter_3_text3,run_time=4))
        self.wait(4)
        self.play(Write(chapter_3_text4,run_time=3))
        self.wait(3)
        self.play(Write(chapter_3_text5,run_time=6))#特效
        self.wait(5)
        self.play(Write(chapter_3_text6, run_time=4))
        self.wait(3)
        self.play(FocusOn(chapter_3_text5),run_time=2)#特效
        self.wait(2)
        self.play(Transform(chapter_3_text5,chapter_3_text5_change_1),run_time=3)
        self.wait(4)
        self.play(ApplyWave(chapter_3_text5,direction=UP+RIGHT,run_time=2))
        self.play(Transform(chapter_3_text5,chapter_3_text5_change_2),run_time=3)
        self.wait(4)
        self.play(ApplyWave(chapter_3_text5,direction=UP+RIGHT,run_time=2))
        self.wait(4)

        self.play(Write(chapter_3_text7, run_time=3))
        self.wait(4)

        self.play(FadeOut(chapter_3_title),FadeOut(chapter_3_text1),FadeOut(chapter_3_text2),FadeOut(chapter_3_text3),FadeOut(chapter_3_text4),FadeOut(chapter_3_text5),FadeOut(chapter_3_text6),FadeOut(chapter_3_text7),run_time=3)
        self.wait(2)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

