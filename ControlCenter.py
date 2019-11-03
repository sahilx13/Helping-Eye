# This is the code the control center would be running
from CenterServer import Server
from DetectionAlgorithm import GodsEye

class ControlCenter:
    def __init__(self):
        print("Running the control center")

    def start(self):
        server = Server(host="127.0.0.1", port=65001)
        flag = False
        try:
            while True:
                # starting the server program
                video = Server.start()
                eye = GodsEye(video, survivors=["person, cat, dog"], threshold=0.5)
                if eye.search():
                    flag = True
                if flag:
                    print("Survivors detected! Notifying Response team!")
        except KeyboardInterrupt:
            print("Closing the Control Center")
            Server.start()
        except:
            print("Caught unknown Exception:")
            raise