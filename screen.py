import pygame

DEFAULT_DIMENSIONS = (1000, 800)
DEFAULT_FPS = 60
class Screen:
    def __init__(self, width=DEFAULT_DIMENSIONS[0], height=DEFAULT_DIMENSIONS[1], fps=DEFAULT_FPS):
        self.width = width
        self.height = height
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.init()
        self.running = True

    def update(self):
        pass

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        pygame.display.flip()

    def run(self):
        while self.running:
            self.eventHandler()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        pygame.quit()