import requests
from pprint import pprint

def MSMYeditor(chapter, verse):
    editor = "uzb-muhammadsodikmu"
    url=f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{editor}/{chapter}/{verse}.json"
    r = requests.get(url)
    res = r.json()
    pprint(res)
    return res['chapter'], res['verse'], res['text']

def AlouddinMeditor(chapter, verse):
    editor = "uzb-alauddinmansour"
    url=f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{editor}/{chapter}/{verse}.json"
    r = requests.get(url)
    res = r.json()
    pprint(res)
    return res['chapter'], res['verse'], res['text']

def Quran_la(chapter, verse):
    editor = "ara-quran-la"
    url=f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{editor}/{chapter}/{verse}.json"
    r = requests.get(url)
    res = r.json()
    pprint(res)
    return res['chapter'], res['verse'], res['text']

def Jalaliddin(chapter, verse):
    editor = "ara-jalaladdinalmah"
    url=f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{editor}/{chapter}/{verse}.json"
    r = requests.get(url)
    res = r.json()
    pprint(res)
    return res['chapter'], res['verse'], res['text']