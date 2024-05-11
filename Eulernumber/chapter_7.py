from manim import *
import numpy as np
class EulerNumber(Scene):
    def construct(self):
        # chapter7———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        #make objects
        chapter_7_title1 = Text("三、欧拉常数的证明",font_size=32)
        chapter_7_title_change=Text("预备知识",font_size=32)
        chapter_7_title2 = Text("如果太快，请自行暂停",font_size=32).shift(UP*3)
        chapter_7_text1=Text("要证明这个无穷和趋于一个常数:",font_size=29).shift(UP*3)
        chapter_7_text2=Tex(r"$\S_n=1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\cdots+\frac{1}{n}-\ln n $",color=YELLOW,font_size=42).next_to(chapter_7_text1,DOWN,buff=0.4)
        chapter_7_text3=Text("可以按照我们刚刚给出的事实来证明",font_size=29).next_to(chapter_7_text2,DOWN,buff=0.4)

        chapter_7_text4=MathTex(r"S_n &=1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\cdots+\frac{1}{n}-\ln n \\ \ln n &=\ln 1 +\ln \frac{2}{1} +\ln \frac{3}{2} +\ln \frac{4}{3} +\cdots+\ln \frac{n}{n-1} \\ S_n&=1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n} -(\ln 1 +\ln \frac{2}{1} +\ln \frac{3}{2} +\cdots+\ln \frac{n}{n-1}) \\ S_n&=(1-\ln 1)+(\frac{1}{2}-\ln \frac{2}{1})+(\frac{1}{3}-\ln \frac{3}{2})+\cdots+(\frac{1}{n}-\ln \frac{n}{n-1}) "
                            ,font_size=35
                                 ,color=BLUE
                                ).next_to(chapter_7_title2,DOWN,buff=0.4)
        chapter_7_text5=Tex(r"$S_n=(1-\ln 1)+(\frac{1}{2}-\ln \frac{2}{1})+(\frac{1}{3}-\ln \frac{3}{2})+\cdots+(\frac{1}{n}-\ln \frac{n}{n-1})$",font_size=42,color=YELLOW,stroke_width=3).next_to(chapter_7_text4,DOWN*2,buff=0.4).align_to(chapter_7_text4,LEFT)

        chapter_7_text6=Text("第二个预备知识(如果太快请自行暂停)",font_size=29).shift(UP*3)
        chapter_7_text7=Tex(r"$(1+\frac{1}{n})^n < e < (1+\frac{1}{n})^{n+1}$",font_size=35,color=YELLOW).next_to(chapter_7_text6,DOWN,buff=0.4)
        chapter_7_text8=Text("两边取对数",font_size=35).next_to(chapter_7_text7,DOWN,buff=0.4)
        chapter_7_text8_change=Tex(r"$n\ln (1+\frac{1}{n}) < 1 < (n+1)\ln (1+\frac{1}{n})$",font_size=35,color=YELLOW).next_to(chapter_7_text7,DOWN,buff=0.4)
        chapter_7_text9=MathTex(r"First: \frac{1}{n+1} < \frac{1}{n}  \quad Second: \frac{1}{n+1} < \ln (1+\frac{1}{n}) ",font_size=35,color=BLUE).next_to(chapter_7_text8_change,DOWN,buff=0.4)
        chapter_7_text10=Tex(r"$Second: \frac{1}{n+1} < \ln (1+\frac{1}{n}) \quad \Rightarrow \quad \frac{1}{n} < \ln (1+\frac{1}{n-1})$",font_size=35,color=YELLOW).next_to(chapter_7_text9,DOWN,buff=0.4)
        chapter_7_text5_change=Tex(r"$n\ln (1+\frac{1}{n}) < 1 < (n+1)\ln (1+\frac{1}{n})$",font_size=35,color=YELLOW).next_to(chapter_7_text10,DOWN,buff=0.4).next_to(chapter_7_text10,DOWN,buff=0.4)
        chapter_7_text11=Text("所以S中每一项都是负的,S越来越小",font_size=32).next_to(chapter_7_text10,DOWN,buff=0.4).next_to(chapter_7_text5_change,DOWN,buff=0.4)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        self.play(Write(chapter_7_title1,run_time=2))
        self.wait(2)
        self.play(FadeOut(chapter_7_title1))
        self.wait(1)


        self.play(Write(chapter_7_text1,run_time=2))
        self.wait(1)
        self.play(Write(chapter_7_text2,run_time=4))
        self.wait(2)
        self.play(Write(chapter_7_text3,run_time=3))
        self.wait(2)
        self.play(FadeOut(chapter_7_text1),FadeOut(chapter_7_text2),FadeOut(chapter_7_text3),run_time=2)
        self.wait(1)

        self.play(Write(chapter_7_title_change,run_time=2))
        self.wait(2)
        self.play(FadeOut(chapter_7_title_change))
        self.wait(1)


        self.play(Write(chapter_7_title2,run_time=2))
        self.wait(2)
        self.play(Write(chapter_7_text4,run_time=40))
        self.wait(2)
        self.play(Write(chapter_7_text5,run_time=10))
        self.play(ApplyWave(chapter_7_text5,direction=UP,run_time=3))
        self.wait(3)
        #clean up
        self.play(FadeOut(chapter_7_text4),FadeOut(chapter_7_text5),FadeOut(chapter_7_title2),run_time=2)

        self.wait(2)
        self.play(Write(chapter_7_text6,run_time=2))
        self.wait(1)
        self.play(Write(chapter_7_text7,run_time=4))
        self.wait(3)
        self.play(Write(chapter_7_text8,run_time=3))
        self.wait(3)
        self.play(Transform(chapter_7_text8,chapter_7_text8_change,run_time=4))
        self.wait(3)
        self.play(Write(chapter_7_text9,run_time=4))
        self.wait(4)
        self.play(Write(chapter_7_text10,run_time=4))
        self.wait(4)
        self.play(ApplyWave(chapter_7_text10,direction=UP,run_time=3))
        self.wait(3)
        self.play(Write(chapter_7_text5_change,run_time=4))
        self.wait(4)
        self.play(Write(chapter_7_text11,run_time=4))
        self.play(FocusOn(chapter_7_text11),run_time=2)
        self.wait(2)
        self.play(FadeOut(chapter_7_text6),FadeOut(chapter_7_text7),FadeOut(chapter_7_text8),FadeOut(chapter_7_text9),FadeOut(chapter_7_text10),FadeOut(chapter_7_text5_change),FadeOut(chapter_7_text11),run_time=2)
        self.wait(3)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————