 # world = []

world = [[], [], []] # 0번, 1번, 2번 레이어를 가진 2차원 리스트

 # 게임월드에 객체를 추가하는 함수, layer를 지정해야 한다.
def add_object(o, depth = 0):       # 기본 depth = 0
    world[depth].append(o)

# 게임월드에 객체를 제거하는 함수
def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()
        