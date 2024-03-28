#!/usr/bin/env python3
import i3ipc
import notify2

# initialize notify2
notify2.init("Dynamic Gaps")

# flag to control notifications
enable_notifications = True        # CAPITALISE first letter True False

def set_gaps(connection, workspace, num_windows):
    try:
        gap_size_hoz = None            
        gap_size_ver = None            
        gap_size_inner = None          
        if num_windows == 1:
            gap_size_hoz = 500      # set horizontal gaps
            gap_size_ver = 100      # set vertical gaps
            gap_size_inner = 0      # set inner gaps
        elif num_windows == 2:      
            gap_size_hoz = 250
            gap_size_ver = 20
            gap_size_inner = 50
        elif num_windows >= 3:
            gap_size_hoz = 20
            gap_size_ver = 20
            gap_size_inner = 20

        connection.command(f'gaps horizontal current set {gap_size_hoz}; gaps vertical current set {gap_size_ver}; gaps inner current set {gap_size_inner}')

        # display notification if enabled
        if enable_notifications:
            notify2.Notification("Gaps Updated", f"Horizontal: {gap_size_hoz}, Vertical: {gap_size_ver}, Inner: {gap_size_inner}", "dialog-information").show()
    except Exception as e:
        error_message = f"An error occurred while setting gaps: {e}"
        notify2.Notification("Error", error_message, "dialog-error").show()

def update_gaps(connection, event=None):
    try:
        current_workspace = connection.get_tree().find_focused().workspace().name
        workspaces = connection.get_tree().workspaces()
        for ws in workspaces:
            if ws.name == current_workspace:
                num_windows = len([node for node in ws.leaves() if not node.floating])
                set_gaps(connection, current_workspace, num_windows)
                break
    except Exception as e:
        error_message = f"An error occurred while updating gaps: {e}"
        notify2.Notification("Error", error_message, "dialog-error").show()

def main():
    try:
        connection = i3ipc.Connection()
        connection.on('window::new', update_gaps)
        connection.on('window::close', update_gaps)
        connection.on('workspace::focus', update_gaps)
        connection.main()
    except Exception as e:
        error_message = f"An error occurred: {e}"
        notify2.Notification("Error", error_message, "dialog-error").show()

if __name__ == '__main__':
    main()
