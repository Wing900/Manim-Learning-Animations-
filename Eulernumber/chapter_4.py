from manim import *
import numpy as np
class EulerNumber(Scene):
    def construct(self):
        # chapter4———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        #make objects
        chapter_4_title = Text("二、级数(无穷和)", font_size=36).shift(np.array([-4.8,3.5,0]))
        chapter_4_text1=Text("那么如何判断一个无穷和是否趋于一个常数（即收敛）呢？",font_size=29).shift(np.array([-1.5,2.7,0]))
        chapter_4_text2=Text("其实有很多专业的方法可以判断，这里介绍一种简单的",font_size=29).next_to(chapter_4_text1,DOWN,buff=0.4).align_to(chapter_4_text1,LEFT)
        chapter_4_text3=Text("它适用于每一项都是正数(positive number)的无穷和:",font_size=29).next_to(chapter_4_text2,DOWN,buff=0.4).align_to(chapter_4_text2,LEFT)

        chapter_4_text4=Tex(r"$S=a_1+a_2+a_3+\cdots+a_n$",font_size=42,color=YELLOW).next_to(chapter_4_text3,DOWN,buff=0.4).align_to(chapter_4_text3,LEFT)
        chapter_4_text4_change=Tex(r"$S=positive+positive+positive+\cdots+positive$",font_size=40,color=YELLOW).next_to(chapter_4_text3,DOWN,buff=0.4).align_to(chapter_4_text4,LEFT)

        chapter_4_text5=Text("这些些全是正项的无穷和有一个特点:每多一项,和一定是越来越大的",font_size=29).next_to(chapter_4_text4_change,DOWN,buff=0.4).align_to(chapter_4_text4_change,LEFT)
        chapter_4_text6=Text("照这样说，岂不是所有的正项无穷和都趋于无穷大？",font_size=29).next_to(chapter_4_text5,DOWN,buff=0.4).align_to(chapter_4_text5,LEFT)
        chapter_4_text7=Text("当然不是,我们把无穷和当成数列来看看:",font_size=29).next_to(chapter_4_text6,DOWN,buff=0.4).align_to(chapter_4_text6,LEFT)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        #add objects to the scene
        self.play(Write(chapter_4_title,run_time=2))
        self.wait(1)
        self.play(Write(chapter_4_text1,run_time=4))
        self.wait(3)

        self.play(Write(chapter_4_text2,run_time=4))
        self.wait(2)
        self.play(Write(chapter_4_text3,run_time=4))
        self.wait(3)
        self.play(Write(chapter_4_text4,run_time=4))

        self.wait(3)
        self.play(Transform(chapter_4_text4,chapter_4_text4_change))
        self.wait(3)
        self.play(Write(chapter_4_text5,run_time=4))
        self.wait(3)

        self.play(Transform(chapter_4_text4,chapter_4_text4_change),run_time=3)
        self.play(Write(chapter_4_text6,run_time=4))
        self.wait(3)
        self.play(Write(chapter_4_text7,run_time=4))
        self.wait(2)
        self.play(FadeOut(chapter_4_title),FadeOut(chapter_4_text1),FadeOut(chapter_4_text2),FadeOut(chapter_4_text3),FadeOut(chapter_4_text4),FadeOut(chapter_4_text5),FadeOut(chapter_4_text6),FadeOut(chapter_4_text7),run_time=3)

        self.wait(2)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
