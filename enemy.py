import random

ENEMY_NAMES = (
	"Grue",
	"Nina",
	"Panda",
)

class Enemy:
	name=None
	hp=100
	maxHp=100
	stat_defense=0
	stat_attack=0
	level = 1
	isPlayer=False
	weapon=None
	
	def __init__(self, level, weapon):
		self.name = random.choice(ENEMY_NAMES)
		self.weapon = weapon
		self.level = level
		self.fixStats()
		self.hp = self.maxHp
		
	def fixStats(self):
		"fixes the stats (attack/defense) after the level has been changed"
		level = self.level
		if self.isPlayer:
			level = level+1 # give the player an extra advantage to keep things fun
		self.stat_attack = 40+(level*5)
		self.stat_defense = 30+(level*5)
		self.maxHp = 100+(10*((level+1)))
	def hurt(self, ammount):
		"hurts the object, removes damage based on the object's defense rating"
		ammount = ammount - (self.stat_defense/2)
		self.hp = self.hp - ammount
		return self.hp
	def attack(self, target):
		"attacks a target, and removes damage based on the object's attack rating"
		damage = ((self.weapon.attack+self.stat_attack)/2)+random.choice(range(self.stat_attack/6, self.stat_attack/4))
		target.hurt(damage)
		return damage
	def heal(self, value):
		"heals the current object"
		oldHp = self.hp
		self.hp = self.hp + value
		if self.hp > self.maxHp: self.hp = self.maxHp
		return self.hp - oldHp
	def think(self, target):
		"AI for the enemy"
		if self.hp < 0: return # we can't think if we're dead!
		if self.hp/self.maxHp < 0.4 and random.choice((True, False, False)):
			ammount = self.heal(self.level*10)
			print "Enemy used a healing potion, recovered %s HP!" % ammount
		else:
			damage = self.attack(target)
			print "Enemy %s attacks, %s looses %s HP" % (self.name, target.name, damage)
