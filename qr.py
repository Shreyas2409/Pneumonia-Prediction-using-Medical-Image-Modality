import pyqrcode

s = input("enter link ")
url=pyqrcode.create(s)
url.svg("weblink.svg",scale=10)
