from manim import *
import numpy as np
class EulerNumber(Scene):
    def construct(self):
        # chapter6———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        #create text and equations
        chapter_6_text1 = Text("综上所述，我们得到到两条事实：",font_size=29).shift(3*UP)
        chapter_6_text2 = Text("1.若无穷和S每一项都是正的，那么S会随着n越变越大",font_size=29,t2c={"正":BLUE,"大":BLUE}).next_to(chapter_6_text1,DOWN,buff=0.5)
        chapter_6_text3 = Text("2.若此时有一个数总比S大，那么S无穷和会趋于一个常数(收敛)",font_size=29,t2c={"大":BLUE,"常数":YELLOW}).next_to(chapter_6_text2,DOWN,buff=0.5).align_to(chapter_6_text2,LEFT)
        chapter_6_text4 = Text("那么对于全是负项的情况，那么我们也可以得到另两条等价的事实",font_size=29).next_to(chapter_6_text3,DOWN,buff=0.5)
        chapter_6_text2_change = Text("1.若无穷和S每一项都是负的，那么S会随着n越变越小",font_size=29,t2c={"负":RED,"小":RED}).next_to(chapter_6_text4,DOWN,buff=0.5).align_to(chapter_6_text2,LEFT)
        chapter_6_text3_change = Text("2.若此时有一个数总比S小，那么S无穷和会趋于一个常数(收敛)",font_size=29,t2c={"小":RED,"常数":YELLOW}).next_to(chapter_6_text2_change,DOWN,buff=0.5).align_to(chapter_6_text2,LEFT)
        chapter_6_text4_change = Text("这里我就偷懒不画图了，大家自行画图理解(并记住这些事实)",font_size=29).next_to(chapter_6_text3_change,DOWN,buff=0.5)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        #write and clean up
        self.play(Write(chapter_6_text1,run_time=3))

        self.wait(2)

        self.play(Write(chapter_6_text2),run_time=5)
        self.wait(1)
        self.play(Write(chapter_6_text3),run_time=5)
        self.wait(4)

        self.play(Write(chapter_6_text4),run_time=4)
        self.wait(1)

        self.play(Write(chapter_6_text2_change,run_time=3))
        self.wait(1)
        self.play(Write(chapter_6_text3_change,run_time=3))
        self.play(ApplyWave(chapter_6_text3_change, direction=UP), ApplyWave(chapter_6_text2_change, direction=DOWN), run_time=2)
        self.wait(4)
        self.play(Write(chapter_6_text4_change),run_time=3)
        self.wait(2)

        self.play(FadeOut(chapter_6_text1),FadeOut(chapter_6_text2),FadeOut(chapter_6_text3),FadeOut(chapter_6_text4),FadeOut(chapter_6_text2_change),FadeOut(chapter_6_text3_change),FadeOut(chapter_6_text4_change))

        self.wait(3)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

