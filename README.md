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
     
  - A file will be opened, add given line to the file
     
     ```
        @reboot python3 <path of Daily_Blocker.py>
     ```

  - Reboot your system.
  
  
- After running above steps you can check that distracting websites (mentioned in script) will not work for specified working hours.
