import openai
from config import groq_api_key

client = openai.OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1"
)

async def meslek_aciklama(meslek_adi: str) -> str:
    """
    Girilen meslek hakkında Türkçe açıklama üretir.
    """
    prompt = (
        f"Sen bir kariyer rehberisin. Bana '{meslek_adi}' mesleği hakkında Türkçe bilgi ver. "
        f"Bu meslek ne iş yapar, hangi beceriler gerekir, nasıl başlanır ve geleceği nasıldır? "
        f"Motive edici, samimi ve kısa paragraf biçiminde anlat."
    )

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ GPT açıklaması alınamadı: {e}"

async def meslek_oner(ozellikler: list) -> str:
    """
    Verilen kişilik özelliklerine göre meslek önerisi üretir.
    """
    prompt = (
        f"Bir kariyer koçusun. Kişinin kişilik özellikleri şunlar: {', '.join(ozellikler)}.\n"
        f"Bu kişilik tipine uygun 2-3 meslek öner. Her biri için neden uygun olduğunu motive edici biçimde "
        f"TÜRKÇE açıklayan kısa bir TÜRKÇE metin yaz."
    )

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ GPT açıklaması alınamadı: {e}"
