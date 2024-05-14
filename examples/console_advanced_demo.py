"""
console_advanced_demo.py - Advanced demo of the mpconsole module using Graphics.text from direct_draw
"""

from board_config import display_drv
from console import Console
from sys import implementation, platform
import vga2_8x16 as font  # Check the font first, otherwise no need to load direct_draw
from direct_draw import Graphics  # Load direct_draw


SSID = "<ssid>"
PASSPHRASE = "<passphrase>"

# Create the tft object, specifying the rotation
tft = Graphics(display_drv, rotation=0)
# Tell Console to use tft.text as the character writer.  Have to use a lambda to map the
# way Console calls char_writer (without `font`) to the way tft.expects it with `font`
char_writer = lambda char, x, y, fg, bg: tft.text(font, char, x, y, fg, bg)
console = Console(tft, char_writer, cwidth=font.WIDTH, lheight=font.HEIGHT)

maj, min, *_ = implementation.version
try:
    import wifi

    wlan = wifi.connect(SSID, PASSPHRASE)
    console.label(
        Console.TITLE,
        f"{implementation.name} {maj}.{min} @ {wlan.ifconfig()[0]}",
        Graphics.BLACK,
    )
except ImportError:
    console.label(Console.TITLE, f"{implementation.name} {maj}.{min}", Graphics.BLACK)

console.label(Console.LEFT, platform, Graphics.RED)


try:
    from gc import mem_free

    console.label(Console.RIGHT, lambda: f"mf={mem_free():,}", Graphics.BLUE)
except ImportError:
    from psutil import virtual_memory

    console.label(Console.RIGHT, lambda: f"mf={virtual_memory().free:,}", Graphics.BLUE)


try:
    import os

    os.dupterm(console)
    help()
except:
    console.write("REPL not available.\n", Graphics.YELLOW)

#### Example commands
# console.cls()                   # Clear the console screen
# console.write("Hello, World!")  # Write text to the console
# console.hide()                  # Hide the console screen
# console.show()                  # Show the console screen after hiding it
