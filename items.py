
class BaseItem:
	isWeapon=False
	name = "Item"
	extraText = "Does something"
	
	def use(self, target):
		"use the object on target"
		pass
		
class Potion(BaseItem):
	name = "Potion"
	extraText = "replenish 20 HP"
	hp = 20
	
	def __init__(self):
		self.extraText = "replenish %s HP" % self.hp
	
	def use(self, target):
		target.heal(self.hp)
		
class SuperPotion(Potion):
	name = "Super Potion"
	hp = 50
