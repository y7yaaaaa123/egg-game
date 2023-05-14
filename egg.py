class EggSpawner:
    def __init__(self):
        self.egg_group = pygame.sprite.Group()
        self.spawn_timer = random.randrange (30, 120)
    def update(self):
        self.egg_group.update()
        if self.spawn_timer == 0:
            self.spawn_egg ()
            self.spawn_timer = random.randrange (30, 120)

        else:   
            self.spawn_timer -= 1
    def spawn_egg (self):
        new_egg= Egg ()
        self.egg_group.add(new_egg)