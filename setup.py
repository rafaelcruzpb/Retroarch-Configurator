import shutil
import os.path

shutil.copy2('joystickconfig.py', '/home/pi/joystickconfig.py')

if os.path.exists('retroarch.cfg')
	shutil.copy2('retroarch.cfg', '/opt/retropie/configs/neogeo/retroarch.cfg')

if os.path.exists('Retroarch Config Input.rp')
	shutil.copy2('Retroarch Config Input.rp', '/home/pi/Desktop/Retropie/retropiemenu/')
