import json
from pathlib import Path

# file path
script_path = Path(__file__)
script_dir = script_path.parent
json_file = script_dir / "database.json"

# ---------------- LOAD ----------------
def load_file(filename=json_file):
    with open(filename, "r") as file:
        return json.load(file)

# ---------------- SAVE ----------------
def save_file(data, filename=json_file):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# ---------------- INITIALIZE ----------------
def initialize_database():
    data = {
        "snacks": [],
        "students": [],
        "sales": []
    }
    save_file(data)

# ---------------- CREATE ----------------
def create_snack(snack_id, name, category, price):
    data = load_file()
    data["snacks"].append({
        "snack_id": snack_id,
        "name": name,
        "category": category,
        "price": price
    })
    save_file(data)

def create_student(student_id, name, grade_level):
    data = load_file()
    data["students"].append({
        "student_id": student_id,
        "name": name,
        "grade_level": grade_level
    })
    save_file(data)

def create_sale(sale_id, student_id, snack_id, quantity, total_price, date, day):
    data = load_file()
    data["sales"].append({
        "sale_id": sale_id,
        "student_id": student_id,
        "snack_id": snack_id,
        "quantity": quantity,
        "total_price": total_price,
        "date": date,
        "day": day
    })
    save_file(data)

# ---------------- READ ----------------
def read_info():
    data = load_file()
    for key, value in data.items():
        print(f"--- {key.upper()} ---")
        for item in value:
            print(item)
        print()

def read_chips():
    data = load_file()
    return [s for s in data["snacks"] if s["category"] == "chips"]

def sales_by_grade(grade_level):
    data = load_file()
    student_ids = [s["student_id"] for s in data["students"] if s["grade_level"] == grade_level]
    return [s for s in data["sales"] if s["student_id"] in student_ids]

def total_quantity_today(day):
    data = load_file()
    return sum(s["quantity"] for s in data["sales"] if s["day"] == day)

# ---------------- UPDATE ----------------
def update_snack_price(snack_id, new_price):
    data = load_file()
    for s in data["snacks"]:
        if s["snack_id"] == snack_id:
            s["price"] = new_price
    save_file(data)

def update_student_grade(student_id, new_grade):
    data = load_file()
    for s in data["students"]:
        if s["student_id"] == student_id:
            s["grade_level"] = new_grade
    save_file(data)

def update_sale_quantity(sale_id, new_quantity):
    data = load_file()
    for s in data["sales"]:
        if s["sale_id"] == sale_id:
            s["quantity"] = new_quantity
    save_file(data)

# ---------------- DELETE ----------------
def delete_snack(snack_id):
    data = load_file()
    data["snacks"] = [s for s in data["snacks"] if s["snack_id"] != snack_id]
    save_file(data)

def delete_student(student_id):
    data = load_file()
    data["students"] = [s for s in data["students"] if s["student_id"] != student_id]
    save_file(data)

def delete_sale(sale_id):
    data = load_file()
    data["sales"] = [s for s in data["sales"] if s["sale_id"] != sale_id]
    save_file(data)

# ---------------- ANALYTICS ----------------
def most_popular_snack():
    data = load_file()
    counts = {}
    for s in data["sales"]:
        counts[s["snack_id"]] = counts.get(s["snack_id"], 0) + s["quantity"]
    popular_id = max(counts, key=counts.get)
    return next(snack["name"] for snack in data["snacks"] if snack["snack_id"] == popular_id)

def top_spending_grade():
    data = load_file()
    spending = {}
    for sale in data["sales"]:
        student = next(s for s in data["students"] if s["student_id"] == sale["student_id"])
        grade = student["grade_level"]
        spending[grade] = spending.get(grade, 0) + sale["total_price"]
    return max(spending, key=spending.get)

def highest_sales_day():
    data = load_file()
    day_counts = {}
    for s in data["sales"]:
        day_counts[s["day"]] = day_counts.get(s["day"], 0) + 1
    return max(day_counts, key=day_counts.get)

def most_active_student():
    data = load_file()
    counts = {}
    for s in data["sales"]:
        counts[s["student_id"]] = counts.get(s["student_id"], 0) + 1
    top_id = max(counts, key=counts.get)
    return next(st["name"] for st in data["students"] if st["student_id"] == top_id)

def average_sale():
    data = load_file()
    total = sum(s["total_price"] for s in data["sales"])
    return total / len(data["sales"])

def get_analytics():
    print("\n--- SNACK SHOP REPORT ---")
    print(f"1. Most Popular Snack: {most_popular_snack()}")
    print(f"2. Top Spending Grade: Grade {top_spending_grade()}")
    print(f"3. Busiest Day: {highest_sales_day()}")
    print(f"4. Top Customer: {most_active_student()}")
    print(f"5. Average Sale Amount: {average_sale():.2f}")

# ---------------- MAIN ----------------
def main():
    initialize_database()

    # CREATE DATA WITH NEW NAMES
    create_snack(1, "CrunchyBits", "chips", 22)
    create_snack(2, "SweetPop", "chips", 19)
    create_snack(3, "ChocoBites", "cookies", 16)
    create_snack(4, "CandyBar", "chocolate", 28)
    create_snack(5, "RiceCracker", "crackers", 14)

    create_student(1, "Liam Torres", 10)
    create_student(2, "Emma Reyes", 9)
    create_student(3, "Noah Cruz", 10)
    create_student(4, "Olivia Santos", 11)
    create_student(5, "Ava Lim", 10)

    create_sale(1, 1, 1, 2, 44, "2026-03-14", "Saturday")
    create_sale(2, 3, 3, 1, 16, "2026-03-14", "Saturday")
    create_sale(3, 2, 2, 3, 57, "2026-03-15", "Sunday")
    create_sale(4, 5, 4, 1, 28, "2026-03-15", "Sunday")
    create_sale(5, 1, 1, 1, 22, "2026-03-16", "Monday")
    create_sale(6, 4, 5, 2, 28, "2026-03-16", "Monday")

    read_info()

    print("\n*** PERFORMING UPDATES ***")
    update_snack_price(4, 30)
    update_student_grade(2, 10)
    update_sale_quantity(3, 5)

    print("\n*** PERFORMING DELETES ***")
    delete_snack(5)
    delete_student(4)
    delete_sale(6)

    print("\n--- FINAL DATABASE AFTER UPDATES AND DELETES ---")
    read_info()

    get_analytics()

    print("\n--- TRENDS & RECOMMENDATIONS ---")
    print("Trend: Grade 10 students are the top spenders.")
    print("Insight: Chips are the most popular snacks.")
    print("Strategy: Offer discounts to Grade 10 students on busy days.")

if __name__ == "__main__":
    main()