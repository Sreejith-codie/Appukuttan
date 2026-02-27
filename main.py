from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler,
    MessageHandler, filters, ContextTypes
)

from config import BOT_TOKEN
from ai_brain import get_ai_reply
from task_manager import add_task, get_tasks, delete_task
from health_tracker import update_health
from income_tracker import set_goal, update_income
from mood_tracker import update_mood

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "BROAI Activated 😎🔥\nYour life upgrade begins now."
    )

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    task = " ".join(context.args)
    add_task(update.message.from_user.id, task)
    await update.message.reply_text("Task added. No excuses now 😌")

async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tasks = get_tasks(update.message.from_user.id)
    if tasks:
        msg = "\n".join([f"{t[0]}. {t[1]}" for t in tasks])
        await update.message.reply_text(msg)
    else:
        await update.message.reply_text("No tasks. Suspicious behavior 👀")

async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    task_id = int(context.args[0])
    delete_task(task_id)
    await update.message.reply_text("Task removed.")

async def health(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sleep = int(context.args[0])
    water = int(context.args[1])
    workout = int(context.args[2])
    update_health(update.message.from_user.id, sleep, water, workout)
    await update.message.reply_text("Health updated. Drink water now.")

async def goal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    goal_amount = int(context.args[0])
    set_goal(update.message.from_user.id, goal_amount)
    await update.message.reply_text("Income goal set. Time to grind 💰")

async def mood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mood = context.args[0]
    update_mood(update.message.from_user.id, mood)
    await update.message.reply_text(f"Mood saved: {mood}")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    reply = get_ai_reply(user_message)
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("list", list_tasks))
app.add_handler(CommandHandler("delete", delete))
app.add_handler(CommandHandler("health", health))
app.add_handler(CommandHandler("goal", goal))
app.add_handler(CommandHandler("mood", mood))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

app.run_polling()