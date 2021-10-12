with open("daka.txt","r") as f:

    c=f.read()
    print(c)
    a=c.replace(": ","\":\"")
    d=a.replace("\n","\",\n")

with open("daka2.text", "w")as fp:
    fp.write(d)
    print(d)


with open("daka2.text", "r") as fi:
    str=fi.readlines()
    with open("zuizhongjieguo","w")as gu:
      for x in str:
          gu.write("\""+x)








