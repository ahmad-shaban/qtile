##############################################################################
#                           _    _____ __  __ _____ ____  
#                          / \  |___  |  \/  | ____|  _ \ 
#                         / _ \    / /| |\/| |  _| | | | |
#                        / ___ \  / / | |  | | |___| |_| |
#                       /_/   \_\/_/  |_|  |_|_____|____/ 
#                                                         
##############################################################################
#  
# The following comments are the copyright and licensing information from the
# default qtile config.
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from typing import List
import os
import re
import socket
import subprocess
from libqtile import bar, layout, widget, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


mod = "mod4"
alt = "mod1"
home = os.path.expanduser("~")
accent_color="#00ffff"
terminal = "st"


keys = [
    ### BASIC KEYBINDINGS
    ## Qtile control
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    ## Apps
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.spawn("firefox"), desc="Web Browser"),
    Key([mod], "e", lazy.spawn("nautilus -w"), desc="File Manager"),
    Key([mod], "space",
            lazy.widget["keyboardlayout"].next_keyboard(),
            desc="Change keyboard layout."
            ),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "a",
            lazy.spawn(home + "/.config/qtile/rofi/launcher.sh"),
            desc="rofi application launcher"
            ),
    Key([alt, "control"], "Escape",
            lazy.spawn("xkill"),
            desc="X Kill"
            ),
    Key([mod], "x",
            lazy.spawn("i3lock -f -e -c 000000"),
            desc="Lock screen"
            ),
    Key([], "Print",
            lazy.spawn("scrot 'Screenshot_%Y-%m-%d_%H-%M-%S.png' -e 'mv $f ~/Pictures/Screenshots/'"),
            desc="full screenshot"
            ),
    Key([], "XF86Calculator", lazy.spawn("qalculate"), desc="Qalculte! (Advanced calculator)"),
    ## Sound / Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+"), desc="increase volume by 5%"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-"), desc="decrease volume by 5%"),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle"), desc="mute volume"),
    ## Screen Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -d 'intel_backlight' s +5%"),
        desc="increase screen brightness by 5%"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -d 'intel_backlight' s 5%-"),
        desc="decrease scr brightness by 5%"),
    
    ### Window control
    ## Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([alt], "Tab", lazy.layout.next(), desc="Move window focus to next window"),
    Key([alt, "shift"], "Tab", lazy.layout.previous(), desc="Move window focus to previous window"),
    ## Control focused window
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([alt], "F4", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "m",
        lazy.window.toggle_maximize(),
        desc='toggle window max state'
        ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc="toggle fullscreen"
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc="toggle floating"
        ),

    ### Layout control
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle next layout"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle previous layout"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(),
            desc="Move window up"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
            desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(),
            desc="Grow window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(),
            desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all windows size"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    # Flip the main pane in monad layouts
    Key([mod, alt], "f", lazy.layout.flip(),
        desc="Flip the main pane in monad layouts"),
    # Treetab controls
    Key([mod, alt], "Up",
        lazy.layout.section_up(),
        desc="Move Up a section in treetab layout"
        ),
    Key([mod, alt], "Down",
        lazy.layout.section_down(),
        desc="Move Down a section in treetab layout"
        ),

    ### Groups
	Key([mod], "Page_Up",
			lazy.screen.prev_group(),
			desc="switch to previous group or workspace"
			),
	Key([mod], "Page_Down",
			lazy.screen.next_group(),
			desc="switch to next group or workspace"
			),
	Key([mod], "Home",
			lazy.group['1'].toscreen(),
			desc="switch to first group or workspace"
			),
	Key([mod], "End",
			lazy.group['7'].toscreen(),
			desc="switch to last group or workspace"
			),
    Key([mod], "Escape",
            lazy.screen.toggle_group(),
            desc="Switch to last visited group"
            )
]

#groups = [Group(i) for i in "123456789"]
groups = [Group("1", label="DEV", layout="monadwide"),
          Group("2", label="WEB", layout="columns"),
          Group("3", label="CHAT", layout="columns"),
          Group("4", label="DOC", layout="monadtall"),
          Group("5", label="MEDIA", layout="max"),
          Group("6", label="GAME", layout="max"),
          Group("7", label="VM", layout="max")]

for i in groups:
    keys.extend([
        # Super + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # Super + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # Super + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
        
        # Add a Keybinding for ScratchPad DropDown
        Key([], "F12", lazy.group["scratchpad"].dropdown_toggle("bpytop"))
    ])

# Append ScratchPad to groups list
groups.append(
	ScratchPad("scratchpad", [
		# define a drop down terminal
		DropDown("bpytop", terminal + " -e bpytop", height=0.75, opacity=1, on_focus_lost_hide=True)
	])
    )

layouts = [
    layout.floating.Floating(border_focus=accent_color, border_normal="#ffffff", border_width=2),
    layout.Max(),
    layout.MonadTall(border_focus=accent_color, border_normal="#ffffff", margin=4, border_width=2),
    layout.MonadWide(border_focus=accent_color, border_normal="#ffffff", margin=4, border_width=2),
    layout.MonadThreeCol(border_focus=accent_color, border_normal="#ffffff", margin=4, border_width=2),
    layout.Bsp(border_focus=accent_color, border_normal="#004444", border_width=2),
    layout.RatioTile(border_focus=accent_color, border_normal="#004444", border_width=2),
    layout.Tile(border_focus=accent_color, border_normal="#004444", border_width=2),
    layout.VerticalTile(border_focus=accent_color, border_normal="#004444", border_width=2),
    # layout.Slice(),
    # layout.Spiral(border_focus=accent_color, border_normal="#004444", border_width=2),
    layout.Columns(border_focus=accent_color, border_normal="#004444", border_focus_stack=accent_color, border_normal_stack="#004444", border_width=2),
    layout.Stack(border_focus=accent_color, border_normal="#004444", border_width=2, num_stacks=2, autosplit=False),
    layout.Matrix(border_focus=accent_color, border_normal="#004444", border_width=2),
    layout.TreeTab(active_bg=accent_color, active_fg="#000000", panel_width=200, font="Awesome", fontsize=20, sections=["SECTION 1", "SECTION 2", "SECTION 3", "SECTION 4"], section_fontsize=22, previous_on_rm=True)
    # layout.Zoomy(columnwidth=200, margin=4)
]

