import urwid
import subprocess

# Define the options and their corresponding commands
options = [
    ("cancel", "None"),
    ("logout", "swaymsg exit"),
    ("sleep", "systemctl suspend"),
    ("reboot", "systemctl reboot"),
    ("shutdown", "systemctl poweroff"),
]

def menu(title, options):
    body = [urwid.Text(title), urwid.Divider()]
    for key, option in options:
        button = urwid.Button(option)
        urwid.connect_signal(button, 'click', item_chosen, key)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, user_data):
    if user_data != "cancel":
        command = options_dict[user_data]
        if command:
            subprocess.run(command.split())
    raise urwid.ExitMainLoop()

if __name__ == '__main__':
    options_dict = dict(options)
    main = urwid.Padding(menu(u'Options', options), left=2, right=2)
    top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
                        align='center', width=('relative', 40),
                        valign='middle', height=('relative', 60),
                        min_width=20, min_height=9)
    loop = urwid.MainLoop(top, palette=[('reversed', 'standout', '')])
    loop.run()
