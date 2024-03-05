"""
mpconsole_simpletest.py

Copy the contents of this file to your boot.py to have it run on every bootup.
Call `console.hide()` before you use the display for anything else.
"""

try:
    # Make sure MPDisplay and MPDisplay are available
    from board_config import display_drv
    from mpconsole import Console
    try:
        # Check to see if tft_graphics is available, because it has better fonts than base MPDisplay
        import vga2_8x16 as font  # Check the font first, otherwise no need to load tft_graphics
        from tft_graphics import Graphics  # Load tft_graphics

        tft = Graphics(display_drv, rotation=0)  # Create the tft object, specifying the rotation
        # Tell Console to use tft.text as the character writer.  Have to use a lambda to map the
        # way Console calls char_writer (without `font`) to the way tft.expects it with `font`
        char_writer = lambda char, x, y, fg, bg: tft.text(font, char, x, y, fg, bg)
        console = Console(tft, char_writer, cwidth=font.WIDTH, lheight=font.HEIGHT)
    except ImportError:
        # If tft_graphics can't be loaded, just use the base MPDisplay with base font
        print("\nError loading tft_graphics or font.  Using base MPDisplay for console.\n")
        console = Console(display_drv)
except ImportError:
    print("\nError loading MPDisplay or MPConsole.\n")
    console = None


if console:
    from sys import implementation, platform
    console.sb_text_left(platform)

    if platform != "linux":
        from gc import mem_free
        console(True)  # Enable the REPL
        maj, min, *_ = implementation.version
        console.register_sb_cmds(right=lambda:f"mf={mem_free():,}")
        # If your board has WIFI, create a wifi.py file that connects to wifi and
        # creates a wlan object for it, then uncomment the following 2 lines.
#         from wifi import wlan
#         console.title(f"MicroPython {maj}.{min} REPL @ {wlan.ifconfig()[0]}", Graphics.BLUE)
    else:
        # MicroPython for Linux doesn't have os.dupterm compiled in by default and 
        # also doesn't have a timer, so just write enough test text to the console
        # to demonstrate scrolling.
        for x in range(60):
            console.write(f"Line {x}\n")

#### Example commands
# console(False)                  # Disable the repl 
# console.cls()                   # Clear the console screen
# console.hide()                  # Hide the console screen
# console.write("Hello, World!")  # Write text to the console

