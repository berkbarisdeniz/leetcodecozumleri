#isim = 49-group-anagrams
#etiket = Yeşil
#tekrar_cozum = 13.04.2026
#konu = Categorization by Hash, Frequency Array






"""
1. Tekniğin Adı Nedir?Bu tekniğin literatürdeki adı "Categorization by Hash" (Hash Map ile Gruplama) ve "Frequency Array" (Frekans Dizisi) kombinasyonudur.
2. Buradan Ne Öğrenmeliydin? (Kalıcı Zihin Notları)Kodun tamamını unut, sadece şu üç mühendislik kuralı aklında kalsın:
Kural 1: Sıralamak ($O(N \log N)$) ameleliktir, Saymak ($O(N)$) mühendisliktir. * "İki kelime aynı harflerden mi oluşuyor?" sorusunu duyduğun an aklına word.sort() gelmesin. Hemen o 26 elemanlı listeyi ([0]*26) ve ord(harf) - 97 formülünü hatırla. Bu formül, İngilizce alfabe sorularının altın anahtarıdır.
Kural 2: Sözlüğün (Hash Map) kapısından sadece "Beton" girer.Elde ettiğin o 26'lık listeyi ([] - oyun hamuru) asla bir sözlüğe etiket (Key) yapamazsın. Onu anında tuple() ile dondurup betona çevirmen gerektiğini unutma. (Hatırlarsan bu kuralı sen kendi mantığınla çözerken keşfetmiştik).
Kural 3: defaultdict hayat kurtarır.Sözlükte "bu anahtar var mı, yoksa yeni liste açayım, varsa içine ekleyeyim" if/else ameleliğine girmek yerine, defaultdict(list) kullanarak işi tek satırda (hash_map[key].append(kelime)) bitirebileceğini gördün.
3. Bu Teknik Başka Nerelerde Karşına Çıkar?Bu "26'lık sayaç + Tuple + Hash Map" silahını şu tarz durumlarda direkt cebinden çıkaracaksın:Anagram Soruları: (Şu an çözdüğün gibi).Permütasyon Soruları: "Bir kelimenin (örneğin 'ab') permütasyonu, başka bir uzun stringin ('eidbaooo') içinde geçiyor mu?" (LeetCode 567). 
Burada da o 26'lık sayacı kullanıp "ikisinin sayacı (tuple'ı) birbirine eşit mi?" diye bakacaksın.Gruplama Soruları: "Elimde bir sürü veri var, ortak özelliği olanları aynı sepete at" diyen her patron/sistem talebinde (tıpkı senin veri tabanındaki bot verilerini gruplaman gerekeceği durumlar gibi)."""













class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash = {}
        
        for word in strs:
            key = [0]*26
            for char in word:
                idx = ord(char) - ord('a')
                key[idx] += 1

            key = tuple(key)    
            if key in hash:
                hash[key].append(word)
            else:
                hash[key] = [word]

        return list(hash.values())
