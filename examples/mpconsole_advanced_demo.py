"""
mpconsole_advanced_demo.py - Advanced demo of the mpconsole module using Graphics.text from tft_graphics

Copy the contents of this file to your boot.py to have it run on every bootup.
Call `console.hide()` before you use the display for anything else.
"""

# Make sure MPDisplay and MPDisplay are available
from board_config import display_drv
from mpconsole import Console
from gc import mem_free
from sys import implementation, platform
import vga2_8x16 as font  # Check the font first, otherwise no need to load tft_graphics
from tft_graphics import Graphics  # Load tft_graphics


tft = Graphics(display_drv, rotation=0)  # Create the tft object, specifying the rotation
# Tell Console to use tft.text as the character writer.  Have to use a lambda to map the
# way Console calls char_writer (without `font`) to the way tft.expects it with `font`
char_writer = lambda char, x, y, fg, bg: tft.text(font, char, x, y, fg, bg)
console = Console(tft, char_writer, cwidth=font.WIDTH, lheight=font.HEIGHT)
console.sb_text_left(platform, Graphics.RED)
console(True)  # Enable the REPL
maj, min, *_ = implementation.version
console.register_sb_cmds(right=lambda: f"mf={mem_free():,}")

try:
    from wifi import wlan
    console.title(f"MicroPython {maj}.{min} REPL @ {wlan.ifconfig()[0]}", Graphics.BLUE)
except ImportError:
    console.title(f"MicroPython {maj}.{min} REPL", Graphics.BLUE)


#### Example commands
# console(False)                  # Disable the repl
# console.cls()                   # Clear the console screen
# console.write("Hello, World!")  # Write text to the console
# console.hide()                  # Hide the console screen
