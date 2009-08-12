from enemy import Enemy
from weapons import Dagger

class Player(Enemy):
	experience = 0
	inventory = []
	isPlayer = True
	def __init__(self):
		self.weapon = Dagger()
		print "What is your name?"
		self.name = raw_input()
		self.level = 2
		self.fixStats()
		self.hp = self.maxHp
		#give some starting items
		from items import Potion, SuperPotion
		from weapons import Excalibur
		self.giveItem(Excalibur)
		for i in range(1, 5):
			self.giveItem(Potion())
			self.giveItem(SuperPotion())
	def giveExp(self, ammount):
		"give the player a certain ammount of experience points, and print the new stats if they gained a level"
		print "You have gained %s experience points" % ammount
		self.experience = self.experience+ammount
		if self.experience > (self.level+1)^2:
			self.level = self.level + 1
			self.fixStats()
			print "You have gained a level!"
			print "Level - %s" % self.level
			print "Attack - %s" % self.stat_attack
			print "Defense - %s" % self.stat_defense
			print "Max HP - %s" % self.maxHp
			raw_input()
		else:
			print "%s experience points until next level" % ((self.level+1)^2)-self.experience
	def giveItem(self, item):
		"give the player an item, and add it to their inventory or weapon slot"
		if item.isWeapon:
			self.weapon = item
		else:
			self.inventory.append(item)
