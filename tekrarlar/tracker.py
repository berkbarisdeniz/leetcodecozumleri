from datetime import datetime, timedelta
import os
from pathlib import Path


def track_questions():
    today = datetime.now()
    print(f"Bugünün tarihi:{today.strftime('%d.%m.%Y')}")
    for path in Path('./tekrarlar').glob('*py'):
        if path.name == "tracker.py":
                continue
        
        with open(path, 'r',encoding='utf-8') as f:
             data = f.readlines()[:4]
        name, label, date_of_solved_str, subject = None, None, None, None
        date_of_repeat = None

        for row in data:
            if row.startswith("#isim"):
                name = row.split("=")[1].replace('\n','').replace('\r','').split()


            elif row.startswith("#etiket"):
                label = row.split("=")[1].replace('\n','').replace('\r','').split()

                
            elif row.startswith("#tekrar_cozum"):
                date_of_solved_str = row.split("=")[1].replace("\n",'').replace('\r','').strip()

                try:
                      date_of_solved = datetime.strptime(date_of_solved_str,'%d.%m.%Y')

                      
                      
                
                except Exception as e :
                     print(e)
            




        if label[0] == "Kırmızı" and date_of_solved:
            date_of_repeat = date_of_solved + timedelta(days=3)
            
            if date_of_repeat < today:
                print("*"*30)
                print(f"Dosya : {name[0]}")
                print(f"Etiket : {label[0]}")
                print(f"{today-date_of_solved} geçti. (kırmızı etikette 3 days, x saat görüyorsan çözmen gerek.)")
                if today-date_of_solved > timedelta(days=6):
                    print("Çok gecikti. Öncelikli!")
                print("*"*30)
        
        elif label[0] == "Sarı" and date_of_solved:
            date_of_repeat = date_of_solved + timedelta(days=7)
            
            if date_of_repeat < today:
                print("*"*30)
                print(f"Dosya : {name[0]}")
                print(f"Etiket : {label[0]}")
                print(f"{today-date_of_solved} geçti. (sarı etikette 7 days, x saat görüyorsan çözmen gerek.)")
                if today-date_of_solved > timedelta(days=10):
                    print("Çok gecikti. Öncelikli!")
                print("*"*30)

        elif label[0] == "Yeşil" and date_of_solved:
            date_of_repeat = date_of_solved + timedelta(days=30)
            
            if date_of_repeat < today:
                print("*"*30)
                print(f"Dosya : {name[0]}")
                print(f"Etiket : {label[0]}")
                print(f"{today-date_of_solved} geçti. (Yeşil etikette 30 days, x saat görüyorsan çözmen gerek.)")
                if today-date_of_solved > timedelta(days=33):
                    print("Çok gecikti. Öncelikli!")
                print("*"*30)

            


track_questions()
