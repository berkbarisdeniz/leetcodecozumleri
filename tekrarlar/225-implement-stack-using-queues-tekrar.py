#isim = 225-implement-stack-using-queues
#etiket = Kırmızı
#tekrar_cozum = 03.04.2026
#konu = Stack, Queue, Design

"""
MÜHENDİSLİK NOTLARI: 225. Implement Stack using Queues

Kavramsal Temel:
Problem, "Kısıtlı yetkilerle tersine mühendislik" yapmaya dayanır. 
Elimizde sadece FIFO (İlk Giren İlk Çıkar) kuralıyla çalışan bir Kuyruk (Queue) var 
ancak bizden LIFO (Son Giren İlk Çıkar) kuralıyla çalışan bir Yığın (Stack) taklidi 
yapmamız isteniyor. 

Elenen Alternatifler ve Trade-off'lar:
1. İki Kuyruk Kullanmak (O(N) Push, O(N) Hafıza): Yeni elemanı yedek kuyruğa ekleyip, 
   asıl kuyruktakileri arkasına dizip sonra isimlerini değiştirmek (Swap). Çalışır 
   ama gereksiz yere ekstra bellek (O(N)) harcar.
2. Normal Liste Pop() Kullanmak: Doğrudan kural ihlali (Hile).

Neden Tek Kuyruk + Döndürme (Rotation) Mimarisi?
- Hem O(1) hafıza harcar (ekstra kuyruk açmayız), hem de kodu çok daha temiz tutar.
- Kural şudur: "Yeni elemanı kuyruğun arkasına ekle (append), sonra içerideki tüm 
  eski elemanları tek tek önden kopar (popleft) ve hemen arkaya geri ekle (append)."
- Bu döngü bittiğinde, en son eklenen eleman sihirli bir şekilde kuyruğun EN BAŞINA 
  geçmiş olur. Artık pop() istendiğinde sadece önden eleman vererek (popleft) 
  Stack kuralını %100 simüle etmiş oluruz.

Kullanım Alanları:
- Gerçek dünya sistemlerinde pek yeri yoktur (Stack lazımsa Stack kullanılır).
- Tamamen mülakatlarda adayın "Veri yapılarının çalışma kurallarını bükebilme" ve 
  "Sınırlı kaynakla çözüm üretebilme" zekasını ölçmek için kullanılan bir eşik sorusudur.
"""





from collections import deque
class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        for num in range(len(self.stack)-1):
            self.stack.append(self.stack[0])
            self.stack.popleft()
        
        

    def pop(self) -> int:
        return self.stack.popleft()

        

    def top(self) -> int:
            return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()