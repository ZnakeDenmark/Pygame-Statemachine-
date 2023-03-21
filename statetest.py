from statemachine import StateMachine, State

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