# WebsiteBlocker
- This script helps in blocking distracting websites for specified working hours.
- You can change working hours and websites to block in the script.

### Build Requirements :
- Python 3+
     
### Build instructions :
- Download or clone repository.

  **For mac and linux**
   
  - Run given command in terminal.
    
     ```
        sudo crontab -e
     ```
     
  - A file will be opened, add given line to the file.
     
     ```
        @reboot python3 <path of Daily_Blocker.py>
     ```

  - Reboot your system.
  
  
  **For Windows**
  
  - Change file_path (in DailyBlocker.py) from **/etc/hosts** to **C:\Windows\System32\drivers\etc\hosts**.
  
  - Change file extension from **.py** to **.pyw**.
  
  - Create a new task using task scheduler and give it root previleges.
  
  - In action tab of this task, give file path of Daily_Blocker.pyw.
  
  - Set Trigger to "At Startup".
  
  - Reboot your system.
  
- After running above steps you can check that distracting websites (mentioned in script) will not work for specified working hours.
