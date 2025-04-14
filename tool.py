# telegram: @kudo1004
# Link: https://github.com/kudovisual/SpamTool
import pyautogui, pyperclip, random, time
print("Tool Spam 2.0 by kudodz")
print("Link: https://github.com/kudovisual/SpamTool")
print("BẢN 2.0: FIX LỖI BỊ SAI CHỖ")
msg = input("Nhập nội dung cần spam: ").split(" || ")
spam_quantity = int(input("Nhập số lần spam: "))
delay = float(input("Nhập thời gian delay: "))

print("Chuẩn bị")
for i in range(5,0, -1):
    print(i,end="...",flush='True')
    time.sleep(1)
print("Bắt đầu!")

for i in range(spam_quantity):
    pyperclip.copy(random.choice(msg))
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(delay)
