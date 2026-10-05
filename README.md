KEYLOGGER - Shraddha Abirami A, 26/A19/014

The attached files are of a simple keylogger made in python and its log file in the form of a .txt file.

The main body of the keylogger consists of a function "Keylogger" that activates when the user presses a key. 
The function then opens the text log file to log the input keys. Some special keys like shift, control, tab, alt etc are renamed to
[Shift], [Ctrl], [Tab] etc. 

<img width="574" height="62" alt="image" src="https://github.com/user-attachments/assets/f71b5d69-28ec-483c-850d-e3229ee9ff73" />

 this line in the file removes the '' marks that appear around inputted letters in the keylogger to make it cleaner.

I created an exit hotkey for the function to immediately stop the execution and logging of the keylogger. Here the exit key is 'Esc'.

<img width="1080" height="204" alt="image" src="https://github.com/user-attachments/assets/243b3f51-2880-4840-a7d7-767d515fe9a7" />

This code enters a timestamp before every key in the log file showing date and time of input.

<img width="850" height="278" alt="image" src="https://github.com/user-attachments/assets/4b5ba3b9-73b2-4218-8f0a-425eb1a168c7" />

This function defines the active runtime of the typing session by taking a reading of the time in UNIX/POSIX timestamp form in seconds,
and then again when the function ends which is then converted into hours, mins and seconds and displayed in the log file once session ends.

Brownie Points Stuff

<img width="750" height="324" alt="image" src="https://github.com/user-attachments/assets/990081ed-ec96-4d9c-b7ac-df03448306a3" />

This function calculates the total runtime of the function in seconds and converts it into minutes. The definition of Words Per Minute in typing
is defined as the number of blocks of 5 letters, numbers, punctuation, spaces etc ie number of keystrokes typed in one min on average throughout
the session. This function returns the value rounded to 2 decimal places.

<img width="618" height="240" alt="image" src="https://github.com/user-attachments/assets/db12448b-cb8c-41f0-b55f-b1e42cf28d21" />

This function calculates the backspace error in the session ie the number of backspaces typed compared to the number of keystrokes
expressed as a percentage.

<img width="1076" height="478" alt="image" src="https://github.com/user-attachments/assets/6e801b09-3e6f-48b6-87aa-67f5ce904fb7" />

This is the code for the exit hotkey which prints out total keystrokes, active runtime, WPM and backspace errors as well after the session is over.

---------------------------

<img width="1152" height="1498" alt="image" src="https://github.com/user-attachments/assets/a1e06377-8c81-4ee1-9e17-c83734cc70cd" />
<img width="1202" height="1500" alt="image" src="https://github.com/user-attachments/assets/87f30f80-348e-4de4-ab97-0035db17ad50" />
<img width="1198" height="342" alt="image" src="https://github.com/user-attachments/assets/27bce090-5ff9-4b43-9068-ed96981a8403" />
Entire code for the keylogger.

<img width="1826" height="276" alt="image" src="https://github.com/user-attachments/assets/51e2d90e-5d07-40d0-8700-0bef3a70e658" />
Sample output in log file.




