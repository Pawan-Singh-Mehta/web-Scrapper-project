
from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests

app=Flask(__name__)
@app.route('/')
def index():
    url="https://www.businesstoday.in/"
    req=requests.get(url)

    soup=BeautifulSoup(req.content,"html.parser")
    outerdata=soup.find_all("div",class_="bn_item_title",limit=6)
    finalnews=""
    for data in outerdata:
        news=data.h3.a["title"]
        finalnews+= "\u2022" + news+ "\n"+"\n"
    return render_template("index.html",News=finalnews)
    
# print(finalnews)




