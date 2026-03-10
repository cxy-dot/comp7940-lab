#!/bin/bash
cd ~/chatbot_comp7940 || exit 1
git pull origin main
pkill -f "python chatbot.py" || true
nohup ~/chatbot_comp7940/venv/bin/python chatbot.py > app.log 2>&1 &