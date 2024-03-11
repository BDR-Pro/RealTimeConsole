# RealTimeConsole ✨

Hey there! 👋 Welcome to `RealTimeConsole` - your go-to Python package for spicing up console outputs. Tired of static, unchanging text? We got you! Say goodbye to the old school and hello to dynamic, real-time updates. Progress bars, status messages, clean slates? We cover them all.

## Get It Now! 🚀

Install `RealTimeConsole` with pip, and jump straight into the action:

```bash
pip install RealTimeConsole
```

Psst... make sure your `pip` is up-to-date to dodge those annoying hiccups during installation.

## How To Rock It 🎸

### Yeeting the Last Line

Wanna update messages or progress bars like a boss? Use `RemoveLastLine`:

```python
from RealTimeConsole import RemoveLastLine
from time import sleep

# Just a lil' example to get you started:
for i in range(100):
    print(f"{'#' * i}---{i}% done...")
    RemoveLastLine()  # POOF! Last line gone!
    sleep(0.1)
```

### Clearing the Console Like Magic 🧙‍♂️

Messy console? Clear it out with `clearConsole` and start fresh:

```python
from RealTimeConsole import clearConsole
from time import sleep

# Zap away the old stuff:
clearConsole()

print("Printing 'Hello World' 10 times, watch this space!")
for i in range(10):
    print("Hello World")
    sleep(0.1)

# And... let's clear it all out again!
print("Brace yourself, clearing the console in 3...")
sleep(3)
clearConsole()
```

## Works Everywhere 🌎

Windows? Yep. Linux? You bet. macOS? Of course! `RealTimeConsole` is your cross-platform buddy.

## Join the Squad 🤝

Got ideas? Jump in and contribute! Found a bug 🐛? Wanna suggest a feature 🌟? Hit us up with an issue or PR.

## Shoutout 📢

Big thanks to everyone who's contributed to `RealTimeConsole`! Created by Bader Alotaibi - hit me up at `baderalotaibi3@gmail.com` for chats, collabs, you name it.

## Examples 🎨 Videos

We have a few examples of how to use the package in the examples folder.

1. Here With the `RemoveLastLine` function:
<video controls src="videos/remove.mp4" title="Title"></video>

2. Here Without the `RemoveLastLine` function:
<video controls src="videos/without.mp4" title="Title"></video>

3. Here With the `clearConsole` function:
<video controls src="videos/clearConsole.mp4" title="Title"></video>

## License 📜

### [MIT License](LICENSE)

## Stalk Us Here 👀

Peep the source code and let's get coding: [RealTimeConsole](https://github.com/bdr-pro/RealTimeConsole).

---

Feel free to tweak this template to better fit your project or personality. Keep it fun, keep it fresh, and most importantly, keep coding! 🎉
