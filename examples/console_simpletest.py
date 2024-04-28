"""
console_simpletest.py

Call `console.hide()` before you use the display for anything else.
"""

from board_config import display_drv
from console import Console


console = Console(display_drv)

for x in range(60):
    console.write(f"Line {x}\n")
