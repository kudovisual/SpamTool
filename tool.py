# Code by kudoo
# Link: https://github.com/kudovisual/SpamTool
import pyautogui, pyperclip, random, time
print("Tool Spam 1.0 by kudoo")
print("Link: https://github.com/kudovisual/SpamTool")
msg = input("Nhập nội dung cần spam: ").split(" || ")
n = int(input("Nhập số lần spam: "))
m = float(input("Nhập thời gian delay: "))

print("Chuẩn bị")
# Đếm ngược 5 giây:
for i in range(5,0, -1):
    print(i,end="...",flush='True')
    time.sleep(1)
print("Bắt đầu")

# Spam:
for i in range(n):
    pyperclip.copy(random.choice(msg))
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(m) # Thời gian delay
