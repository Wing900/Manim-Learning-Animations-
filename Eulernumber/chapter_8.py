from manim import *
import numpy as np
class EulerNumber(Scene):
    def construct(self):
        # chapter7———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        #make object
        chapter_8_text1=MathTex(r"First:& \ln (1+\frac{1}{n}) < \frac{1}{n} \Rightarrow \ln \frac{n+1}{n} < \frac{1}{n} \\&\ln \frac{2}{1}<\frac{1}{1},\ln \frac{3}{2} < \frac{1}{2},\ln \frac{4}{3} < \frac{1}{3},\cdots\ln \frac{n+1}{n} < \frac{1}{n} "
                                ,font_size=32,color=YELLOW).shift(UP*2.7)
        chapter_8_text2=Text("此时将不等式左右两边对齐，相加起来，得到：",font_size=29).next_to(chapter_8_text1,DOWN,buff=0.4)
        chapter_8_text3=MathTex(r"\ln (n+1) < 1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\cdots+\frac{1}{n} ",font_size=32,color=YELLOW).next_to(chapter_8_text2,DOWN,buff=0.4)
        chapter_8_text4=MathTex(r"\ln n +\ln \frac{n+1}{n} &< 1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\cdots+\frac{1}{n} \\\ln \frac{n+1}{n} &<1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\cdots+\frac{1}{n}-\ln n ",
                                font_size=32).next_to(chapter_8_text3,DOWN,buff=0.4).next_to(chapter_8_text3,DOWN,buff=0.4)
        chapter_8_text5=MathTex(r"so \quad S_n = right >\ln \frac{n+1}{n} > 0",font_size=32,color=YELLOW).next_to(chapter_8_text4,DOWN,buff=0.4)
        chapter_8_text6=Text("所以有一个常数，S一直大于它，根据我们刚才得到的事实",font_size=29).next_to(chapter_8_text5,DOWN,buff=0.4)
        chapter_8_text7=Text("得出S必定趋近于某个数，这个数就称为Euler常数",font_size=29).next_to(chapter_8_text5,DOWN,buff=0.4)
        chapter_8_text8=Text("以上就是全部证明过程，证毕！",font_size=29).next_to(chapter_8_text5,DOWN,buff=0.4)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        #add object to scene
        self.play(Write(chapter_8_text1,run_time=8))

        self.wait(5)

        self.play(Write(chapter_8_text2,run_time=2))
        self.wait(2)
        self.play(Write(chapter_8_text3,run_time=4))
        self.wait(3)
        self.play(Write(chapter_8_text4,run_time=4))
        self.wait(3)
        self.play(Write(chapter_8_text5,run_time=4))
        self.wait(3)
        self.play(Write(chapter_8_text6,run_time=3))
        self.wait(2)
        self.play(ReplacementTransform(chapter_8_text6,chapter_8_text7,run_time=3))
        self.wait(2)
        self.play(ReplacementTransform(chapter_8_text7,chapter_8_text8,run_time=3))

        self.wait(5)

        #clear all object
        self.play(FadeOut(chapter_8_text1),FadeOut(chapter_8_text2),FadeOut(chapter_8_text3),FadeOut(chapter_8_text4),FadeOut(chapter_8_text5),FadeOut(chapter_8_text6),FadeOut(chapter_8_text7),FadeOut(chapter_8_text8),run_time=2)

        self.wait(3)
        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
