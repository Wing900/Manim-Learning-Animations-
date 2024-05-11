from manim import *
import numpy as np
class EulerNumber(Scene):
    def construct(self):
        #chapter1 ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        #make the mobjects of the chapter1
        chapter1_title1 = Text("大家好，今天我想给大家介绍一个神秘的数字",font_size=29)
        chapter1_title2 = Tex(r"欧拉常数$\gamma$\\[0.5em](Euler-Mascheroni number)",tex_template=TexTemplateLibrary.ctex,font_size=29)
        chapter1_text1 = Tex("我将从以下几个方面展开：",tex_template=TexTemplateLibrary.ctex,font_size=29).shift(np.array([0,3.2,0]))
        chapter1_text2 =BulletedList("一、欧拉常数的简介", "二、级数（无穷和）", "三、欧拉常数的证明", "四、欧拉常数的神奇之处",buff=1, font_size=27,tex_template=TexTemplateLibrary.ctex).set_color(BLUE).next_to(chapter1_text1,DOWN,buff=1)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        #add the mobjects to the scene
        self.play(Write(chapter1_title1,run_time=2))
        self.wait(2)

        self.play(Transform(chapter1_title1,chapter1_title2))
        self.wait(2)

        self.play(Unwrite(chapter1_title1))
        self.play(Succession(Write(chapter1_text1,run_time=2)),Write(chapter1_text2,run_time=2))
        self.wait(3)

        self.play(Uncreate(chapter1_text1,run_time=2),FadeOut(chapter1_text2,run_time=2))
        self.wait(2)


        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
