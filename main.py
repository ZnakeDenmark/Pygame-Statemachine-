import pygame
from sprites import *
from config import *
import sys
from statemachine import statemachine, State
#import * betyder at det tager hele kode
class Game(statemachine):
    floor1 = State("floor1", initial=True)
    floor2 = State("floor2")

    start = floor1.to(floor1)
    next = floor1.to(floor2)
    @start.on
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, Win_HEIGHT)) #sætter hvor stort skærm skal være
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font('MOTHEM_Black.ttf', 32)

        self.character_spritesheet = Spritesheet('img/character.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')
        self.door_spritesheet = Spritesheet('img/terrain.png')
        self.fakedoor_spritesheet = Spritesheet('img/terrain.png')
        self.enemy_spritesheet = Spritesheet('img/enemy.png')
        self.attack_spritesheet = Spritesheet('img/attack.png')
        self.intro_background = pygame.image.load('./img/introbackground.png')
        self.go_background = pygame.image.load('./img/gameover.png')
    


    @next.on
    def intro_screen(self):
        intro = True

        title = self.font.render('Dream Hotel', True, BLACK)
        title_rect = title.get_rect(x=10, y=10)

        play_button = Button(10, 50, 100, 50, WHITE, BLACK, 'Play', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
            
            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
    
    @next.on
    def new(self):
        #nyt spil starter
        self.playing = True
        self.skift = False

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.doors = pygame.sprite.LayeredUpdates()


    @next.on
    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "D":
                    Door(self, j, i)
                if column == "F":
                    FakeDoor(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    self.player = Player(self, j , i)
                if column == "E":
                    Enemy(self, j, i)
    
    @next.on
    def fixed(self):
        g = Game()
        while g.running:
            g.main()
            g.game_over()


    def createTilemap2(self):
        for sprite in self.all_sprites:
            sprite.kill()
        for i, row in enumerate(tilemap2):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "D":
                    Door(self, j, i)
                if column == "F":
                    FakeDoor(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    self.player = Player(self, j , i)
                if column == "E":
                    Enemy(self, j, i)



        
    
    def events(self):
        #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == 'up':
                        Attack(self, self.player.rect.x, self.player.rect.y - TILESIZE)
                    if self.player.facing == 'down':
                        Attack(self, self.player.rect.x, self.player.rect.y + TILESIZE)
                    if self.player.facing == 'left':
                        Attack(self, self.player.rect.x - TILESIZE, self.player.rect.y)
                    if self.player.facing == 'right':
                        Attack(self, self.player.rect.x + TILESIZE, self.player.rect.y)

    def update(self):
        #game loop updates
        self.all_sprites.update()
        

    def draw(self):
        #game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        #game loop
        while self.playing:
            if self.skift:
                self.skift = False
                self.createTilemap2()
            self.events()
            self.update()
            self.draw()
    
    def game_over(self):
        text = self.font.render('Game Over', True, WHITE)
        text_rect = text.get_rect(center=(WIN_WIDTH/2, Win_HEIGHT/2))

        restart_button = Button(10, Win_HEIGHT - 60, 120, 50, WHITE, BLACK, 'Restart', 32)

        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()
            self.screen.blit(self.go_background, (0,0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()


scene = Game()
scene.start()


pygame.quit()
sys.exit()
    