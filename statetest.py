from statemachine import StateMachine, State
import pygame as pg

class hotelgame(StateMachine):
    "Scene handling"
    floor1 = State("floor1", initial=True)
    floor2 = State("floor2")



    start = floor1.to(floor1)
    test = floor1.to(floor2)


    @start.on
    def in_floor1(self):
        print("du er i floor1")


    @test.before
    def before_floor2(self):
        print("Du bevæger dig til floor2")

    @test.on
    def in_floor2(self):
        print("Du er i floor2")

scene = hotelgame()

scene.start()



