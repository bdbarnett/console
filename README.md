# MPConsole
MPConsole is a console / MicroPython REPL for MPDisplay adapted from [FBConsole](https://github.com/boochow/FBConsole)

Note: the Unix port of MicroPython has os.dupterm(), which enables duplicating the terminal (REPL), disabled by default.  To enable it, add
```
#define MICROPY_PY_OS_DUPTERM (1)
```
to the bottom of 
```
micropython/ports/unix/mpconfigport.h
```

See [mpconsole_simpletest.py](mpconsole_simpletest.py) for a usage example.
