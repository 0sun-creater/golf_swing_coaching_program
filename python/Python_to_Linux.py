import os
import subprocess



def JSONmaker():
    class cd:
        """Context manager for changing the current working directory"""
        def __init__(self, newPath):
            self.newPath = os.path.expanduser(newPath)

        def __enter__(self):
            self.savedPath = os.getcwd()
            os.chdir(self.newPath)

        def __exit__(self, etype, value, traceback):
            os.chdir(self.savedPath)


    with cd("~/openpose"):
        subprocess.call('./build/examples/openpose/openpose.bin --video examples/media/Camera1.avi --tracking 2 --number_people_max 1 --write_json output/', shell = True)
        subprocess.call('./build/examples/openpose/openpose.bin --video examples/media/Camera2.avi --tracking 2 --number_people_max 1 --write_json output/', shell = True)
