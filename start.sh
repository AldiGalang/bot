sudo apt update && sudo apt install screen -y
git clone https://github.com/AldiGalang/bot.git
screen -S gaiabot
cd bot
sudo apt install python3 python3.12-venv -y
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
python3 bot.py
