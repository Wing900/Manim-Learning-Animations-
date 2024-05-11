from manim import *

class EulerNumber(Scene):

    def construct(self):
        # chapter0———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        #chapter_0_logo
        chapter_0_title= Text(
            r"W i n g",
            font="Pacifico",
            font_size=128,stroke_width=5,
            opacity=0.6,color=BLUE_A,
            stroke_color=BLUE_A
        )

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        #logo's animation
        self.play(Write(chapter_0_title),run_time=2)
        self.wait(1)
        self.play(FadeOut(chapter_0_title,run_time=4))

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
