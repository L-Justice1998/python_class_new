# Creator:justice 廖振谊
# Creat time:2022/6/22 23:02
class MiniOS:
    def __init__(self,name):
        self.name=name
        self.apps=[]

    def install(self,app):
        if app.name in self.apps:
            print("app had been installed in the OS")
        else:
            app.install()
            self.apps.append(app.name)
    def __str__(self):
        return "%s has installed %s" %(self.name,str(self.apps))

class App:
    def __init__(self,name):
        self.name=name
    def install(self):
        print("%s is installing in the OS"%self.name)
        print("%s is installed in the OS"%self.name)

class Pycharm(App):
    pass

class QQ(App):
    def install(self):
        print("%s is unzipping and installed"%self.name)

OS1=MiniOS("linux")
Pycharm1=Pycharm("pycharm")
Pycharm2=Pycharm("pycharm")
QQ1=QQ("qq")
OS1.install(Pycharm1)
OS1.install(Pycharm2)
OS1.install(QQ1)
print(OS1.__str__())