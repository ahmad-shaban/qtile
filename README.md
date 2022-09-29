# **Qtile Config by A7MED**
---
# **Intro**
Qtile is a full-featured, hackable [tiling window manager](https://wiki.archlinux.org/title/window_manager) written in Python. Qtile is simple, small, and extensible. It is easy to write your own layouts, widgets, and built-in commands. It is written and configured entirely in Python.

The following comments are the copyright and licensing information from the default qtile config.
Copyright (c) 2010 Aldo Cortesi
Copyright (c) 2010, 2014 dequis
Copyright (c) 2012 Randall Ma
Copyright (c) 2012-2014 Tycho Andersen
Copyright (c) 2012 Craig Barnes
Copyright (c) 2013 horsik
Copyright (c) 2013 Tao Sauvage

Modified by A7MED

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


---
# **Screenshots**

![IMAGE](https://github.com/ahmed0124/qtile/blob/main/preview/rofi.png)

![IMAGE](https://github.com/ahmed0124/qtile/blob/main/preview/3-empty-terminals-monadtall.png)

![IMAGE](https://github.com/ahmed0124/qtile/blob/main/preview/neofetch.png)

![IMAGE](https://github.com/ahmed0124/qtile/blob/main/preview/bpytop-dropdown.png)

![IMAGE](https://github.com/ahmed0124/qtile/blob/main/preview/nautilus.png)

* ### **GTK Theme**: [Yaru-Aqua-Dark](https://www.gnome-look.org/p/1299514/)

* ### **Icon Themes**: [Flat-Remix-Cyan-Dark](https://www.gnome-look.org/p/1012430/), [Papirus](https://www.gnome-look.org/p/1166289/)

* ### **Cursor Theme**: [Vanilla-DMZ](https://www.gnome-look.org/p/999970/)

#### **Hint**: Use `lxappearence` app to set previous theme settings

---
# **Features**
* ### **App Launcher** `rofi`
  Theme is inspired by [adi1090x](https://github.com/adi1090x/rofi). This config is built on top of `rofi version >=1.7.4`
* ### **Screensaver**
  [screensaver.sh](https://github.com/ahmed0124/qtile/blob/main/scripts/screen-saver.sh) is custom script that depends on `xss-lock` and `i3lock` to provide screensaver functionality
* ### **TouchPad**
  [TouchPad.sh](https://github.com/ahmed0124/qtile/blob/main/scripts/TouchPad.sh) is custom script that depends on `xinput`. Used to enable "Tap to click" and "Natural scrolling" Options
* ### **Autostart**
  [autostart.sh](https://github.com/ahmed0124/qtile/blob/main/scripts/autostart.sh) will be called on session startup and by default it will do some tasks like set background, start compositor, start polkit agent and enable TouchPad. You can add more stuff here if you want it to be called on Qtile session startup

---
# **Widgets**
* ### **Image widget**
  It's the one that has python icon and it will trigger rofi app launcher if you left click on it

* ### **Groupbox**
  It's some sort of organization to your workflow in predefined workspaces with custom layouts

* ### **Prompt**
  dmenu like prompt

* ### **GenPollText (Disabled by default)**
  used to track total network usage by triggering the script [nt-usage.sh](https://github.com/ahmed0124/qtile/blob/main/scripts/nt-usage.sh) but note that it depends on `ifconfig` command from `net-tools`. You may need to change network interface name to your interface name, It's the one called "***wlp3s0***"

* ### **Keyboard Layout**
  by default it will switch between "**US**" and "**AR**" when you click on it, but of course you can change that to your layouts.

* ### **Volume**
  click will toggle mute

  mouse scrollback changes the volume/sound level

* ### **Battery (Disabled by default)**

* ### **Date and Time**

* ### **Qtile Layout Icon**
  switch to next layout by left mouse click and to previous layout by right mouse click

* ### **Task list (Disabled by default)**

* ### **Weather widget (Disabled by default)**

* ### **Systray widget (Disabled by default)**

* ### **Close Button (Disabled by default)**
  Image widget that will simulate the keybinding of ***kill active window***

* ### **Switch Button (Disabled by default)**
  Image widget that will simulate the keybinding of ***switch active window*** (useful for max layout to change active window easly by mouse)

#### Hint: Disabled widgets can be easly enabled by just uncomment thier lines in "***config.py***" file

---
# **Utilites**
* ### **Terminal Emulator**
  I use my custom build of [`st`](https://github.com/ahmed0124/st), but you can change that in ***config.py***
* ### **Web Browser**
  `firefox`
* ### **File Manager**
  `nautilus`
* ### **App Launcher**
  `rofi`
* ### **Screenshot Utility**
  `scrot` Note that you need to create ***`~/Pictures/Screenshots`*** dir beacuse it will save on it or change the path in the ***config.py***
* ### **Set background**
  `feh` is an awesome and lightweight image viewer and it can be used to set background as in here
* ### **Set themes**
  `lxappearence`
* ### **Compositor**
  `picom`
* ### **Screen Locker**
  `i3lock`

---
# **Installation**
## First install Qtile
refer to [qtile official website](http://docs.qtile.org/en/stable/manual/install/index.html) to see documentaion for how to install qtile on your distro
## Install dependencies
Depending on your distro, choose on of the following commands
#### Debian
```bash
sudo apt install rofi scrot feh lxappearance picom bpytop papirus-icon-theme policykit-1-gnome amixer brightnessctl xinput alsa-utils net-tools xss-lock i3lock fonts-font-awesome fonts-powerline fonts-symbola fonts-noto-color-emoji fonts-hack fonts-firacode
```
#### Fedora
```bash
sudo dnf install rofi scrot feh lxappearance picom bpytop papirus-icon-theme polkit-gnome brightnessctl xinput alsa-utils net-tools xss-lock i3lock fontawesome-fonts powerline-fonts texlive-noto-emoji adobe-source-code-pro-fonts fira-code-fonts
```
#### Arch
```bash
sudo pacman -S rofi scrot feh lxappearance picom bpytop papirus-icon-theme polkit-gnome brightnessctl xorg-xinput alsa-utils net-tools xss-lock i3lock awesome-terminal-fonts powerline-fonts noto-fonts-emoji ttf-hack adobe-source-code-pro-fonts ttf-fira-code
```
## Clone the configs
if you have previous qtile configs, make sure to backup by running this first
```bash
mv ~/.config/qtile ~/.config/qtile.bak
```
put the configs in thier proper location
```bash
git clone https://github.com/ahmed0124/qtile.git
mv qtile ~/.config/qtile
```
now logout and choose qtile session from your login manager and everything should be fine

---
# **Usage**
* ### **Apps**
KEYBINDINGS             | ASSOCIATED ACTIONS
------------------------|-------------------------
SUPER + ENTER           | open Terminal Emulator (st)
SUPER + W               | open Web Browser (firefox)
SUPER + E               | open File Manager (nautilus)
SUPER + SPACE           | change Keyboard Layout
SUPER + R               | PROMPT widget (dmenu like prompt)
SUPER + A               | open App Launcher (rofi)
F12			                | system monitor as a dropdown (bpytop)
Prt Scr                 | take a screenshot by `scrot` (saved in `~/Pictures/Screenshots`)
CTRL + ALT + ESCAPE     | Xkill (kill misbehaving apps)
SUPER + X               | lock screen

* ### **Qtile Session Control**
KEYBINDINGS             | ASSOCIATED ACTIONS
------------------------|-------------------------
SUPER + CTRL + R        | restart qtile session
SUPER + CTRL + Q        | quit qtile session (logout)

* ### **Window Control**
KEYBINDINGS             | ASSOCIATED ACTIONS
------------------------|-------------------------
ALT + TAB               | switch between active windows
SUPER + LEFT            | move focus to left
SUPER + RIGHT           | move focus to right
SUPER + DOWN            | move focus down
SUPER + UP              | move focus up
SUPER + M               | toggle window max state
SUPER + F               | toggle window fullscreen
SUPER + SHIFT + F       | toggle window floating
SUPER + Q               | close active window
ALT + F4                | close active window

* ### **Layout Control**
KEYBINDINGS             | ASSOCIATED ACTIONS
------------------------|-------------------------
SUPER + TAB             | toggle between Qtile Layouts
SUPER + SHIFT + LEFT    | move window to the left
SUPER + SHIFT + RIGHT   | move window to the right
SUPER + SHIFT + DOWN    | move window down
SUPER + SHIFT + UP      | move window up
SUPER + CTRL + LEFT     | grow window to the left
SUPER + CTRL + RIGHT    | grow window to the right
SUPER + CTRL + DOWN     | grow window down
SUPER + CTRL + UP       | grow window up
SUPER + N               | reset all windows sizes
SUPER + SHIFT + ENTER   | toggle between split and unsplit sides of stack
SUPER + ALT + F         | flip the main pane in monad layouts
SUPER + ALT + UP        | move up a section in treetab layout
SUPER + ALT + DOWN      | move down a section in treetab layout

* ### **Workspaces Control**
KEYBINDINGS             | ASSOCIATED ACTIONS
------------------------|-------------------------
SUPER + (1-7)           | switch to group (1-7)
SUPER + SHIFT + (1-7)   | move active window to group (1-7)
SUPER + PageUp          | switch to previous group or workspace
SUPER + PageDown        | switch to next group or workspace
SUPER + HOME            | switch to first group or workspace (workspace 1)
SUPER + END             | switch to last group or workspace (workspace 7)
SUPER + ESCAPE          | switch to last visited group or workspace

You should also be able to use screen brightness and voulme/sound keys to adjust them. If you have a calculator key in your keyboard it should start `Qalculate!` if it's installed on your system.

---
# **Aditional Tip**
if you notice [screen tearing](https://en.wikipedia.org/wiki/Screen_tearing) which is some sort of broken lines that appear when scrolling on web pages or when watching a video, it's not a qtile problem. it may be caused by your graphics card. try the next to solve it

## **First enable `vsync` in [picom.conf](https://github.com/ahmed0124/qtile/blob/main/picom/picom.conf)** like that
```
vsync = true
```

## **Depending on your Graphics Card**
* ### **if you have a reasonablly good dedicated Graphics Card**
  try changing the backend option in [picom.conf](https://github.com/ahmed0124/qtile/blob/main/picom/picom.conf) from **`xrender`** to **`glx`** like that
  ```
  backend = "glx"
  ```
* ### **else**
  add **`--experimental-backends`** in picom command in [autostart.sh](https://github.com/ahmed0124/qtile/blob/main/scripts/autostart.sh) like that
  ```
  picom --experimental-backends --config ~/.config/qtile/picom/picom.conf &
  ```

---
# **License**
The files and scripts in this repository are licensed under the [MIT License](https://github.com/ahmed0124/qtile/blob/main/LICENSE), which is a very permissive license allowing you to use, modify, copy, distribute, sell, give away, etc. the software. In other words, do what you want with it. The only requirement with the MIT License is that the license and copyright notice must be provided with the software.
