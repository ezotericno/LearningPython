import sys 

import pygame

from settings import Settings

from ship import Ship

class AlienInvasion:
    """Overall class to manage game assests and behavior"""

    def __init__(self):
        """Initialize the game, and crate game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, 
                                               self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Set the Background colour
        self.bg_color = (230, 230, 230)

def run_game(self):
    """Start the main loop for the game"""
    while True:
        # Watch for keyboard and mouse events.
        self._check_events()
        self._update_screen()

        def _check_events(self):
            """Respond to keypresses and ouse events."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # Move the ship to the right.
                        self.ship.rect.x += 1

        def _update_screen(self):
            """Update images on the screen, and flip to the new screen."""
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
