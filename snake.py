import pygame
import random

class Apple:
    def __init__(self, pos_X, pos_Y):
        self.pos_X = pos_X
        self.pos_Y = pos_Y

class Node:
    def __init__(self, parent, pos_X, pos_Y):
        self.parent = parent
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.prev_X = pos_X
        self.prev_Y = pos_Y

    def update_position(self):
        # Guarda la posición actual como "previa"
        self.prev_X = self.pos_X
        self.prev_Y = self.pos_Y

        if self.parent is None:
            # La cabeza se mueve con input del jugador
            pass
        else:
            # El cuerpo sigue la posición previa del nodo anterior
            self.pos_X = self.parent.prev_X
            self.pos_Y = self.parent.prev_Y

    def move_left(self):
        if self.parent == None:
            self.pos_X -= node_size
            if self.pos_X < 0:
                self.pos_X = screen_width
        else:
            self.pos_X = self.parent.pos_X + node_size
            self.pos_Y = self.parent.pos_Y

    def move_right(self):
        if self.parent == None:
            self.pos_X += node_size
            if self.pos_X > screen_width:
                self.pos_X = 0
        else:
            self.pos_X = self.parent.pos_X - node_size
            self.pos_Y = self.parent.pos_Y

    def move_up(self):
        if self.parent == None:
            self.pos_Y -= node_size
            if self.pos_Y < 0:
                self.pos_Y = screen_height
        else:
            self.pos_Y = self.parent.pos_Y + node_size
            self.pos_X = self.parent.pos_X

    def move_down(self):
        if self.parent == None:
            self.pos_Y += node_size
            if self.pos_Y > screen_height:
                self.pos_Y = 0
        else:
            self.pos_Y = self.parent.pos_Y - node_size
            self.pos_X = self.parent.pos_X

def check_eat(node):
    if (node.pos_X, node.pos_Y) in apples_cords:
        tail = body[-1]
        body.append(Node(parent=tail, pos_X=tail.pos_X, pos_Y=tail.pos_Y))
        apples_cords.remove((node.pos_X, node.pos_Y))
        i = 0
        found = False
        while not found:
            if (apples[i].pos_X, apples[i].pos_Y) == (node.pos_X, node.pos_Y): 
                apples.pop(i)
                found = True
            else:
                i += 1
        return True
    else: return False

pygame.init()

# Sizes
screen_width = 1280
screen_height = 720
node_size = 40

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

head_X = screen_width/2
head_Y = screen_height/2

head = Node(parent=None, pos_X=head_X, pos_Y=head_Y)
body = list()
body.append(head)

velocity = 8
direction = ""
next_direction = ""

limit_apples = 3
apples = list()
apples_cords = list()

def generate_apple():
    apple_X = random.randint(1, (screen_width - 1)//node_size)*node_size
    apple_Y = random.randint(1, (screen_height - 1)//node_size)*node_size

    while (apple_X, apple_Y) in apples_cords:
        apple_X = random.randint(1, (screen_width - 1)//node_size)*node_size
        apple_Y = random.randint(1, (screen_height - 1)//node_size)*node_size

    apples_cords.append((apple_X, apple_Y))

    apples.append(Apple(
        pos_X=apple_X, 
        pos_Y=apple_Y
    ))

def check_colision():
    if len(body) > 2: 
        head = (body[0].pos_X, body[0].pos_Y)
        for node in body[1:]:
            if (node.pos_X, node.pos_Y) == head:
                return True
        else: return False

for i in range(limit_apples):
    generate_apple()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)

    running = not check_colision()

    for apple in apples:
        pygame.draw.rect(screen, RED, (apple.pos_X, apple.pos_Y, node_size, node_size))

    for node in body:
        node.update_position()

    if next_direction:
        if (direction == "UP" and next_direction != "DOWN") or \
        (direction == "DOWN" and next_direction != "UP") or \
        (direction == "LEFT" and next_direction != "RIGHT") or \
        (direction == "RIGHT" and next_direction != "LEFT") or \
        direction == "":
            direction = next_direction
            
    if direction == "DOWN":
        body[0].move_down()
    elif direction == "UP":
        body[0].move_up()
    elif direction == "LEFT":
        body[0].move_left()
    elif direction == "RIGHT":
        body[0].move_right()
    
    for node in body:
        if node.parent == None:
            pygame.draw.rect(screen, YELLOW, (node.pos_X, node.pos_Y, node_size, node_size))
        else:
            pygame.draw.rect(screen, GREEN, (node.pos_X, node.pos_Y, node_size, node_size))

    if check_eat(body[0]):
        generate_apple()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                next_direction = "DOWN"
            elif event.key == pygame.K_UP:
                next_direction = "UP"
            elif event.key == pygame.K_LEFT:
                next_direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                next_direction = "RIGHT"
            elif event.key == pygame.K_ESCAPE:
                running = False

    
    pygame.display.update()

    clock.tick(velocity)

pygame.quit()