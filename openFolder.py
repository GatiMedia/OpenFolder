# ----- CREATE UTILITIES MENU & ASSIGN ITEMS -------------------

#IF DON'T HAVE A MENU YET

utilitiesMenu = nuke.menu('Nuke').addMenu('My Menu')

utilitiesMenu.addCommand( 'message', "nuke.message('yay, it works')", index=0 )


# Written by Attila Gasparetz based on https://community.foundry.com/discuss/topic/154100/how-to-open-folder-from-write-node

def openFolder():
    import platform
    import subprocess
    import os

    multipleNodes = nuke.selectedNodes()

    if len(multipleNodes) == 0 or len(multipleNodes) > 1:
        nuke.message("""<center><font color=orange>Select a single node with a <font color=yellow><u><a href="https://learn.foundry.com/nuke/developers/63/ndkdevguide/knobs-and-handles/knobtypes.html#knobs-knobtypes-file-knob"><font color=yellow>File</a></u><font color=orange> knob!""")

    else:
        fileNode = nuke.selectedNode()

        if fileNode.knob('file'):
            # get path to directory
            dirname = fileNode.knob('file').evaluate()
            dirname = os.path.dirname(dirname)

            operatingSystem = platform.system()

            if os.path.isdir(dirname):

                # windows
                if operatingSystem == 'Windows':
                    os.startfile(dirname)
                # mac
                elif operatingSystem == 'Darwin':
                    subprocess.Popen(['open', dirname])
                # linux
                else:
                    subprocess.Popen(['xdg-open', dirname])

            else:
                nuke.message("<center><font color=orange>The folder wasn't created yet to open!")

        else:
            nuke.message(
                """<center><font color=orange>Select a single node with a <font color=yellow><u><a href="https://learn.foundry.com/nuke/developers/63/ndkdevguide/knobs-and-handles/knobtypes.html#knobs-knobtypes-file-knob"><font color=yellow>File</a></u><font color=orange> knob!""")

utilitiesMenu.addCommand('Open Folder in file browser', 'openFolder()', shortcut='ctrl+f', index=4)
