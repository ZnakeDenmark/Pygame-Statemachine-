from statemachine import StateMachine, State

class level(StateMachine):
    "Scene handling"
    floor1 = State("floor1", initial=True)
    floor2 = State("floor2")

    start = floor1.to(floor1)
    next = floor1.to(floor2)
    skift = "tester"
    @start.on
    def test(self):
        skift2 = "no more testing"
        level.skift = skift2
        print("current stage: floor1")
        scene.next()

    @next.on
    def test2(self):
        print("current stage: floor2")


        
    

scene = level()