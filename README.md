# p8dl
[PICO-8](http://www.lexaloffle.com/pico-8.php) cartridge downloader

This should work on Windows, OS X and Linux.



## installing

Requires Python and pip!

For installing it to the Python user install directory for your platform:
```
pip install --user p8dl
```

If you want to install as root (not advised) or inside a virtualenv, you can drop the `--user` flag.

## usage

In your terminal:

```
p8dl 10022 # gets you Hug Army!
```

Then, in PICO-8:
```
> LOAD 10022
LOADED 10022.P8.PNG (15258 CHARS
)
> RUN
```
