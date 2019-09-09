
from ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/184-4","103808","1f246b6e2d1c48aa919228586d68db37" )
r.addFilePara("image","/Users/yangchao/Desktop/乐学/img副本.png")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
print(res.text)     #  返回信息