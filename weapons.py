class BaseWeapon:
	attack=0
	isWeapon=True
	
class Dagger(BaseWeapon):
	attack=2
	
class ShortSword(BaseWeapon):
	attack=5
	
class LongSword(BaseWeapon):
	attack=10
	
class Excalibur(BaseWeapon):
	attack = 15
	
	def __init__(self):
		if CHEATS:
			self.attack = 9999 # IT'S OVER 9000!!!
