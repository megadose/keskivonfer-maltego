from keskivonfer import getInfo
from MaltegoTransform import *
trx = MaltegoTransform()
try:
    if len(sys.argv[2].split('#vintedExtensionWebsite=')[1].split("#id")[0])<=1:
        trx.addEntity("maltego.Phrase","vintedExtensionWebsite is required !")
        print(trx.returnOutput())
        exit()

except:
    trx.addEntity("maltego.Phrase","vintedExtensionWebsite is required !")
    print(trx.returnOutput())
    exit()

infos=getInfo(sys.argv[1],sys.argv[2].split('#vintedExtensionWebsite=')[1].split("#id")[0])
vintedprofile=trx.addEntity("megadose.vinted",str(infos["login"]))
vintedprofile.addProperty(fieldName="id",value=str(infos["id"]))
vintedprofile.addProperty(fieldName="anon_id",value=str(infos["anon_id"]))
vintedprofile.addProperty(fieldName="vintedExtensionWebsite",value=sys.argv[2].split('#vintedExtensionWebsite=')[1].split("#id")[0])
if infos["real_name"]!=None:
    vintedprofile.addProperty(fieldName="real_name",value=str(infos["real_name"]))
if infos["email"]!=None:
    trx.addEntity("maltego.EmailAddress",str(infos["email"]))
if infos["facebook_user_id"]!=None:
    vintedprofile.addProperty(fieldName="facebook_user_id",value=str(infos["facebook_user_id"]))
if infos["gender"]!=None:
    vintedprofile.addProperty(fieldName="gender",value=str(infos["gender"]))
if infos["birthday"]!=None:
    vintedprofile.addProperty(fieldName="birthday",value=str(infos["birthday"]))
if infos["item_count"]!=None:
    vintedprofile.addProperty(fieldName="item_count",value=str(infos["item_count"]))
if infos["followers_count"]!=None:
    vintedprofile.addProperty(fieldName="followers_count",value=str(infos["followers_count"]))
if infos["following_count"]!=None:
    vintedprofile.addProperty(fieldName="following_count",value=str(infos["following_count"]))
if infos["created_at"]!=None:
    vintedprofile.addProperty(fieldName="created_at",value=str(infos["created_at"]))
if infos["last_loged_on_ts"]!=None:
    vintedprofile.addProperty(fieldName="last_loged_on_ts",value=str(infos["last_loged_on_ts"]))


if infos["country_title"]!=None:
    if infos["city"]!=None:
        country=infos["country_title"]
        infos["country_title"] = str(infos["city"])+","+str(infos["country_title"])
    location = trx.addEntity("maltego.Location",infos["country_title"])
    location.addProperty(fieldName="countrycode",value=str(country))

if infos["photo"]["url"]!=None:
    vintedprofile.addProperty(fieldName="photo",value=str(infos["photo"]["url"]))
else :
    vintedprofile.addProperty(fieldName="photo",value=str(infos["photo"]))

for v in infos["verification"]:
    toprint=""
    for i in infos["verification"][v]:
        toprint+=str(i)+" : "+str(infos["verification"][v][i])
    trx.addEntity("keskivonfer.SocialNetwork",v).setNote(toprint)

print(trx.returnOutput())
