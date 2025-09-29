import random
from colorama import Fore, Style, init

# ініціалізація для кольорів
init(autoreset=True)

# список країн і столиць
countries = ["Україна", "Франція", "Японія", "Німеччина", "Італія", "Канада", "Іспанія", "Норвегія"]
capitals = ["Київ", "Париж", "Токіо", "Берлін", "Рим", "Оттава", "Мадрид", "Осло"]

# зробимо пари країна -> столиця
quiz = list(zip(countries, capitals))
random.shuffle(quiz)

mistakes = 0
score = 0

print(Fore.CYAN + "╔════════════════════════════════════════╗")
print(Fore.CYAN + "║       🎮 Гра «Відгадай столицю» 🎮      ║")
print(Fore.CYAN + "╚════════════════════════════════════════╝\n")

for country, capital in quiz:
    answer = input(Fore.YELLOW + f"👉 Яка столиця країни {country}? ").strip()

    if answer.lower() == capital.lower():
        print(Fore.GREEN + f"✅ Правильно! {capital} — столиця {country}.\n")
        score += 1
    else:
        mistakes += 1
        print(Fore.RED + f"❌ Неправильно! Правильна відповідь: {capital}\n")
        if mistakes == 3:
            break

print(Fore.MAGENTA + "══════════════════════════════════════════")
print(Fore.CYAN + f"📊 Результат: {score} правильних відповідей, {mistakes} помилок.")
if mistakes < 3:
    print(Fore.GREEN + "🎉 Вітаю! Ви завершили гру без 3-х помилок.")
else:
    print(Fore.RED + "💀 Гру завершено! Ви зробили 3 помилки.")
print(Fore.MAGENTA + "══════════════════════════════════════════")
