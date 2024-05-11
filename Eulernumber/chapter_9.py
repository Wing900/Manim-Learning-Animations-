from manim import *
import numpy as np
class EulerNumber(Scene):
    def construct(self):
        # chapter9———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        #make objects
        chapter_9_title = Text("四、欧拉数的神奇之处",font_size=30)
        chapter_9_text1=Text("Euler-Mascheroni常数有以下神奇与有趣的性质:",font_size=24).shift(np.array([-2,2.7,0]))

        chapter_9_text2 = Tex(r"$\gamma=\lim_{n\to\infty}(\sum_{k=1}^n\frac{1}{k}-\ln n)$", font_size=32, color=BLUE).next_to(chapter_9_text1,DOWN,buff=0.4).shift(RIGHT*2.4)
        chapter_9_text2_change=Text("1.从它的定义来看，它关联了调和级数与自然对数，这两者出乎意料地通过这个常数联系在一起！",font_size=20,color=BLUE).next_to(chapter_9_text1,DOWN,buff=0.4).shift(RIGHT*2.35)

        chapter_9_text3 = Text("2.欧拉常数γ经常数论、复分析、以及特殊函数如Γ和ζ函数的研究中出现，扮演着神秘且重要的角色!", font_size=20,color=BLUE).next_to(chapter_9_text2,DOWN,buff=0.4).align_to(chapter_9_text2_change,LEFT)

        chapter_9_text4 = Text("3.欧拉常数γ至今未确定其有理性和超越性，π和e都已被证明，γ却仍然是一个悬而未决的问题!", font_size=20,color=BLUE).next_to(chapter_9_text3,DOWN,buff=0.4).align_to(chapter_9_text2_change,LEFT)
        chapter_9_last=Text("感谢观看！", font_size=40)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        #add objects to the scene
        self.play(Write(chapter_9_title,run_time=2))
        self.play(chapter_9_title.animate.to_edge(UP))
        self.wait(2)
        self.play(FadeIn(chapter_9_text1,run_time=2))
        self.wait(2)
        self.play(Write(chapter_9_text2,run_time=3))
        self.wait(2)
        self.play(Transform(chapter_9_text2,chapter_9_text2_change),run_time=3.5)
        self.wait(3)

        self.play(Write(chapter_9_text3,run_time=3))

        self.wait(2)

        self.play(Write(chapter_9_text4,run_time=3))

        self.wait(5)

        #clear objects
        self.play(FadeOut(chapter_9_title),FadeOut(chapter_9_text1),FadeOut(chapter_9_text2),FadeOut(chapter_9_text3),FadeOut(chapter_9_text4),run_time=3)

        self.wait(2)
        self.play(Write(chapter_9_last,run_time=2))
        self.wait(2)
        self.play(Unwrite(chapter_9_last),run_time=2)

        self.wait(2)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


