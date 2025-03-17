import aiohttp, asyncio, re
from colorama import init, Fore

init(autoreset=True)

# Banner Program
print(f"{Fore.LIGHTWHITE_EX}=" * 50)
print(f"{Fore.LIGHTWHITE_EX}             GAIANET - AUTO CHATBOT AI               ")
print(f"{Fore.LIGHTWHITE_EX}=" * 50)
print(f"{Fore.LIGHTGREEN_EX}Author   : Muhammad Andre Syahli")
print(f"{Fore.LIGHTBLUE_EX}Telegram : https://t.me/yaelahmas")
print(f"{Fore.LIGHTWHITE_EX}Github   : https://github.com/yaelahmas")
print(f"{Fore.LIGHTWHITE_EX}=" * 50)

# Meminta API Key dari user
while True:
    api_keys_input = input(f"{Fore.LIGHTMAGENTA_EX}📝 Masukkan API Keys (pisahkan dengan koma): {Fore.LIGHTWHITE_EX}").strip()
    API_KEYS = [key.strip() for key in api_keys_input.split(",") if key.strip()]
    if API_KEYS:
        break
    print(f"{Fore.LIGHTRED_EX}🚨 API Key tidak boleh kosong. Silakan coba lagi.")

# Mengatur domain ke dharma.gaia.domains secara default
URLS = ["dharma.gaia.domains"]

print(f"{Fore.LIGHTCYAN_EX}🌍 Chat Domain: {Fore.LIGHTWHITE_EX}{URLS[0]}")
print(f"{Fore.LIGHTWHITE_EX}=" * 50)

# Memuat daftar pertanyaan dari file
def load_questions(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.LIGHTRED_EX}🚨 File {file_path} not found!")
        return []

QUESTIONS = load_questions("file_questions.txt")

if not QUESTIONS:
    print(f"{Fore.LIGHTRED_EX}🚨 Tidak ada pertanyaan ditemukan. Program dihentikan!")
    exit()

class ChatBot:
    def __init__(self):
        self.api_key_index = 0

    def get_next_api_key(self):
        api_key = API_KEYS[self.api_key_index]
        self.api_key_index = (self.api_key_index + 1) % len(API_KEYS)
        return api_key

    async def send_question(self, question: str, max_retries=5):
        retries = 0
        while retries < max_retries:  
            api_key = self.get_next_api_key()
            base_url = URLS[0]
            
            data = {
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question}
                ]
            }

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
            }
            
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.post(f"https://{base_url}/v1/chat/completions", headers=headers, json=data, timeout=120) as response:
                        response.raise_for_status()
                        result = await response.json()
                        answer = result["choices"][0]["message"]["content"]
                        
                        print(f"{Fore.LIGHTGREEN_EX}💬 Answer   : {Fore.LIGHTWHITE_EX}{answer}")
                        print(f"{Fore.LIGHTWHITE_EX}=" * 50)
                        return answer
                except Exception as e:
                    retries += 1
                    print(f"{Fore.LIGHTRED_EX}🚨 Error: {str(e)} - {Fore.LIGHTYELLOW_EX}(Attempt {retries}/{max_retries})")
                    await asyncio.sleep(5)
        return None

async def main():
    bot = ChatBot()
    for index, question in enumerate(QUESTIONS, start=1):
        print(f"{Fore.LIGHTBLUE_EX}📝 Question : {Fore.LIGHTWHITE_EX}{question}")
        await bot.send_question(question)
        if index < len(QUESTIONS):
            await asyncio.sleep(10)  # Tunggu sebelum pertanyaan berikutnya

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print(f"{Fore.LIGHTRED_EX}🛑 Program dihentikan oleh user.")
