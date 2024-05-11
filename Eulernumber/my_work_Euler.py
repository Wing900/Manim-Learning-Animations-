from manim import *
import numpy as np
class EulerMascheroniNumber(Scene):
    def construct(self):
        #这是我学了一个月左右manim的基础之后写的第一个长作品，此时python总学习时长也不超过1个月，只入门到了类，代码的风格可能并不那么好。
        #很开心完工了这份作品，构思大概花了四个小时，写代码碰到很多问题，累但是很有动力，花了大概两三天发疯般地写改改改，终于完成了。
        #我分了10个chapter去写，方便及时检测效果，于是这里的整合的代码也是按顺序来的，我并没有采用总体先创建物体再写动画的的方式，但在每个chapter里面是这样做的
        # This is my first extensive work written after learning the basics of manim for about a month. At this point, my total Python learning duration hadn't exceeded a month either, and I had just gotten started with classes. The coding style might not be that refined.
        #I'm thrilled to have completed this project. It took me roughly four hours to conceive the idea, and during the coding process, I encountered numerous issues. Despite being exhausting, the sheer drive to finish kept me going. I spent around two to three days fervently writing, tweaking, and revising until it was all done.
        #I divided the project into 10 chapters to facilitate immediate checks on the effects. Consequently, the consolidated code here is presented in sequence. While I didn't adopt an approach where all objects are created first before scripting the animations at the overall level, I did follow this practice within each individual chapter.
        # chapter0———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        # chapter_0_logo
        chapter_0_title = Text(
            r"W i n g",
            font="Pacifico",
            font_size=128, stroke_width=5,
            opacity=0.6, color=BLUE_A,
            stroke_color=BLUE_A
        )

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        # logo's animation
        self.play(Write(chapter_0_title), run_time=2)
        self.wait(1)
        self.play(FadeOut(chapter_0_title, run_time=4))
        self.wait(2)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # chapter1 ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        # make the mobjects of the chapter1
        chapter1_title1 = Text("大家好，今天我想给大家介绍一个神秘的数字", font_size=29)
        chapter1_title2 = Tex(r"欧拉常数$\gamma$\\[0.5em](Euler-Mascheroni number)",
                              tex_template=TexTemplateLibrary.ctex, font_size=29)
        chapter1_text1 = Tex("我将从以下几个方面展开：", tex_template=TexTemplateLibrary.ctex, font_size=29).shift(
            np.array([0, 3.2, 0]))
        chapter1_text2 = BulletedList("一、欧拉常数的简介", "二、级数（无穷和）", "三、欧拉常数的证明",
                                      "四、欧拉常数的神奇之处", buff=1, font_size=27,
                                      tex_template=TexTemplateLibrary.ctex).set_color(BLUE).next_to(chapter1_text1,
                                                                                                    DOWN, buff=1)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        # add the mobjects to the scene
        self.play(Write(chapter1_title1, run_time=2))
        self.wait(2)

        self.play(Transform(chapter1_title1, chapter1_title2))
        self.wait(2)

        self.play(Unwrite(chapter1_title1))
        self.play(Succession(Write(chapter1_text1, run_time=2)), Write(chapter1_text2, run_time=2))
        self.wait(3)

        self.play(Uncreate(chapter1_text1, run_time=2), FadeOut(chapter1_text2, run_time=2))
        self.wait(2)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
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
        # chapter3 ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        # make the objects
        chapter_3_title = Text("二、级数(无穷和)", font_size=36)
        chapter_3_text1 = Text("你可能并不知道级数，但你肯定理解无穷和", font_size=29).shift(np.array([-2, 2.7, 0]))
        chapter_3_text2 = Text("即无穷多个数相加,听上去似乎都是越加越大,比如说:", font_size=29).next_to(chapter_3_text1,
                                                                                                        DOWN,
                                                                                                        buff=0.4).align_to(
            chapter_3_text1, LEFT)
        chapter_3_text3 = Tex(r"$S=1+2+3+...+n=\frac{n(n+1)}{2}$", font_size=42, color=YELLOW).next_to(chapter_3_text2,
                                                                                                       DOWN,
                                                                                                       buff=0.4).align_to(
            chapter_3_text2, LEFT)
        chapter_3_text4 = Text("但如果你学过Taylor公式,你应该知道:", font_size=29).next_to(chapter_3_text3, DOWN,
                                                                                           buff=0.4).align_to(
            chapter_3_text3, LEFT)
        chapter_3_text5 = MathTex(r"e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+ \cdots +\frac{x^n}{n!}\quad (n \to \infty)",
                                  color=RED, font_size=42).next_to(chapter_3_text4, DOWN, buff=0.4).align_to(
            chapter_3_text4, LEFT)

        # change x to 1 2  #pay ateetion to color
        chapter_3_text5_change_1 = MathTex(
            r"e^1=1+1+\frac{1^2}{2!}+\frac{1^3}{3!}+\cdots+\frac{1^n}{n!} \quad (n\to\infty)", color=RED,
            font_size=45).next_to(chapter_3_text4, DOWN, buff=0.4).align_to(chapter_3_text4, LEFT)
        chapter_3_text5_change_2 = MathTex(
            r"e^2=1+2+\frac{2^2}{2!}+\frac{2^3}{3!}+\cdots+\frac{2^n}{n!} \quad (n\to\infty)", color=RED,
            font_size=45).next_to(chapter_3_text4, DOWN, buff=0.4).align_to(chapter_3_text4, LEFT)

        chapter_3_text6 = Text("当你变换x为1或2时,你会得到不同的无穷和,它们都是趋于一个常数的(如e)",
                               font_size=29).next_to(chapter_3_text5, DOWN, buff=0.4).align_to(chapter_3_text5, LEFT)
        chapter_3_text7 = Text("像这样趋于一个常数的无穷和,我们称它是收敛的", font_size=29).next_to(chapter_3_text6,
                                                                                                    DOWN,
                                                                                                    buff=0.4).align_to(
            chapter_3_text6, LEFT)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        # add animation
        self.play(Write(chapter_3_title, run_time=2))
        self.wait(2)
        self.play(chapter_3_title.animate.shift(np.array([-4.8, 3.5, 0])))
        self.wait(2)

        # succession of text

        self.play(Write(chapter_3_text1, run_time=2))
        self.wait(3)
        self.play(Write(chapter_3_text2, run_time=5))
        self.wait(3)
        self.play(Write(chapter_3_text3, run_time=4))
        self.wait(4)
        self.play(Write(chapter_3_text4, run_time=3))
        self.wait(3)
        self.play(Write(chapter_3_text5, run_time=6))  # 特效
        self.wait(5)
        self.play(Write(chapter_3_text6, run_time=4))
        self.wait(3)
        self.play(FocusOn(chapter_3_text5), run_time=2)  # 特效
        self.wait(2)
        self.play(Transform(chapter_3_text5, chapter_3_text5_change_1), run_time=3)
        self.wait(4)
        self.play(ApplyWave(chapter_3_text5, direction=UP + RIGHT, run_time=2))
        self.play(Transform(chapter_3_text5, chapter_3_text5_change_2), run_time=3)
        self.wait(4)
        self.play(ApplyWave(chapter_3_text5, direction=UP + RIGHT, run_time=2))
        self.wait(4)

        self.play(Write(chapter_3_text7, run_time=3))
        self.wait(4)

        self.play(FadeOut(chapter_3_title), FadeOut(chapter_3_text1), FadeOut(chapter_3_text2),
                  FadeOut(chapter_3_text3), FadeOut(chapter_3_text4), FadeOut(chapter_3_text5),
                  FadeOut(chapter_3_text6), FadeOut(chapter_3_text7), run_time=3)
        self.wait(2)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # chapter4———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        # make objects
        chapter_4_title = Text("二、级数(无穷和)", font_size=36).shift(np.array([-4.8, 3.5, 0]))
        chapter_4_text1 = Text("那么如何判断一个无穷和是否趋于一个常数（即收敛）呢？", font_size=29).shift(
            np.array([-1.5, 2.7, 0]))
        chapter_4_text2 = Text("其实有很多专业的方法可以判断，这里介绍一种简单的", font_size=29).next_to(chapter_4_text1,
                                                                                                        DOWN,
                                                                                                        buff=0.4).align_to(
            chapter_4_text1, LEFT)
        chapter_4_text3 = Text("它适用于每一项都是正数(positive number)的无穷和:", font_size=29).next_to(
            chapter_4_text2, DOWN, buff=0.4).align_to(chapter_4_text2, LEFT)

        chapter_4_text4 = Tex(r"$S=a_1+a_2+a_3+\cdots+a_n$", font_size=42, color=YELLOW).next_to(chapter_4_text3, DOWN,
                                                                                                 buff=0.4).align_to(
            chapter_4_text3, LEFT)
        chapter_4_text4_change = Tex(r"$S=positive+positive+positive+\cdots+positive$", font_size=40,
                                     color=YELLOW).next_to(chapter_4_text3, DOWN, buff=0.4).align_to(chapter_4_text4,
                                                                                                     LEFT)

        chapter_4_text5 = Text("这些些全是正项的无穷和有一个特点:每多一项,和一定是越来越大的", font_size=29).next_to(
            chapter_4_text4_change, DOWN, buff=0.4).align_to(chapter_4_text4_change, LEFT)
        chapter_4_text6 = Text("照这样说，岂不是所有的正项无穷和都趋于无穷大？", font_size=29).next_to(chapter_4_text5,
                                                                                                     DOWN,
                                                                                                     buff=0.4).align_to(
            chapter_4_text5, LEFT)
        chapter_4_text7 = Text("当然不是,我们把无穷和当成数列来看看:", font_size=29).next_to(chapter_4_text6, DOWN,
                                                                                             buff=0.4).align_to(
            chapter_4_text6, LEFT)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # add objects to the scene
        self.play(Write(chapter_4_title, run_time=2))
        self.wait(1)
        self.play(Write(chapter_4_text1, run_time=4))
        self.wait(3)

        self.play(Write(chapter_4_text2, run_time=4))
        self.wait(2)
        self.play(Write(chapter_4_text3, run_time=4))
        self.wait(3)
        self.play(Write(chapter_4_text4, run_time=4))

        self.wait(3)
        self.play(Transform(chapter_4_text4, chapter_4_text4_change))
        self.wait(3)
        self.play(Write(chapter_4_text5, run_time=4))
        self.wait(3)

        self.play(Transform(chapter_4_text4, chapter_4_text4_change), run_time=3)
        self.play(Write(chapter_4_text6, run_time=4))
        self.wait(3)
        self.play(Write(chapter_4_text7, run_time=4))
        self.wait(2)
        self.play(FadeOut(chapter_4_text1), FadeOut(chapter_4_text2), FadeOut(chapter_4_text3),
                  FadeOut(chapter_4_title),
                  FadeOut(chapter_4_text4), FadeOut(chapter_4_text5), FadeOut(chapter_4_text6),
                  FadeOut(chapter_4_text7), run_time=3)

        self.wait(2)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # chapter5 ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        # define the axes
        chapter_5_axes = Axes(
            axis_config={'include_ticks': False, 'stroke_width': 0.5, 'tip_shape': StealthTip, 'include_numbers': True},
            # 修改此处
            x_range=[0, 14, 1],  # 从0开始代表只有正半轴
            y_range=[0, 14, 2],  # 从0开始代表只有正半轴
            x_length=11,
            y_length=7, stroke_color=BLUE_A
        ).to_corner(DL, buff=0.5)
        label = chapter_5_axes.get_axis_labels(Tex(r"$n$").scale(0.7), Tex(r"$S_n$").scale(0.5))
        # write the text
        chapter_5_text1 = Text("先把数列各项画在坐标系上", font_size=29).shift(np.array([-1.5, 3.2, 0]))
        chapter_5_text2 = Tex(r"$S_1=a_1,S_2=a_1+a_2,S_3=a_1+a_2+a_3 \cdots$", color=YELLOW, font_size=42).next_to(
            chapter_5_text1, DOWN, buff=0.4)
        chapter_5_text3 = Text("当n增大时，S看起来似乎会一直越来越大", font_size=29).next_to(chapter_5_text2, DOWN,
                                                                                            buff=0.4).shift(RIGHT * 0.5)

        chapter_5_text4 = Text("但如果我告诉你:", font_size=29).shift(np.array([-1.5, 3.2, 0]))
        chapter_5_text5 = Tex(r"$\exists M,s.t. S_n\leq M$", font_size=42).next_to(chapter_5_text4, DOWN, buff=0.4)
        chapter_5_text6 = Text("结果会怎么样？", font_size=29).next_to(chapter_5_text5, DOWN, buff=0.4)

        chapter_5_text7 = Text("事实上:S将不断趋于一个小于等于M的常数,这个过程会永远持续下去", font_size=29).shift(
            np.array([0, 3.2, 0]))
        chapter_5_text8 = Text("严谨的证明是可行的，但直观的理解足够了", font_size=29).next_to(chapter_5_text7, DOWN,
                                                                                              buff=0.4)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        # by FunctionGraph
        e_graph = FunctionGraph(
            function=lambda x: 0, color=BLUE_A,
            x_range=[0.3, 14, 0.01])
        e_graph.move_to(Dot(chapter_5_axes.c2p(0, 7)), aligned_edge=LEFT)
        # plot the function by plot
        e_func_graph = chapter_5_axes.plot(
            function=lambda x: (1 + 2 / x) ** x, color=RED, stroke_width=2,
            x_range=[0.01, 16, 0.01], )

        self.play(Write(chapter_5_axes, run_time=5))
        self.play(Write(label))
        self.wait(2)
        # the first batch of texts
        self.play(Write(chapter_5_text1, run_time=3))

        self.wait(2)
        self.play(Write(chapter_5_text2, run_time=3))
        self.wait(3)
        dot_group = VGroup()  # the group of dots, to be used to clean all dotslater
        # the first batch of dots
        for i in range(1, 6):
            a = (1 + 2 / i) ** i
            dot_i = Dot(chapter_5_axes.c2p(i, a), color=RED, radius=0.04)

            self.play(FadeIn(dot_i, run_time=1))
            self.wait(1)
            dot_group = dot_group.add(dot_i)
        self.wait(3)
        self.play(Write(chapter_5_text3, run_time=4))
        self.wait(3)
        # clean
        self.play(FadeOut(chapter_5_text1, chapter_5_text2, chapter_5_text3, run_time=3))
        self.wait(1)

        # the second batch of texts
        self.play(Write(chapter_5_text4, run_time=3))

        self.wait(2)
        self.play(Write(chapter_5_text5, run_time=4))
        self.wait(4)
        self.play(Write(chapter_5_text6, run_time=3))
        self.wait(2)
        # plot the e_graph
        self.play(Create(e_graph, run_time=3))

        self.play(FocusOn(e_graph), run_time=2)
        # the second batch of dots

        self.wait(2)
        for i in range(6, 15):
            b = (1 + 2 / i) ** i
            dot_i = Dot(chapter_5_axes.c2p(i, b), color=RED, radius=0.04)

            self.play(FadeIn(dot_i, run_time=1))
            self.wait(1)
            dot_group = dot_group.add(dot_i)
        self.wait(2)

        # clean
        self.play(FadeOut(chapter_5_text4, chapter_5_text5, chapter_5_text6, run_time=3))
        self.wait(1)

        # the third batch of texts
        self.play(Write(chapter_5_text7, run_time=4))
        self.wait(3)
        self.play(Write(chapter_5_text8, run_time=5))
        self.wait(1.5)
        # plot the e_func_graph
        self.play(Create(e_func_graph, run_time=5))
        self.wait(2)
        self.play(ApplyWave(chapter_5_text7, run_time=1, amplitude=0.5, wiggle_rate=0.5, direction=DOWN))
        self.wait(2)
        # clean all
        self.play(FadeOut(chapter_5_text7, chapter_5_text8, e_graph, e_func_graph, label, chapter_5_axes, dot_group,
                          run_time=4))
        self.wait(3)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # chapter6———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        # create text and equations
        chapter_6_text1 = Text("综上所述，我们得到到两条事实：", font_size=29).shift(3 * UP)
        chapter_6_text2 = Text("1.若无穷和S每一项都是正的，那么S会随着n越变越大", font_size=29,
                               t2c={"正": BLUE, "大": BLUE}).next_to(chapter_6_text1, DOWN, buff=0.5)
        chapter_6_text3 = Text("2.若此时有一个数总比S大，那么S无穷和会趋于一个常数(收敛)", font_size=29,
                               t2c={"大": BLUE, "常数": YELLOW}).next_to(chapter_6_text2, DOWN, buff=0.5).align_to(
            chapter_6_text2, LEFT)
        chapter_6_text4 = Text("那么对于全是负项的情况，那么我们也可以得到另两条等价的事实", font_size=29).next_to(
            chapter_6_text3, DOWN, buff=0.5)
        chapter_6_text2_change = Text("1.若无穷和S每一项都是负的，那么S会随着n越变越小", font_size=29,
                                      t2c={"负": RED, "小": RED}).next_to(chapter_6_text4, DOWN, buff=0.5).align_to(
            chapter_6_text2, LEFT)
        chapter_6_text3_change = Text("2.若此时有一个数总比S小，那么S无穷和会趋于一个常数(收敛)", font_size=29,
                                      t2c={"小": RED, "常数": YELLOW}).next_to(chapter_6_text2_change, DOWN,
                                                                               buff=0.5).align_to(chapter_6_text2, LEFT)
        chapter_6_text4_change = Text("这里我就偷懒不画图了，大家自行画图理解(并记住这些事实)", font_size=29).next_to(
            chapter_6_text3_change, DOWN, buff=0.5)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        # write and clean up
        self.play(Write(chapter_6_text1, run_time=3))

        self.wait(2)

        self.play(Write(chapter_6_text2), run_time=5)
        self.wait(1)
        self.play(Write(chapter_6_text3), run_time=5)
        self.wait(4)

        self.play(Write(chapter_6_text4), run_time=4)
        self.wait(1)

        self.play(Write(chapter_6_text2_change, run_time=3))
        self.wait(1)
        self.play(Write(chapter_6_text3_change, run_time=3))
        self.play(ApplyWave(chapter_6_text3_change, direction=UP), ApplyWave(chapter_6_text2_change, direction=DOWN),
                  run_time=2)
        self.wait(4)
        self.play(Write(chapter_6_text4_change), run_time=3)
        self.wait(2)

        self.play(FadeOut(chapter_6_text1), FadeOut(chapter_6_text2), FadeOut(chapter_6_text3),
                  FadeOut(chapter_6_text4), FadeOut(chapter_6_text2_change), FadeOut(chapter_6_text3_change),
                  FadeOut(chapter_6_text4_change))

        self.wait(3)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # chapter7———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # make objects
        chapter_7_title1 = Text("三、欧拉常数的证明", font_size=32)
        chapter_7_title_change = Text("预备知识", font_size=32)
        chapter_7_title2 = Text("如果太快，请自行暂停", font_size=32).shift(UP * 3)
        chapter_7_text1 = Text("要证明这个无穷和趋于一个常数:", font_size=29).shift(UP * 3)
        chapter_7_text2 = Tex(r"$\S_n=1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\cdots+\frac{1}{n}-\ln n $", color=YELLOW,
                              font_size=42).next_to(chapter_7_text1, DOWN, buff=0.4)
        chapter_7_text3 = Text("可以按照我们刚刚给出的事实来证明", font_size=29).next_to(chapter_7_text2, DOWN,
                                                                                         buff=0.4)

        chapter_7_text4 = MathTex(
            r"S_n &=1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\cdots+\frac{1}{n}-\ln n \\ \ln n &=\ln 1 +\ln \frac{2}{1} +\ln \frac{3}{2} +\ln \frac{4}{3} +\cdots+\ln \frac{n}{n-1} \\ S_n&=1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n} -(\ln 1 +\ln \frac{2}{1} +\ln \frac{3}{2} +\cdots+\ln \frac{n}{n-1}) \\ S_n&=(1-\ln 1)+(\frac{1}{2}-\ln \frac{2}{1})+(\frac{1}{3}-\ln \frac{3}{2})+\cdots+(\frac{1}{n}-\ln \frac{n}{n-1}) "
            , font_size=35
            , color=BLUE
            ).next_to(chapter_7_title2, DOWN, buff=0.4)
        chapter_7_text5 = Tex(
            r"$S_n=(1-\ln 1)+(\frac{1}{2}-\ln \frac{2}{1})+(\frac{1}{3}-\ln \frac{3}{2})+\cdots+(\frac{1}{n}-\ln \frac{n}{n-1})$",
            font_size=42, color=YELLOW, stroke_width=3).next_to(chapter_7_text4, DOWN * 2, buff=0.4).align_to(
            chapter_7_text4, LEFT)

        chapter_7_text6 = Text("第二个预备知识(如果太快请自行暂停)", font_size=29).shift(UP * 3)
        chapter_7_text7 = Tex(r"$(1+\frac{1}{n})^n < e < (1+\frac{1}{n})^{n+1}$", font_size=35, color=YELLOW).next_to(
            chapter_7_text6, DOWN, buff=0.4)
        chapter_7_text8 = Text("两边取对数", font_size=35).next_to(chapter_7_text7, DOWN, buff=0.4)
        chapter_7_text8_change = Tex(r"$n\ln (1+\frac{1}{n}) < 1 < (n+1)\ln (1+\frac{1}{n})$", font_size=35,
                                     color=YELLOW).next_to(chapter_7_text7, DOWN, buff=0.4)
        chapter_7_text9 = MathTex(
            r"First: \frac{1}{n+1} < \frac{1}{n}  \quad Second: \frac{1}{n+1} < \ln (1+\frac{1}{n}) ", font_size=35,
            color=BLUE).next_to(chapter_7_text8_change, DOWN, buff=0.4)
        chapter_7_text10 = Tex(
            r"$Second: \frac{1}{n+1} < \ln (1+\frac{1}{n}) \quad \Rightarrow \quad \frac{1}{n} < \ln (1+\frac{1}{n-1})$",
            font_size=35, color=YELLOW).next_to(chapter_7_text9, DOWN, buff=0.4)
        chapter_7_text5_change = Tex(r"$n\ln (1+\frac{1}{n}) < 1 < (n+1)\ln (1+\frac{1}{n})$", font_size=35,
                                     color=YELLOW).next_to(chapter_7_text10, DOWN, buff=0.4).next_to(chapter_7_text10,
                                                                                                     DOWN, buff=0.4)
        chapter_7_text11 = Text("所以S中每一项都是负的,S越来越小", font_size=32).next_to(chapter_7_text10, DOWN,
                                                                                         buff=0.4).next_to(
            chapter_7_text5_change, DOWN, buff=0.4)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        self.play(Write(chapter_7_title1, run_time=2))
        self.wait(2)
        self.play(FadeOut(chapter_7_title1))
        self.wait(1)

        self.play(Write(chapter_7_text1, run_time=2))
        self.wait(1)
        self.play(Write(chapter_7_text2, run_time=4))
        self.wait(2)
        self.play(Write(chapter_7_text3, run_time=3))
        self.wait(2)
        self.play(FadeOut(chapter_7_text1), FadeOut(chapter_7_text2), FadeOut(chapter_7_text3), run_time=2)
        self.wait(1)

        self.play(Write(chapter_7_title_change, run_time=2))
        self.wait(2)
        self.play(FadeOut(chapter_7_title_change))
        self.wait(1)

        self.play(Write(chapter_7_title2, run_time=2))
        self.wait(2)
        self.play(Write(chapter_7_text4, run_time=40))
        self.wait(2)
        self.play(Write(chapter_7_text5, run_time=10))
        self.play(ApplyWave(chapter_7_text5, direction=UP, run_time=3))
        self.wait(3)
        # clean up
        self.play(FadeOut(chapter_7_text4), FadeOut(chapter_7_text5), FadeOut(chapter_7_title2), run_time=2)

        self.wait(2)
        self.play(Write(chapter_7_text6, run_time=2))
        self.wait(1)
        self.play(Write(chapter_7_text7, run_time=4))
        self.wait(3)
        self.play(Write(chapter_7_text8, run_time=3))
        self.wait(3)
        self.play(Transform(chapter_7_text8, chapter_7_text8_change, run_time=4))
        self.wait(3)
        self.play(Write(chapter_7_text9, run_time=4))
        self.wait(4)
        self.play(Write(chapter_7_text10, run_time=4))
        self.wait(4)
        self.play(ApplyWave(chapter_7_text10, direction=UP, run_time=3))
        self.wait(3)
        self.play(Write(chapter_7_text5_change, run_time=4))
        self.wait(4)
        self.play(Write(chapter_7_text11, run_time=4))
        self.play(FocusOn(chapter_7_text11), run_time=2)
        self.wait(2)
        self.play(FadeOut(chapter_7_text6), FadeOut(chapter_7_text7), FadeOut(chapter_7_text8),
                  FadeOut(chapter_7_text9), FadeOut(chapter_7_text10), FadeOut(chapter_7_text5_change),
                  FadeOut(chapter_7_text11), run_time=2)
        self.wait(3)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # chapter7———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # make object
        chapter_8_text1 = MathTex(
            r"First:& \ln (1+\frac{1}{n}) < \frac{1}{n} \Rightarrow \ln \frac{n+1}{n} < \frac{1}{n} \\&\ln \frac{2}{1}<\frac{1}{1},\ln \frac{3}{2} < \frac{1}{2},\ln \frac{4}{3} < \frac{1}{3},\cdots\ln \frac{n+1}{n} < \frac{1}{n} "
            , font_size=32, color=YELLOW).shift(UP * 2.7)
        chapter_8_text2 = Text("此时将不等式左右两边对齐，相加起来，得到：", font_size=29).next_to(chapter_8_text1, DOWN,
                                                                                                buff=0.4)
        chapter_8_text3 = MathTex(r"\ln (n+1) < 1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\cdots+\frac{1}{n} ",
                                  font_size=32, color=YELLOW).next_to(chapter_8_text2, DOWN, buff=0.4)
        chapter_8_text4 = MathTex(
            r"\ln n +\ln \frac{n+1}{n} &< 1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\cdots+\frac{1}{n} \\\ln \frac{n+1}{n} &<1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\cdots+\frac{1}{n}-\ln n ",
            font_size=32).next_to(chapter_8_text3, DOWN, buff=0.4).next_to(chapter_8_text3, DOWN, buff=0.4)
        chapter_8_text5 = MathTex(r"so \quad S_n = right >\ln \frac{n+1}{n} > 0", font_size=32, color=YELLOW).next_to(
            chapter_8_text4, DOWN, buff=0.4)
        chapter_8_text6 = Text("所以有一个常数，S一直大于它，根据我们刚才得到的事实", font_size=29).next_to(
            chapter_8_text5, DOWN, buff=0.4)
        chapter_8_text7 = Text("得出S必定趋近于某个数，这个数就称为Euler常数", font_size=29).next_to(chapter_8_text5,
                                                                                                    DOWN, buff=0.4)
        chapter_8_text8 = Text("以上就是全部证明过程，证毕！", font_size=29).next_to(chapter_8_text5, DOWN, buff=0.4)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # add object to scene
        self.play(Write(chapter_8_text1, run_time=8))

        self.wait(5)

        self.play(Write(chapter_8_text2, run_time=2))
        self.wait(2)
        self.play(Write(chapter_8_text3, run_time=4))
        self.wait(3)
        self.play(Write(chapter_8_text4, run_time=4))
        self.wait(3)
        self.play(Write(chapter_8_text5, run_time=4))
        self.wait(3)
        self.play(Write(chapter_8_text6, run_time=3))
        self.wait(2)
        self.play(ReplacementTransform(chapter_8_text6, chapter_8_text7, run_time=3))
        self.wait(2)
        self.play(ReplacementTransform(chapter_8_text7, chapter_8_text8, run_time=3))

        self.wait(5)

        # clear all object
        self.play(FadeOut(chapter_8_text1), FadeOut(chapter_8_text2), FadeOut(chapter_8_text3),
                  FadeOut(chapter_8_text4), FadeOut(chapter_8_text5), FadeOut(chapter_8_text6),
                  FadeOut(chapter_8_text7), FadeOut(chapter_8_text8), run_time=2)

        self.wait(3)
        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # chapter9———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # make objects
        chapter_9_title = Text("四、欧拉数的神奇之处", font_size=30)
        chapter_9_text1 = Text("Euler-Mascheroni常数有以下神奇与有趣的性质:", font_size=24).shift(
            np.array([-2, 2.7, 0]))

        chapter_9_text2 = Tex(r"$\gamma=\lim_{n\to\infty}(\sum_{k=1}^n\frac{1}{k}-\ln n)$", font_size=32,
                              color=BLUE).next_to(chapter_9_text1, DOWN, buff=0.4).shift(RIGHT * 2.4)
        chapter_9_text2_change = Text(
            "1.从它的定义来看，它关联了调和级数与自然对数，这两者出乎意料地通过这个常数联系在一起！", font_size=20,
            color=BLUE).next_to(chapter_9_text1, DOWN, buff=0.4).shift(RIGHT * 2.35)

        chapter_9_text3 = Text("2.欧拉常数γ经常数论、复分析、以及特殊函数如Γ和ζ函数的研究中出现，扮演着神秘且重要的角色!",
                               font_size=20, color=BLUE).next_to(chapter_9_text2, DOWN, buff=0.4).align_to(
            chapter_9_text2_change, LEFT)

        chapter_9_text4 = Text("3.欧拉常数γ至今未确定其有理性和超越性，π和e都已被证明，γ却仍然是一个悬而未决的问题!",
                               font_size=20, color=BLUE).next_to(chapter_9_text3, DOWN, buff=0.4).align_to(
            chapter_9_text2_change, LEFT)
        chapter_9_last = Text("感谢观看！", font_size=40)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # add objects to the scene
        self.play(Write(chapter_9_title, run_time=2))
        self.play(chapter_9_title.animate.to_edge(UP))
        self.wait(2)
        self.play(FadeIn(chapter_9_text1, run_time=2))
        self.wait(2)
        self.play(Write(chapter_9_text2, run_time=3))
        self.wait(2)
        self.play(Transform(chapter_9_text2, chapter_9_text2_change), run_time=3.5)
        self.wait(3)

        self.play(Write(chapter_9_text3, run_time=3))

        self.wait(2)

        self.play(Write(chapter_9_text4, run_time=3))

        self.wait(5)

        # clear objects
        self.play(FadeOut(chapter_9_title), FadeOut(chapter_9_text1), FadeOut(chapter_9_text2),
                  FadeOut(chapter_9_text3), FadeOut(chapter_9_text4), run_time=3)

        self.wait(2)
        self.play(Write(chapter_9_last, run_time=2))
        self.wait(2)
        self.play(Unwrite(chapter_9_last), run_time=2)

        self.wait(2)

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
