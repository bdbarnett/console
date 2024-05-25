"""
console_advanced_demo.py - Advanced demo of the mpconsole module
"""

from board_config import display_drv
from console import Console
from sys import implementation, platform
import vga2_8x16 as font


SSID = "<ssid>"
PASSPHRASE = "<passphrase>"


pal = display_drv.get_palette()

# Have to use a lambda to map the way Console calls char_writer to the way display_drv.text expects it
char_writer = lambda char, x, y, fg, bg: display_drv.text(font, char, x, y, fg, bg)
console = Console(display_drv, char_writer, cwidth=font.WIDTH, lheight=font.HEIGHT)

maj, min, *_ = implementation.version
try:
    import wifi

    wifi.radio.connect(SSID, PASSPHRASE)
    console.label(
        Console.TITLE,
        f"{implementation.name} {maj}.{min} @ {wifi.radio.ipv4_address}",
        pal.BLACK,
    )
except:
    console.label(Console.TITLE, f"{implementation.name} {maj}.{min}", pal.BLACK)

try:
    import gc

    console.label(Console.RIGHT, lambda: f"mf={gc.mem_free():,}", pal.BLUE)
except ImportError:
    from psutil import virtual_memory

    console.label(Console.RIGHT, lambda: f"mf={virtual_memory().free:,}", pal.BLUE)

try:
    import os

    os.dupterm(console)
    help()
except:
    console.write("REPL not available.\n", pal.YELLOW)

console.label(Console.LEFT, platform, pal.RED)


#### Example commands
# console.cls()                   # Clear the console screen
# console.write("Hello, World!")  # Write text to the console
# console.hide()                  # Hide the console screen
# console.show()                  # Show the console screen after hiding it
