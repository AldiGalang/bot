sudo apt update && sudo apt install screen -y
git clone https://github.com/AldiGalang/bot.git
cd bot
echo -e '#!/bin/bash\nsource myenv/bin/activate\npython3 bot.py' > run_bot.sh
chmod +x run_bot.sh
