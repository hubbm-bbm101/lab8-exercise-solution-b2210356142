import sys
users=sys.argv[2].split(',') # EMRE NURAY LİSTEDE
kişiler=open(sys.argv[1],"r").read().splitlines()
sözlük={}
for i in kişiler:
    kişiler_yeni=i.split(":")
    sözlük[kişiler_yeni[0]]=kişiler_yeni[1].split(",")

def info(user):

    try:
      print("Name: {}, University: {} ".format(user, ','.join(sözlük[user])))
    except:
      print("No record of '{}' was found".format(user))

for user in users:
  info(user)


