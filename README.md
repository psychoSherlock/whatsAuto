# WhatsAuto: Simple, but tricky whatsapp automation 🤪
## ⚠️ Warning, read this page before using the program or you might break the system 😵

### What's this program?
Well this is a simple python code that you can run to send automated whatsapp messages through whatsapp web to multiple person.
It needs you to choose between two options. Either 1 message for all people or different specified message to different people

⚠️ Warning, if misused the script can be used for spamming. If used by someone, neither the developer or GitHub is responsible for their misdoings. By using this script, you are agreeing that you will be responsible for your misdoings

### How to use the program?
😄 I know this is why you are here for. Before doing so you need to know how the program works. Here's how
#### How?
* There's a python module called pyautogui. That's the base. It has functions to move the cursor.
* There are three variables in the code. You need to edit this *manually*. They are:
```python
SearchField = var # The search filed on Whatsapp Web
FirstChild = var # The first contact that appears after searching
TextField = var # The chat Field for a contact
```
#### Here's what you need to do.
* There's one more script in this repo named findCursorPos.py
* Open a terminal (or CMD on windows) and run the script. The script will print the cursors X and Y position on the screen.
* Maximize your browser and hover your cursor to the search Field🔎 on Whatsapp Web. 
* Without moving your cursor, open the terminal which is running the script and stop it by pressing `CTRL + C` (you could use keyboard shortcuts to switch windows)
* Copy the X and Y coordinates and pass it to the variable mentioned above.
* Find other two variables the same way.
* ⚠️ Warning, make sure to choose right co-ordinates else you might sent the message to someone you don't wanted to 🧟
* Configure the messages in the script. For multiple people edit the variable `var`
* That's it. Run the script and enjoy 😊
