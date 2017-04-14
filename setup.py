import shutil
import os.path

shutil.copy2('joystickconfig.py', '/home/pi/joystickconfig.py')

if os.path.exists('retroarch.cfg'):
	print "arquivo retroarch encontrado..."
	shutil.copy2('retroarch.cfg', '/opt/retropie/configs/neogeo/retroarch.cfg')

if os.path.exists('Retroarch Config Input.sh'):
	print "arquivo retroarch config input encontrado..."
	print "Configurando e instalando..."
	os.system('chmod +x Retroarch\ Config\ Input.sh')
	shutil.copy2('Retroarch Config Input.sh', '/home/pi/Desktop/RetroPie/retropiemenu/')
