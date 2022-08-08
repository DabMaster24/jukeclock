# JukeClock
Description:
<br>The jukeclock is an audio device that plays the current time through a speaker on the press of a button.  Currently, the only language is Vietnamese. 

How it works:
<br>The jukeclock uses a Raspberry Pi 3 B+ as its "brain". The pi holds the python code, which gets the time after connecting to wifi. It accesses the Raspberry Pi's GPIO library to take inputs from the button, which is wired to it.  The button is connected to 3 GPIO prongs: one for power (voltage), one for ground, and one as the "on/off switch" for our program. The program then translates the time into audio by pairing the time integers with audio clips of a person saying that number (Currently the audio clips are of my mom saying numbers in Vietnamese because that is the only language my grandpa understands).  Based on what time of day it is, the program also says whether it is morning, noon, afternoon, or evening. After the time has been translated to audio, it is played through a speaker. 

*For more information, see the images, diagrams, and video demonstration.
https://drive.google.com/drive/folders/1FOIJPE0SSdSOIXMq1YoJwNLXz8gcPGIe?usp=sharing

Bill of Materials (BOM): 
<br>CanaKit Raspberry Pi 3 B+:
https://amzn.to/3QuzgFl

Extra Large Push Button:
https://amzn.to/3QhQXYS

Plastic Box:
https://amzn.to/3d6s4kp

Speaker:
https://amzn.to/3Sxf9bB

USB Extension (for debugging):
https://amzn.to/3A4vOMz
