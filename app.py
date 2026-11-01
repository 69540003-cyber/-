
import random

print("===== NUMBER GUESSING GAME =====")
print("เกมทายตัวเลข")
print("1. Easy (ง่าย)")
print("2. Medium (ปานกลาง)")
print("3. Hard (ยาก)")

level = int(input("เลือกระดับความยาก (1-3): "))

if level == 1:
    max_number = 50
    max_attempts = 10
    level_name = "Easy"

elif level == 2:
    max_number = 100
    max_attempts = 7
    level_name = "Medium"

elif level == 3:
    max_number = 200
    max_attempts = 5
    level_name = "Hard"

else:
    print("เลือกระดับไม่ถูกต้อง!")
    exit()

number = random.randint(1, max_number)
count = 0

print("\nระดับ:", level_name)
print("ฉันสุ่มตัวเลขตั้งแต่ 1 ถึง", max_number)
print("คุณมีโอกาสทาย", max_attempts, "ครั้ง")

while count < max_attempts:

    guess = int(input("กรอกตัวเลขที่ต้องการทาย: "))
    count += 1

    if guess < number:
        print("น้อยไป! ลองใหม่")
    
    elif guess > number:
        print("มากไป! ลองใหม่")
    
    else:
        print("ถูกต้อง! คุณชนะแล้ว")
        print("คุณทายทั้งหมด", count, "ครั้ง")
        break

    print("เหลือโอกาสอีก", max_attempts - count, "ครั้ง")

if guess != number:
    print("\nหมดโอกาสแล้ว!")
    print("ตัวเลขที่ถูกต้องคือ", number)

print("\n===== GAME OVER =====")
