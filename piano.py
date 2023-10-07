import pygame
import sys
import mido

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1200  # Wider screen for better visualization
SCREEN_HEIGHT = 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
KEY_WIDTH = SCREEN_WIDTH // 88  # Divide the screen width by the number of keys
WHITE_KEY_HEIGHT = SCREEN_HEIGHT * 2 // 3
BLACK_KEY_HEIGHT = WHITE_KEY_HEIGHT * 2 // 3
KEY_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("88-Key Piano")

# Create a list to store key colors (white and black keys)
key_colors = [WHITE, BLACK] * 44  # Alternating white and black keys for 88 keys

# Create a dictionary to map MIDI notes to corresponding keys
note_to_key = {
    21: 0, 22: 1, 23: 2, 24: 3, 25: 4, 26: 5, 27: 6,
    # Add more mappings for all 88 keys...
}

# Initialize the MIDI input port using MIDO
midi_input = mido.open_input("Your_MIDI_Input_Device_Name")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for incoming MIDI messages
    for message in midi_input.iter_pending():
        if message.type == 'note_on':
            note = message.note
            if note in note_to_key:
                key_index = note_to_key[note]
                key_colors[key_index] = GRAY

        elif message.type == 'note_off':
            note = message.note
            if note in note_to_key:
                key_index = note_to_key[note]
                key_colors[key_index] = WHITE

    # Clear the screen
    screen.fill(WHITE)

    # Draw the piano keys and labels
    for i, color in enumerate(key_colors):
        if color == WHITE:
            key_height = WHITE_KEY_HEIGHT
            key_label = KEY_LABELS[i % 7]
        else:
            key_height = BLACK_KEY_HEIGHT
            key_label = ""

        key_rect = pygame.Rect(i * KEY_WIDTH, 0, KEY_WIDTH, key_height)
        pygame.draw.rect(screen, color, key_rect)

        if key_label:
            font = pygame.font.Font(None, 36)
            text = font.render(key_label, True, BLACK)
            text_rect = text.get_rect(center=(i * KEY_WIDTH + KEY_WIDTH // 2, WHITE_KEY_HEIGHT // 2))
            screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame and MIDO
pygame.quit()
mido.get_input_names().remove(midi_input.name)
midi_input.close()
sys.exit()
