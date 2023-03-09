from statemachine import StateMachine, State

class level(StateMachine):


    "Scene handling"
    floor1 = State("floor1", initial=True)
    floor2 = State("floor2")

    start = floor1.to(floor1)
    next = floor1.to(floor2)

    @start.on
    def test(self):
        print("current stage: floor1")
        scene.next()

    @next.on
    def test2(self):
        print("current stage: floor2")
    
    @next.on
    def test3(self):
        print("current stage: floor3")

        
    

scene = level()