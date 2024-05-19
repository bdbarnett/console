"""
console_advanced_demo.py - Advanced demo of the mpconsole module using Graphics.text from direct_draw
"""

from board_config import display_drv
from console import Console
from sys import implementation, platform
import vga2_8x16 as font


SSID = "<ssid>"
PASSPHRASE = "<passphrase>"

BLACK = display_drv.color565(0, 0, 0)
RED = display_drv.color565(255, 0, 0)
GREEN = display_drv.color565(0, 255, 0)
BLUE = display_drv.color565(0, 0, 255)
CYAN = display_drv.color565(0, 255, 255)
MAGENTA = display_drv.color565(255, 0, 255)
YELLOW = display_drv.color565(255, 255, 0)
WHITE = display_drv.color565(255, 255, 255)
#def _text(canvas, font, text, x0, y0, color=WHITE, background=BLACK):


# Have to use a lambda to map the way Console calls char_writer to the way display_drv.text expects it
char_writer = lambda char, x, y, fg, bg: display_drv.text(font, char, x, y, fg, bg)
console = Console(display_drv, char_writer, cwidth=font.WIDTH, lheight=font.HEIGHT)

maj, min, *_ = implementation.version
try:
    import wifi

    wlan = wifi.connect(SSID, PASSPHRASE)
    console.label(
        Console.TITLE,
        f"{implementation.name} {maj}.{min} @ {wlan.ifconfig()[0]}",
        BLACK,
    )
except ImportError:
    console.label(Console.TITLE, f"{implementation.name} {maj}.{min}", BLACK)

console.label(Console.LEFT, platform, RED)


try:
    import gc

    console.label(Console.RIGHT, lambda: f"mf={gc.mem_free():,}", BLUE)
except ImportError:
    from psutil import virtual_memory

    console.label(Console.RIGHT, lambda: f"mf={virtual_memory().free:,}", BLUE)


try:
    import os

    os.dupterm(console)
    help()
except:
    console.write("REPL not available.\n", YELLOW)

#### Example commands
# console.cls()                   # Clear the console screen
# console.write("Hello, World!")  # Write text to the console
# console.hide()                  # Hide the console screen
# console.show()                  # Show the console screen after hiding it
