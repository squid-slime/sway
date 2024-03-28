#!/usr/bin/env python3

import i3ipc

def set_gaps(connection, workspace, num_windows):
    gap_size = 0
    if num_windows == 1:
        gap_size = 150
    elif num_windows == 2:
        gap_size = 100
    elif num_windows >= 3:
        gap_size = 16
    
    connection.command(f'gaps inner current set {gap_size}')

def update_gaps(connection, event=None):
    current_workspace = connection.get_tree().find_focused().workspace().name
    workspaces = connection.get_tree().workspaces()
    for ws in workspaces:
        if ws.name == current_workspace:
            num_windows = len([node for node in ws.leaves() if not node.floating])
            set_gaps(connection, current_workspace, num_windows)
            break

def main():
    connection = i3ipc.Connection()
    connection.on('window::new', update_gaps)
    connection.on('window::close', update_gaps)
    connection.on('workspace::focus', update_gaps)
    connection.main()

if __name__ == '__main__':
    main()
