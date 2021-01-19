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
# SOFTWARE.

from typing import List  # noqa: F401
import subprocess
import socket
import os
import re
from libqtile import bar, layout, widget,hook
from libqtile.config import KeyChord, Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy

mod = "mod4"
terminal = "alacritty"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),


    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod, "shift"], "d", lazy.spawn("rofi -show drun -show-icons -config ~/.config/rofi/themes/dt-dmenu.rasi -display-drun \"Run: \" -drun-display-format \"{name}\""),
             desc='rofi launcher'
             ),
    Key([mod], "Tab", lazy.spawn("rofi -show window -show-icons"),
    desc='tab menu'
    ),
    Key([mod],"d", lazy.spawn("rofi -show drun -show-icons -config ~/.config/rofi/themes/dt-center.rasi -display-drun \"Run: \" -drun-display-format \"{name}\""),
             desc='rofi launcher'),

    # Toggle between different layouts as defined below "", "", "", "", "", ""
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawn("rofi -show file-browser-extended  -show-icons"),
        desc=""),


    Key([mod],"w",lazy.group[""].toscreen()),
    Key([mod],"c",lazy.group["</>"].toscreen()),
    Key([mod],"x",lazy.group["⌨"].toscreen()),
    Key([mod],"v",lazy.group["💻"].toscreen()),
    Key([mod],"p",lazy.group["⛁"].toscreen()),
    Key([mod],"m",lazy.group["♬"].toscreen()),

    Key([mod, "shift"], "w", lazy.window.togroup("")),
    Key([mod, "shift"], "c", lazy.window.togroup("</>")),
    Key([mod, "shift"], "x", lazy.window.togroup("⌨")),
    Key([mod, "shift"], "v", lazy.window.togroup("💻")),
    Key([mod, "shift"], "p", lazy.window.togroup("⛁")),
    Key([mod, "shift"], "m", lazy.window.togroup("♬")),


    Key([mod], "a", lazy.spawn("firefox")),
    Key([mod], "z", lazy.spawn("code")),
    Key([mod], "e", lazy.spawn("pamac-manager")),
    Key([mod], "q", lazy.spawn("thunar")),

       Key([mod], "h",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),

    Key([mod], "l",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),


    Key([mod, "shift"], "k",
             lazy.layout.shuffle_down(),
             desc='Move windows down in current stack'
             ),
    Key([mod, "shift"], "Down",
             lazy.layout.shuffle_down(),
             desc='Move windows down in current stack'
             ),


    Key([mod, "shift"], "j",
             lazy.layout.shuffle_up(),
             desc='Move windows up in current stack'
             ),

    Key([mod, "shift"], "Up",
             lazy.layout.shuffle_up(),
             desc='Move windows up in current stack'
             ),

    Key([mod, "shift"], "Left",
             lazy.layout.shuffle_left(),
             desc='Move windows up in current stack'
             ),
    Key([mod, "shift"], "Right",
             lazy.layout.shuffle_right(),
             desc='Move windows up in current stack'
             ),



    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),


]

group_names = [("", {'layout': 'monadtall'}),
               ("⌨", {'layout': 'monadtall'}),
               ("</>", {'layout': 'monadtall'}),
               ("💻", {'layout': 'monadtall'}),
               ("⛁", {'layout': 'monadtall'}),
               ("♬", {'layout': 'monadtall'}),]


groups = [Group(name, **kwargs) for name, kwargs in group_names]



for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }
layouts = [
    #layout.Max(),
    #layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme)
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

colors = [["#282c34", "#282c34"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"], # color for the even widgets
          ["#e1acff", "#e1acff"]]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                       filename = "~/.config/qtile/icons/manjaro.svg",
                       padding =2
                       ),
                widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 16,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 10,
                       padding_x = 10,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[3],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[0],
                       other_screen_border = colors[0],
                       foreground = colors[2],
                       background = colors[0]
                       ),
                widget.Sep(
                       linewidth = 0,
                       padding = 1,
                       foreground = colors[5],
                       background = colors[2]
                       ),
                widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 10
                       ),
                widget.Chord(
                    chords_colors={
                        'launch': (colors[4], colors[6]),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
                       text = " 📅 ",
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0,
                       fontsize = 14
                       ),
                widget.Clock(
                    foreground = colors[2],
                    background = colors[0],
                    padding = 3,
                    format='%A,  %b %d - %I:%M %p  '
                ),
                widget.Sep(
                       linewidth = 0,
                       padding = 1,
                       foreground = colors[5],
                       background = colors[2]
                       ),
                widget.TextBox(
                    text = "🎙️",
                    padding = 2,
                    mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('pavucontrol')},
                    foreground = colors[6],
                    background = colors[0],
                    fontsize = 13
                    ),
                widget.Systray(
                    background = colors[0],
                    padding = 2
                ),
                widget.QuickExit(
                    default_text= "🔑",
                    fontsize= 16,
                    countdown_format= '{}',
                    foreground = colors[4],
                    background = colors[0],
                    padding = 3
                ),

            ],
            20,
        ),
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
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
