# run.py
import subprocess
import sys


def main():
    print("🚀 Запуск бота...")
    print("Токен загружается из .env файла")

    try:
        # Запускаем бота
        subprocess.run([sys.executable, "bot.py"])
    except KeyboardInterrupt:
        print("\n🛑 Бот остановлен")
    except Exception as e:
        print(f"❌ Ошибка: {e}")


if __name__ == "__main__":
    main()
