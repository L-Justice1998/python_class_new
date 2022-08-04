# Creator:justice 廖振谊
# Creat time:2022/6/30 18:04
def get_score(self):
    print(self.score)

Score_Class=type("Score_Class",(),{"score":115,"get_score":get_score})
lzy=Score_Class()
print(hasattr(lzy,"math"))
lzy.get_score()
print(lzy)