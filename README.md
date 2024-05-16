# Console
Console is a console / MicroPython REPL for [MPDisplay](https://github.com/bdbarnett/mpdisplay) adapted from [FBConsole](https://github.com/boochow/FBConsole)

Note: the Unix port of MicroPython has os.dupterm(), which enables duplicating the terminal (REPL), disabled by default.  To enable it, add
```
#define MICROPY_PY_OS_DUPTERM (1)
```
to the bottom of 
```
micropython/ports/unix/mpconfigport.h
```

See [console_simpletest.py](examples/console_simpletest.py) for a usage example.
