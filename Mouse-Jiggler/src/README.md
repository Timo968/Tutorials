1. Install pyautogui with the Terminal

```
pip install pyautogui
```

2. Start python3 with the Terminal

```
python3
```

3. Paste the code in

```
import pyautogui
import time

while True:
    pyautogui.moveRel(50, 50, duration=1)
    pyautogui.moveRel(-50, -50, duration=1)
    time.sleep(1)
```


To interrupt the script press ctrl + c 
