# Creator:justice 廖振谊
# Creat time:2022/6/22 0:59
import re
websites=[r'http://www.interoem.com/messageinfo.asp?id=35',
r'http://3995503.com/class/class09/news_show.asp?id=14',
r'http://lib.wzmc.edu.cn/news/onews.asp?id=769',
r'http://www.zy-ls.com/alfx.asp?newsid=377&id=6',
r'http://www.fincm.com/newslist.asp?id=415']
for website in websites:
    result=re.match('http://([^/]*).*',website)
    print("the domain name of",website,"is",result.group(1))