####### MOUSE CALLBACKS #######
def open_rofi():
    qtile.cmd_spawn(home + "/.config/qtile/rofi/launcher.sh")

def kill_active_window():
    qtile.cmd_simulate_keypress([mod], "q")

def switch_next_window():
    qtile.cmd_simulate_keypress([alt], "Tab")

def switch_previous_window():
    qtile.cmd_simulate_keypress([alt, "shift"], "Tab")

widget_defaults = dict(
    font="Awesome",
    fontsize=22,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        ## Top Bar
        top=bar.Bar(
            [
                # App Launcher "rofi"
                widget.Image(
                    filename = "~/.config/qtile/icons/python.png",
                    mouse_callbacks = {"Button1": open_rofi}
                ),

                # Groups
                widget.GroupBox(disable_drag=True,
                    spacing = 5,
					highlight_method="block",
                    #borderwidth=4,
                    this_current_screen_border=accent_color,
                    block_highlight_text_color="#000000",
                    active=accent_color, inactive="#ffffff",
                    urgent_alert_method="block",
					#urgent_border="#ff0000",
                    urgent_text="#ff0000",
                    ),
                widget.TextBox(text=" "),
                
                # qtile prompt like dmenu
                widget.Prompt(foreground=accent_color, font="Source Code Pro Semibold"),
                
                widget.Spacer(),
               
                ## Task list
                #widget.TaskList(highlight_method="block", border="#666666",
                #    borderwidth=0,
                #    #margin=4,
                #    icon_size=22,
                #    font="Source Code Pro semibold",
                #    fontsize=16,
                #    #max_title_width=30
                #    ),
               
                ## Window name
                #widget.WindowName(foreground=accent_color),
               
                ## Switch Button "Switch active window" --> switch active window easly with mouse in max layout
                #widget.Image(
                #    filename = "~/.config/qtile/icons/switch-button.png",
                #    scale=False,
                #    margin=1,
                #    mouse_callbacks = {"Button1": switch_next_window, "Button2": switch_previous_window}
                #),
               
                ## Close Button "kill active window"
                #widget.Image(
                #    filename = "~/.config/qtile/icons/close-button.png",
                #    scale=False,
                #    margin=1,
                #    mouse_callbacks = {"Button1": kill_active_window}
                #),
                
                ## KeyChord ---> see that for doc "https://docs.qtile.org/en/stable/manual/config/keys.html#keychords"
                #widget.Chord(
                #     chords_colors={
                #         'launch': (accent_color, "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),
                
                ## Weather
                #widget.OpenWeather(location="cairo", format="☁ {main_temp}°{units_temperature} {weather_details} "),
                
                ## Systray
                #widget.WidgetBox(widgets = [widget.Systray()], text_closed="⮜", text_open="⮞ "),
                
                ## Network usage "if it doesn't work, you need to edit the script to change network interface name"
                #widget.GenPollText(update_interval=1, func=lambda: subprocess.check_output(home + "/.config/qtile/scripts/nt-usage.sh").decode("utf-8"), foreground=accent_color),
                
                ## CPU
                #widget.TextBox(text="CPU:", foreground=accent_color),
                #widget.CPU(format="{freq_current}GHz {load_percent}%"),
                
                ## Memory
                #widget.TextBox(text="Memory:", foreground=accent_color),
                #widget.Memory(),
                
                ## Keyboard Layout
                widget.TextBox(text=" "),
                widget.KeyboardLayout(configured_keyboards=["us","ar"]),
                widget.TextBox(text=" "),
                
                ## Sound / Volume
                widget.Volume(volume_app="pavucontrol", step=3, foreground=accent_color, fmt="🎧{}"),

                ## Battery
                #widget.Battery(foreground="#ffe05c", format=" ⚡{percent:2.0%} ", show_short_text=False),
                
                ## Date and Time
                widget.TextBox(text="🕒"),
                widget.Clock(format="%a %d %b - %I:%M:%S %p", foreground=accent_color),
                
                ## Qtile Layout Icon
                widget.CurrentLayoutIcon(),
                
                ## Exit Qtile Session
                #widget.QuickExit(foreground="#ff0000"),
            ],
            33,
            background='#000000',
        ),
        ## Bottom Bar
        #bottom=bar.Bar([
        #    widget.WindowTabs()
        #    ],
        #    24,
        #    ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(border_focus=accent_color, border_normal="#ffffff", border_width=2, float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(title='OGL'), # OGL devleopment 
    Match(title='Qalculate!'),
    Match(wm_class='vncviewer'),
    Match(wm_class='xterm'),
    Match(wm_class='feh')
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def autostart():
    subprocess.run([home + "/.config/qtile/scripts/autostart.sh"])
    subprocess.run([home + "/.config/qtile/scripts/screen-saver.sh"])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
