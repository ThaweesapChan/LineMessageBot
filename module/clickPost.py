import pyautogui
import time

def clickPost(targetX,targetY,distanceX,distanceY,numItems,numLine,numPage,minuteToPost):
    second = minuteToPost*60
    time.sleep(15)
    while True:
        for r in range(numPage):
            print("numPage ",r+1)
            for i in range(numLine):
                if i == 0:
                    print("แถวที่ 1 ")
                    for i in range(numItems):
                        #คลิกซ้ายและขวาที่ตำแหน่งของข้อความ
                        pyautogui.click(targetX + (distanceX * i), targetY, button='left')
                        pyautogui.click(targetX+(distanceX * i), targetY, button='right')
                        time.sleep(1)
                        # คลิกขวาและซ้ายที่ตำแหน่งของข้อความ "ประกาศ" ของแถวที่ 1
                        pyautogui.click(targetX + (distanceX * i) + 70, targetY + 230, button='left')
                if i == 1:
                    print("แถว 2 ")
                    for i in range(numItems):
                        #คลิกซ้ายและขวาที่ตำแหน่งของข้อความ
                        pyautogui.click(targetX + (distanceX * i), targetY + distanceY, button='left')
                        pyautogui.click(targetX+(distanceX * i), targetY + distanceY, button='right')
                        time.sleep(1)
                        # คลิกขวาและซ้ายที่ตำแหน่งของข้อความ "ประกาศ" ของแถวที่ 2
                        pyautogui.click(targetX + (distanceX * i) + 70, targetY + distanceY + 230, button='left')

            pyautogui.hotkey('ctrl', 'right')
            print("")
            if r == numPage-1:
                for i in range(numPage+1):
                    pyautogui.hotkey('ctrl', 'left')
        time.sleep(second)

clickPost(180,250,375,460,5,2,3,60)
#180,250,375,460
