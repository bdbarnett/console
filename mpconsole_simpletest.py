"""
mpconsole_simpletest.py

Call `console.hide()` before you use the display for anything else.
"""

# Make sure MPDisplay and MPDisplay are available
from board_config import display_drv
from mpconsole import Console
from sys import implementation, platform
import time

try:
    import vga2_8x16 as font  # Check the font first, otherwise no need to load tft_graphics
    from tft_graphics import Graphics  # Load tft_graphics
    tft = Graphics(display_drv, rotation=0)  # Create the tft object, specifying the rotation
    # Tell Console to use tft.text as the character writer.  Have to use a lambda to map the
    # way Console calls char_writer (without `font`) to the way tft.expects it with `font`
    char_writer = lambda char, x, y, fg, bg: tft.text(font, char, x, y, fg, bg)
    console = Console(tft, char_writer, cwidth=font.WIDTH, lheight=font.HEIGHT)
    RED, GREEN, BLUE, BLACK = Graphics.RED, Graphics.GREEN, Graphics.BLUE, Graphics.BLACK
except ImportError:
    console = Console(display_drv)
    RED, GREEN, BLUE, BLACK = 0XF800, 0X07E0, 0X001F, 0X0000

maj, min, *_ = implementation.version
console.title("Simple Test", RED)
console.sb_text_left(platform, GREEN)
console.sb_text_middle(f"{implementation.name} {maj}.{min}", BLACK)
y, m, d, *_ = time.localtime()
console.sb_text_right(f"{m}-{d}-{y}", BLUE)

for x in range(60):
    console.write(f"Line {x}\n")

#### Example commands
# console(True)                   # Enable the repl
# console(False)                  # Disable the repl 
# console.cls()                   # Clear the console screen
# console.write("Hello, World!")  # Write text to the console
# console.hide()                  # Hide the console screen

