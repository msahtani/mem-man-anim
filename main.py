from manim import *

class MemorySpace(Scene):


    def construct(self):

        heap = Rectangle(
            height=6, 
            width=4,
            stroke_width=2
        )
        object_ = Circle(
            radius=.5,
            fill_opacity=1
        )
        
        # add mobject to the scene
        self.add(heap, object_)
