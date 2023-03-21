from statemachine import StateMachine, State
<<<<<<< HEAD

class level(StateMachine):
    "Scene handling"
    floor1 = State("floor1", initial=True)
    floor2 = State("floor2")
    floor3 = State("floor3")

    reset2 = floor3.to(floor1)
    reset = floor2.to(floor1)
    start = floor1.to(floor1)
    next = floor1.to(floor2)
    lvl3 = floor2.to(floor3)
    skift = "tester"
    lvl = "1"
    @start.on
    def test(self):
        skift2 = "no more testing"
        level.skift = skift2
        level.lvl = "2"
        print("current stage: floor1")
        scene.next()

    @next.on
    def test2(self):
        print("current stage: floor2")

    @lvl3.on
    def test3(self):
        skift2 = "no more testing"
        level.skift = skift2
        level.lvl = "3"



        
    

scene = level()
=======
import pygame as pg

class hotelgame(StateMachine):
    "Scene handling"
    floor1 = State("floor1", initial=True)
    floor2 = State("floor2")



    start = floor1.to(floor1)
    test = floor1.to(floor2)

    pg.init()

    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()


    @start.on
    def in_floor1(self):
        print("du er i floor1")
        while True:
            pressed = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        scene.test()

            pg.display.flip()
            clock.tick(60)

    @test.before
    def before_floor2(self):
        print("Du bevæger dig til floor2")

    @test.on
    def in_floor2(self):
        print("Du er i floor2")

scene = hotelgame()

scene.start()



>>>>>>> main
