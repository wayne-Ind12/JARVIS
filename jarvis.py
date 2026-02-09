import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters, CommandHandler

# --- CONFIGURACIÓN ---
TELEGRAM_TOKEN = '8109029152:AAFH9G-pLNDht9caP43tErMfVnVypE-P9Xw'
GEMINI_API_KEY = 'AIzaSyDQ8Z9HV2An4zXoCUY5zz8zpjDuFsZcFNc'

def obtener_modelo_valido():
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models?key={GEMINI_API_KEY}"
        response = requests.get(url)
        modelos = response.json()
        if "models" in modelos:
            for m in modelos["models"]:
                if "generateContent" in m["supportedGenerationMethods"]:
                    return m["name"].split("/")[-1]
    except: pass
    return "gemini-1.5-flash"

MODELO_ACTIVO = obtener_modelo_valido()

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODELO_ACTIVO}:generateContent?key={GEMINI_API_KEY}"
    
    # PERSONALIDAD EQUILIBRADA: Amable pero no pesado.
    personalidad = (
        "Eres JARVIS, el asistente de Guillermo. Tu tono es sofisticado y servicial. "
        "Responde de forma natural y amable, pero sé conciso. "
        "No escribas párrafos gigantes a menos que Guillermo te pida una explicación detallada."
    )

    payload = {"contents": [{"parts": [{"text": f"{personalidad}\n\nGuillermo: {user_text}"}]}]}

    try:
        response = requests.post(url, json=payload)
        result = response.json()
        if "candidates" in result:
            await update.message.reply_text(result["candidates"][0]["content"]["parts"][0]["text"])
    except Exception as e:
        print(f"Error: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Sistemas en línea. A su servicio, Guillermo.")

if __name__ == '__main__':
    # El 'drop_pending_updates' limpia los mensajes viejos para evitar el error de conflicto
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), chat))
    
    print(f"--- JARVIS LISTO (Modelo: {MODELO_ACTIVO}) ---")
    app.run_polling(drop_pending_updates=True)