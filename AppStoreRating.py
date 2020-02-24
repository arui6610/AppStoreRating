#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import json,datetime
import requests,xmltodict
from GoogleFreeTrans import Translator

def countryCode():
    return {
        " Armenia":"am",
        " Bahrain":"bh",
        " البحرين": "bh-ar",
        " Botswana": "bw",
        " Cameroun": "cm",
        " République Centrafricaine": "cf",
        " Côte d'Ivoire": "ci",
        " Egypt": "eg",
        " مصر": "eg-ar",
        " Guinea-Bissau": "gw",
        " Guinée": "gn",
        " Guinée Equatoriale": "gq",
        " India": "in",
        " Israel": "il",
        " Jordan": "jo",
        " الأردن": "jo-ar",
        " Kenya": "ke",
        " Kuwait": "kw",
        " الكويت": "kw-ar",
        " Madagascar": "mg",
        " Mali": "ml",
        " Maroc": "ma",
        " Maurice": "mu",
        " Mozambique": "mz",
        " Niger": "ne",
        " Nigeria": "ng",
        " Oman": "om",
        " عُمان": "om-ar",
        " Qatar": "qa",
        " قطر": "qa-ar",
        " Saudi Arabia": "sa",
        " المملكة العربية السعودية": "sa-ar",
        " Sénégal": "sn",
        " South Africa": "za",
        " Tunisie": "tn",
        " Uganda": "ug",
        " United Arab Emirates": "ae",
        " الإمارات العربية المتحدة": "ae-ar",
        " Australia": "au",
        " 中国大陆": "cn",
        " Hong Kong (English)": "hk/en",
        " 香港": "hk",
        " Indonesia": "id",
        " 日本": "jp",
        " 대한민국": "kr",
        " 澳門": "mo",
        " Malaysia": "my",
        " New Zealand": "nz",
        " Philippines": "ph",
        " Singapore": "sg",
        " 台灣": "tw",
        " ไทย": "th",
        " Vietnam": "vn",
        " België": "benl",
        " Belgique": "befr",
        " България": "bg",
        " Česko": "cz",
        " Danmark": "dk",
        " Deutschland": "de",
        " Eesti": "ee",
        " España": "es",
        " France": "fr",
        " Ελλάδα": "gr",
        " Hrvatska": "hr",
        " Ireland": "ie",
        " Italia": "it",
        " Latvija": "lv",
        " Liechtenstein": "li",
        " Lietuva": "lt",
        " Luxembourg": "lu",
        " Magyarország": "hu",
        " Malta": "mt",
        " Moldova": "md",
        " Montenegro": "me",
        " Nederland": "nl",
        " North Macedonia": "mk",
        " Norge": "no",
        " Österreich": "at",
        " Polska": "pl",
        " Portugal": "pt",
        " România": "ro",
        " Россия": "ru",
        " Slovensko": "sk",
        " Slovenia": "si",
        " Schweiz": "chde",
        " Suisse": "chfr",
        " Suomi": "fi",
        " Sverige": "se",
        " Türkiye": "tr",
        " UK": "uk",
        " Anguilla": "lae",
        " Antigua & Barbuda": "lae",
        " Argentina": "la",
        " Barbados": "lae",
        " Belize": "lae",
        " Bermuda": "lae",
        " Bolivia": "la",
        " Brasil": "br",
        " British Virgin Islands": "lae",
        " Cayman Islands": "lae",
        " Chile": "cl",
        " Colombia": "co",
        " Costa Rica": "la",
        " Dominica": "lae",
        " República Dominicana": "la",
        " Ecuador": "la",
        " El Salvador": "la",
        " Grenada": "lae",
        " Guatemala": "la",
        " Guyana": "lae",
        " Honduras": "la",
        " Jamaica": "lae",
        " México": "mx",
        " Montserrat": "lae",
        " Nicaragua": "la",
        " Panamá": "la",
        " Paraguay": "la",
        " Perú": "la",
        " St. Kitts & Nevis": "lae",
        " St. Lucia": "lae",
        " St. Vincent & The Grenadines": "lae",
        " Suriname": "lae",
        " The Bahamas": "lae",
        " Trinidad & Tobago": "lae",
        " Turks & Caicos": "lae",
        " Uruguay": "la",
        " Venezuela": "la",
        " América Latina y el Caribe (Español)": "la",
        " Latin America and the Caribbean (English)": "lae",
        " Canada (English)": "ca",
        " Canada (Français)": "ca/fr",
        " Puerto Rico (English)": "lae",
        " Puerto Rico (Español)": "la",
        " United States": "us",
    }

def parser(appid,appname,zone):
    print("["+appname+"]")
    page = 1
    count = 0
    translator = Translator.translator(src='auto', dest='zh-CN')
    # 默认循环10次，获取500条数据
    while page < 11:
        myurl = "https://itunes.apple.com/"+zone+"/rss/customerreviews/page=" + str(page) + "/id=" + str(appid) + "/sortby=mostrecent/xml"
        response = requests.request("GET",myurl)
        xmlstr = response.text
        xmlparse = xmltodict.parse(xmlstr)
        myjson = json.loads(json.dumps(xmlparse, indent=1))
        print(myurl)
        if "entry" in myjson["feed"]:
            count += len(myjson["feed"]["entry"])
            for i in myjson["feed"]["entry"]:
                # (id) id - i["id"]
                id = i["id"]
                # (时间) time - i["updated"]
                updated = i["updated"]
                # (用户) name - i["author"]["name"]
                name = i["author"]["name"]
                # (标题) title - i["title"]
                title = i["title"]
                # (内容) content - i["content"]
                content = ''
                contentTrans = ''
                for c in i["content"]:
                    if c["@type"] == "text":
                        content =  c["#text"]
                # (评分) rating - i["im:rating"]
                rating = i["im:rating"]
                # (版本) im:version - i["im:version"]
                version =  i["im:version"]
                payload = {
                    'review':{
                        "id": int(id),
                        "author": name,
                        "title": title,
                        "titleTrans":translator.translate(title),
                        "contentTrans":translator.translate(content),
                        "content": content,
                        "star": int(rating),
                        "time": updated,
                        "appId": appid,
                        "appName": appname,
                        "appVersion": version,
                        "language":zone
                    }
                }
                payload = json.dumps(payload)
                print(payload)
                # 这里。。。。。。。。
            page = page + 1
        else:
            break
    if count == 0:
        print("未获取到任何数据。")
    else:
        print(str(count) + "条数据")

def task(appid,appname):
    codes = countryCode().values()
    codes = list(set(codes))
    for val in codes:
        try:
            now = datetime.datetime.now()
            ts = now.strftime('%Y-%m-%d %H:%M:%S')
            print(val,ts)
            parser(appid,appname,val)
        except Exception as e:
            print(val,"失败",e,"\n\n")
        else:
            print(val,"结束","\n\n")

def timing(appid,appname):
    from apscheduler.schedulers.blocking import BlockingScheduler
    scheduler = BlockingScheduler()
    scheduler.add_job(task(appid,appname), 'interval', days=1, id='appstore_score')
    scheduler.start()


if __name__ == '__main__':
    appid = 414478124
    appname = "微信"
    task(appid,appname)
