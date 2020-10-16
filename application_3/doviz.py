import requests
import json

htppGet = requests.get("https://api.exchangeratesapi.io/latest?base=TRY")
# htppGet = htppGet.text
# print(htppGet)
# print("-"*50)
htppGet = json.loads(htppGet.text)
#print(type(htppGet)) --> dict
#print("Base = ",htppGet["base"]) --> TRY

print("DUMAN DOVİZ HOŞGELDİNİZ\n".center(50))
cevirilen = input("ÇEVİRMEK İSTEDİĞİNİZ PARA BİRİMİ: ")
donusturelecek = input("DÖNÜŞTÜRMEK İSTEDİĞİNİZ PARA BİRİMİ: ")
para = float(input("ÇEVİRMEK İSTEDİĞİNİZ MİKTAR GİRİN: "))
htppGet_Cevirilen = requests.get("https://api.exchangeratesapi.io/latest?base="+cevirilen)
htppGet_Cevirilen = json.loads(htppGet_Cevirilen.text)
doviz = para * float(htppGet_Cevirilen["rates"][donusturelecek])
print("sonuc:",doviz)
