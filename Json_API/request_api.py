import requests
# requesting an image from xkcd.com/353/ website to read(request.get) and write(to write in binary format)
r=requests.get("http://imgs.xkcd.com/comics/circuit_diagram.png")
print(r)
print(r.status_code)
# writing the image in binary format
f=open("D:\pyth_config\Sample1.png",'wb')
f.write(r.content)
print(r.content)
f.close()
