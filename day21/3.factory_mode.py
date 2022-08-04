# Creator:justice 廖振谊
# Creat time:2022/6/22 20:51
class instrument():
    def play(self):
        pass
        print("the instrument is playing")
    def put(self):
        print("the instrument is put in the study")

class piano(instrument):
    def play(self):
        print("the piano is playing")
    def put(self):
        print("the piano is put in the study")

class violin(instrument):
    def play(self):
        print("the violin is playing")
    def put(self):
        print("the violin is put in the study")

class Factory_mode(instrument):
    def __init__(self):
        self.dict={"violin":violin,"piano":piano}
    def create(self,instrument_name):
        return self.dict[instrument_name]()

i=Factory_mode()
instru=i.create("piano")
instru.play()

