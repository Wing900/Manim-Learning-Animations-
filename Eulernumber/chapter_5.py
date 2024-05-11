from manim import *
import numpy as np
class EulerNumber(Scene):
    def construct(self):
        #chapter5 ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        # define the axes
        chapter_5_axes = Axes(
            axis_config={'include_ticks': False, 'stroke_width': 0.5,'tip_shape':StealthTip,'include_numbers':True} , # 修改此处
            x_range=[0, 14, 1],  # 从0开始代表只有正半轴
            y_range=[0, 14,2],  # 从0开始代表只有正半轴
            x_length=11,
            y_length=7,stroke_color=BLUE_A
        ).to_corner(DL, buff=0.5)
        label=chapter_5_axes.get_axis_labels(Tex(r"$n$").scale(0.7),Tex(r"$S_n$").scale(0.5))
        #write the text
        chapter_5_text1=Text("先把数列各项画在坐标系上",font_size=29).shift(np.array([-1.5,3.2,0]))
        chapter_5_text2=Tex(r"$S_1=a_1,S_2=a_1+a_2,S_3=a_1+a_2+a_3 \cdots$",color=YELLOW,font_size=42).next_to(chapter_5_text1,DOWN,buff=0.4)
        chapter_5_text3=Text("当n增大时，S看起来似乎会一直越来越大",font_size=29).next_to(chapter_5_text2,DOWN,buff=0.4).shift(RIGHT*0.5)

        chapter_5_text4=Text("但如果我告诉你:",font_size=29).shift(np.array([-1.5,3.2,0]))
        chapter_5_text5=Tex(r"$\exists M,s.t. S_n\leq M$",font_size=42).next_to(chapter_5_text4,DOWN,buff=0.4)
        chapter_5_text6=Text("结果会怎么样？",font_size=29).next_to(chapter_5_text5,DOWN,buff=0.4)

        chapter_5_text7=Text("事实上:S将不断趋于一个小于等于M的常数,这个过程会永远持续下去",font_size=29).shift(np.array([0,3.2,0]))
        chapter_5_text8=Text("严谨的证明是可行的，但直观的理解足够了",font_size=29).next_to(chapter_5_text7,DOWN,buff=0.4)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        # by FunctionGraph
        e_graph = FunctionGraph(
            function=lambda x: 0,color=BLUE_A,
        x_range=[0.3,14,0.01])
        e_graph.move_to(Dot(chapter_5_axes.c2p(0,7)),aligned_edge=LEFT)
        #plot the function by plot
        e_func_graph = chapter_5_axes.plot(
            function=lambda x: (1+2/x)**x,color=RED,stroke_width=2,
        x_range=[0.01,16,0.01],)



        self.play(Write(chapter_5_axes,run_time=5))
        self.play(Write(label))
        self.wait(2)
        #the first batch of texts
        self.play(Write(chapter_5_text1,run_time=3))

        self.wait(2)
        self.play(Write(chapter_5_text2,run_time=3))
        self.wait(3)
        dot_group = VGroup()#the group of dots, to be used to clean all dotslater
        #the first batch of dots
        for i in range(1,6):
              a=(1+2/i)**i
              dot_i=Dot(chapter_5_axes.c2p(i,a),color=RED,radius=0.04)

              self.play(FadeIn(dot_i,run_time=1))
              self.wait(1)
              dot_group = dot_group.add(dot_i)
        self.wait(3)
        self.play(Write(chapter_5_text3,run_time=4))
        self.wait(3)
        #clean
        self.play(FadeOut(chapter_5_text1,chapter_5_text2,chapter_5_text3,run_time=3))
        self.wait(1)

        #the second batch of texts
        self.play(Write(chapter_5_text4,run_time=3))

        self.wait(2)
        self.play(Write(chapter_5_text5,run_time=4))
        self.wait(4)
        self.play(Write(chapter_5_text6,run_time=3))
        self.wait(2)
        #plot the e_graph
        self.play(Create(e_graph,run_time=3))

        self.play(FocusOn(e_graph),run_time=2)
        #the second batch of dots

        self.wait(2)
        for i in range(6,15):
            b = (1 + 2 / i) ** i
            dot_i = Dot(chapter_5_axes.c2p(i, b), color=RED, radius=0.04)

            self.play(FadeIn(dot_i, run_time=1))
            self.wait(1)
            dot_group=dot_group.add(dot_i)
        self.wait(2)


        #clean
        self.play(FadeOut(chapter_5_text4,chapter_5_text5,chapter_5_text6,run_time=3))
        self.wait(1)

        #the third batch of texts
        self.play(Write(chapter_5_text7,run_time=4))
        self.wait(3)
        self.play(Write(chapter_5_text8,run_time=5))
        self.wait(1.5)
        #plot the e_func_graph
        self.play(Create(e_func_graph,run_time=5))
        self.wait(2)
        self.play(ApplyWave(chapter_5_text7,run_time=1,amplitude=0.5,wiggle_rate=0.5,direction=DOWN))
        self.wait(2)
        #clean all
        self.play(FadeOut(chapter_5_text7,chapter_5_text8,e_graph,e_func_graph,label,chapter_5_axes,dot_group,run_time=4))
        self.wait(3)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————




