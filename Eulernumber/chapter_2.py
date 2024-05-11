from manim import *
import numpy as np
class EulerNumber(Scene):
    def construct(self):
        # chapter2———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        #make mobejects
        chapter_2_title = Text("一、欧拉常数的简介",font_size=36)
        chapter_2_picture=ImageMobject("Euler.jpg")
        chapter_2_text1=Text("欧拉常数Euler-Mascheroni number是一个无穷和(级数)的极限： ",font_size=34).shift(np.array([0,3,0]))
        chapter_2_text2=Tex(r"$\gamma=\lim_{n\to\infty}(\sum_{k=1}^n\frac{1}{k}-\ln n)$",font_size=34).next_to(chapter_2_text1,DOWN,buff=0.5)
        chapter_2_text3=MathTex(r"\gamma=1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\cdots+\frac{1}{n}-\ln n \quad (n \to \infty)",font_size=34,color=YELLOW).next_to(chapter_2_text2,DOWN,buff=0.5)
        chapter_2_text4=MathTex(r"\gamma \approx 0.5772156649015328606065120900824",font_size=29).next_to(chapter_2_text3,DOWN,buff=0.5)
        chapter_2_text5=Text("你可能会疑问：",font_size=34).next_to(chapter_2_text4,DOWN,buff=0.5)
        chapter_2_text6=Text("这样一个无穷求和真的会趋近于某个常数吗？",font_size=34).next_to(chapter_2_text5,DOWN,buff=0.5)
        chapter_2_text7=Text("这完全是有可能的,下面我们来证明",font_size=34).next_to(chapter_2_text6,DOWN,buff=0.5)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        #add objects to the scene
        self.play(Write(chapter_2_title,run_time=2))
        self.wait(1)
        self.play(chapter_2_title.animate.shift(np.array([-4.8,3.7,0])),run_time=1)
         #picture
        self.play(FadeIn(chapter_2_picture,scale=1.2,run_time=2))
        self.wait(1)
        self.play(chapter_2_picture.animate.shift(np.array([-5.1,0,0])),run_time=1)

        self.play(Write(chapter_2_text1,run_time=2))
        self.wait(1)
        self.play(ApplyWave(chapter_2_text1,direction=UP),run_time=1)
        self.play(Write(chapter_2_text2,run_time=4))#公式
        self.wait(4)
        self.play(Write(chapter_2_text3,run_time=4))
        self.wait(4)
        self.play(Write(chapter_2_text4,run_time=2))
        self.wait(3)
        self.play(Write(chapter_2_text5,run_time=2))
        self.wait(2)
        self.play(Write(chapter_2_text6,run_time=3.5))
        self.wait(3)
        self.play(Write(chapter_2_text7,run_time=3.5))
        self.wait(3)

        #clear all objects
        chapter_2_all=Group(chapter_2_title,chapter_2_picture,chapter_2_text1,chapter_2_text2,chapter_2_text3,chapter_2_text4,chapter_2_text5,chapter_2_text6,chapter_2_text7)
        self.play(FadeOut(chapter_2_all,run_time=3.999))

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————