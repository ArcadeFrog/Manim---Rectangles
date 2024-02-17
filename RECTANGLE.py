from manim import *

class Test(Scene):
    def construct(self):
        
        green_square = Square(
            color=GREEN,
            fill_opacity=0.8,
            side_length=2
        )

        red_rectangle = Rectangle(
            color=RED, 
            fill_opacity=0.5
        )

        label = Text(
            "This is a square.",
        ).to_edge(
            DOWN, 
            buff=0.5
        )

        label2 = Text(
            "Square is also a rectangle."
        ).to_edge(
            UP,
            buff=1
        )

        label3 = Text(
            "Every rectangle have 4 sides and all angles equal 90°.",
            font_size=24
        ).to_edge(
            DOWN,
            buff=1
        )

        label4 = Text(
            "Let's remove one of the sides in the rectangle.",
            font_size=26
        ).to_edge(
            DOWN,
            buff = 1
        )

        triangle = Triangle(
            color=ORANGE,
            fill_opacity=0.5
        )

        label5 = Text(
            "We made a triangle."
        ).to_edge(
            UP,
            buff = 2
        )

        label6 = Text(
            "We made a triangle that all its sides are same length."
        ).to_edge(
            DOWN,
            buff = 1
        )

        self.play(Write(green_square))
        self.wait(2)
        self.play(Write(label))
        self.wait(2)
        self.play(FadeOut(label))
        self.play(Transform(green_square, red_rectangle))
        self.play(Write(label2))
        self.wait()
        self.play(FadeOut(label2))
        self.play(Write(label3))
        self.wait()
        self.play(FadeOut(label3))
        self.play(Write(label4))
        self.wait()
        self.play(Transform(red_rectangle, triangle))
        self.play(FadeOut(green_square))
        self.wait()
        self.play(FadeOut(label4))
        self.play(Write(label5), run_time = 5)
        self.wait()
        self.play(FadeOut(label5))
        self.wait()
        self.play(Write(label6))
