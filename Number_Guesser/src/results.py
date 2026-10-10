import os
from datetime import datetime

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SRC_DIR)
RESULTS_FILE = os.path.join(PROJECT_DIR, "results.txt")

DIFFICULTY_LEVELS = {
    "1": "Easy",
    "2": "Medium",
    "3": "Hard"
}

def store_results(id, difficulty, score):
    '''ذخیره نتیحه هر بازی در فایل'''
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(RESULTS_FILE, "a") as f:
        f.write(f"{id},{difficulty},{score},{date}\n")
        
def load_results(user_id):
    """همه بازی های یک کاربر رو لیست میکنه"""
    results = []
    if not os.path.exists(RESULTS_FILE):
        return results
    
    with open(RESULTS_FILE, "r") as f:
        
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            uid , difficulty, score, date = line.split(",")

            if uid == user_id:
                results.append({'difficulty': DIFFICULTY_LEVELS.get(difficulty, difficulty), 'score': int(score), 'date': date})
    return results

def history_game(user_id):
    '''نمایش بازی های قبلی کاربر'''
    results_id = load_results(user_id)
    if not results_id:
        print("No game history found.")
        return

    print(f"Game history for user {user_id}:")
    for i, result in enumerate(results_id, start=1):
        print(f"{i}. Difficulty: {result['difficulty']}, Score: {result['score']}, Date: {result['date']}")

def display_results(user_id):
    ''' بعداً می‌توانیم آمار کلی مثل میانگین حدس‌ها را اینجا اضافه کنیم'''
    results = load_results(user_id)
    if not results:
        print("No results to show.")
        return
    avg = sum(r["score"] for r in results) / len(results)
    print(f"Games played: {len(results)}, average score: {avg:.1f}")