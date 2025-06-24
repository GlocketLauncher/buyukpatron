sorular = [
    {
        "soru": "Kalabalık ortamlarda mı daha rahatsın, yalnızken mi?",
        "secenekler": {
            "a": "dışadönük",
            "b": "içedönük"
        }
    },
    {
        "soru": "Bir sorunu çözerken hangisini tercih edersin?",
        "secenekler": {
            "a": "analitik",
            "b": "içgüdüsel"
        }
    },
    {
        "soru": "Hangi cümle seni daha iyi tanımlar?",
        "secenekler": {
            "a": "düzenli",
            "b": "yaratıcı"
        }
    },
    {
        "soru": "Hangi ortamda daha verimli çalışırsın?",
        "secenekler": {
            "a": "bağımsız",
            "b": "takımcı"
        }
    }
]

def en_baskin_ozellik(cevaplar):
    sayac = {}
    for cevap in cevaplar:
        sayac[cevap] = sayac.get(cevap, 0) + 1
    # En çok tekrar eden 3 özelliği al
    return sorted(sayac, key=sayac.get, reverse=True)[:3]
