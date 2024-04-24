# Photon LaserTag Software
Repository dedicated to developing the software to run a game utilizing the Photon Laser Tag equipment.

# Before Running
- Make sure you have pip installed
  - For Linux run: `python get-pip.py`
- Clone the project `git clone https://github.com/Group-20-Software-Engineering/lasertag`
- Build Dependencies `./build.sh`
  - This will update your machine and install the needed dependencies
  - You will need to insert your passcode as it calls sudo
  - If running in VScode built in terminal you will need to restart VScode for changes to apply

# TO RUN
- Run game `./run.sh`
- Press the `-` button to scroll faster on the Splash Screen
- After Splash Screen enter Player ID, Followed by Codename, followed by Machine ID *in that order*
  - If the Player ID already exists in the Database, enter the Machine ID next, instead of Codename
- To Start the game press the `=` button
- While game is running if you wish to return to the player entry screen again press the `=` button

# TO USE TRAFFIC GENERATOR
- After the splash screen is finished and the playerentry screen is open another terminal and  `cd frontend` then run `python3 python_trafficgenarator_v2.py` 
- Input the machine IDs in the order of `odd,odd,even,even`
- Return to the playerentry screen and press the `=` button to start the game
- The numbers you entered previously should appear in the playeraction screen
- After the 30 second countdown, the game should commence 


# TO QUIT
- The program should quit once you exit the main window, but if it does not, `ctrl + c` the terminal that is running the Python code



# Contributers 
- Programmer061703--------------Blake Williams            
- m-thursday--------------------Max Thursby
- chinamanryan------------------Ryan Cheng
- noahnewton10------------------Noah Newman
- JosephFolenV------------------Joseph Folen
- unclejeffaimgumin-------------Kevin Zheng
- landonr7----------------------Landon Reynolds
