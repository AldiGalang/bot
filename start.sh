sudo apt install screen -y
git clone https://github.com/AldiGalang/bot.git
cd bot
sudo apt install python3 && apt install python3.12-venv && python3 -m venv myenv && source myenv/bin/activate && pip install -r requirements.txt && pyton3 bot.py
