from email import message
from multiprocessing import context
from os import times
from turtle import update
from telegram import Update
import telegram.ext
import schedule
import threading
import time
import requests

from config import question_interval, api_key, group_id, game_info
from triviaAPI import TriviaAPI
from dataBase import userDataBase

triviaApi = TriviaAPI()
userDB = userDataBase()

def send_msg_once(message):
    bot = telegram.Bot(api_key)
    bot.sendMessage(group_id, message)

def handle_message(update, context):
    if update.message.text == triviaApi.getAnswer():
        if triviaApi.getAccept_answers() == True:
            triviaApi.setAccept_answersOff()
            points = triviaApi.getPoints()
            update.message.reply_text("✅ Corect answer! You got " + str(points) + " points! ✅")
            sender_id = update.message.from_user
            userDB.updateUser(sender_id.id, sender_id.first_name + " " + sender_id.last_name , points)
            userDB.commit()
        else:
            update.message.reply_text("⛔ Answer already accepted! ⛔")

def nextQuestion():
    triviaApi.generateQuestion()
    send_msg_once("❓ Question: " + triviaApi.getQuestion() + " ❓")

def showTop5():
    printData = " #🔝# TOP 5 #🔝#\n"
    top5Data = userDB.getTop5()
    count = 1
    numbers_pic = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
    for user in top5Data:
        printData += f" {numbers_pic[count-1]} " + str(user[1]) + " -> " + str(user[2]) + " points" + f" {numbers_pic[count-1]}" + "\n"
        count += 1
    send_msg_once(printData)

def showInfo():
    send_msg_once(game_info)

def help(update, context):
    update.message.reply_text("""
#❔# HELP #❔#
/help - show this help
/top5 - show top 5 players
/points - show your points
""")

def top5handler(update, context):
    showTop5()

def getPoints(update, context):
    points = str(userDB.getUserPoints(update.message.from_user.id))
    if points == "None":
        send_msg_once("🔴 You have no points! 🔴")
    else:
        send_msg_once("🟢 You have " + points + " points! 🟢")

def botScheduler():
    schedule.every(question_interval).seconds.do(nextQuestion)
    schedule.every(10).minutes.do(showInfo)

    for tm in range(0, 24):
        dayHours = ""
        if tm < 10:
            dayHours = "0" + str(tm)
        else:
            dayHours += str(tm)
        dayHours += ":00"
        schedule.every().day.at(dayHours).do(showTop5)

    while True:
        schedule.run_pending()
        time.sleep(1)


### Main code
if __name__ == "__main__":
    print("Bot is up...")

    showInfo()

    userDB.createTable()

    t1 = threading.Thread(target=botScheduler)
    t1.start()

    updater = telegram.ext.Updater(api_key, use_context=True)
    disp = updater.dispatcher

    disp.add_handler(telegram.ext.CommandHandler('help', help))
    disp.add_handler(telegram.ext.CommandHandler('points', getPoints))
    disp.add_handler(telegram.ext.CommandHandler('top5', top5handler))
    disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
    
    updater.start_polling()
    updater.idle()

    print("Bot died...")

    del userDB