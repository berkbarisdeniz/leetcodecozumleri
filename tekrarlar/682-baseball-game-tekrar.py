#isim = 682-baseball-game
#etiket = Yeşil
#tekrar_cozum = 31.03.2026
#konu = Stack, Simulation

"""
MÜHENDİSLİK NOTLARI: 682. Baseball Game

Kavramsal Temel:
Bir sürecin geçmiş adımlarına rastgele değil, her zaman "en sondan geriye doğru" 
erişim (LIFO) gerektiren klasik bir simülasyon. 'C' işlemi (Undo) ve 
'+' işlemi (son iki veriye bakma) doğrudan Stack'in tepe (top/peek) 
noktasına müdahale eder.

Elenen Alternatifler ve Trade-off'lar:
1. Sadece Değişken Tutmak (O(1) Hafıza): Soru eğer sadece "son iki sayıyı topla" 
   deseydi O(1) hafıza ile çözülebilirdi. Ancak 'C' (iptal) işlemi olduğu için, 
   iptalden sonra daha da eski geçmişe dönmemiz gerekir. Bu "sınırsız geri alma" 
   ihtiyacı doğurduğu için O(N) ekstra hafıza (Stack) ZORUNLUDUR.

Neden Bu Çözüm?
Dizi sonundan okuma (stack[-1], stack[-2]), ekleme (append) ve silme (pop) 
işlemlerinin hepsi Python listelerinde (dinamik dizilerde) O(1) zaman maliyetine 
sahiptir. Tüm liste tek turda dönüldüğü için zaman karmaşıklığı saf O(N)'dir.

Kullanım Alanları:
- Hesap makinelerindeki geçmiş işlemleri yönetme.
- Finansal terminal/log sistemlerinde hatalı girilen son işlemi iptal edip 
  bakiyeyi önceki duruma döndürme (Rollback).
"""





class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                stack.append((stack[-1])+(stack[-2]))   
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(int(stack[-1])*2)
            else:
                stack.append(int(op))
        return sum(stack)