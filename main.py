#!/usr/bin/env python

import weapons
from enemy import *
from items import *
from player import Player
import random

# If you want to add in saving, check out the 'pickle' module.

# some configuration stuff
CHEATS = False # set to true for cheats. Good for debugging.

# menu constants
ATTACK = 1
RUN = 2
USE_ITEM = 3
EXIT = 4

class RPG:
	def main(self):
		"game setup, and main loop"
		self.player = Player()
		# for now, let's just make it a series of battles
		# you can add in more stuff if you want.
		for i in range(1, 5):
			self.battle()
			choice = "y"
			while 1:
				print "Use an item? (y/n)"
				choice = raw_input()
				if choice == "n":
					break
				self.item_menu()
	
	def battle(self):
		"initiate a battle sequence"
		#get an enemy, give it a random weapon, and give it a random level (but no more then one less then the player)
		level = range(1, self.player.level-1)
		if not level:
			level = 1
		else:
			level = random.choice(level)
		enemy = Enemy(level = level, weapon=random.choice([weapons.Dagger(),
								   weapons.ShortSword(),
								   weapons.LongSword()]))
		print "Enemy %s appears!" % enemy.name
		raw_input()
		while self.player.hp > 0 and enemy.hp > 0:
			while 1:
				res = self.battleScreen(enemy)
				if res is EXIT:
					self.exit()
					break
				elif res is RUN:
					if random.choice([True, False, False]):
						print "You got away!"
						raw_input()
						return
					else:
						print "couldn't escape!"
						raw_input()
						return
				elif res is ATTACK:
					dmg = self.player.attack(enemy)
					print "Enemy took %s damage" % dmg
					break
				elif res is USE_ITEM:
					# item_menu will return false when the user chooses back
					if self.item_menu():
						break
			
			#enemy's turn
			enemy.think(self.player)
			raw_input()
		if self.player.hp <= 0:
			print "You have died."
			self.exit()
		elif enemy.hp <= 0:
			print "Enemy %s has been defeated!" % enemy.name
			expGain = enemy.level * 100
			self.player.giveExp(expGain)
			return
			
	def battleScreen(self, enemy):
		"prints the battle screen, and calls self.menu to get input in the form of a menu"
		print ".------------------->"
		print "| Level %s %s" % (enemy.level, enemy.name)
		print "| HP: %s/%s" % (enemy.hp, enemy.maxHp)
		print "'------------------->"
		print ".------------------->"
		print "| Level %s %s" % (self.player.level, self.player.name)
		print "| HP: %s/%s" % (self.player.hp, self.player.maxHp)
		print "'------------------->"
		print ""
		return self.menu()
	def menu(self):
		"draws the menu, and returns the action the user requested"
		print ".-----------."
		print "| 1. Attack |"
		print "| 2. Item   |"
		print "| 3. Run    |"
		print "| 4. Exit   |"
		print "'-----------'"
		try:
			do = int(raw_input())
		except ValueError:
			print "invalid choice"
			raw_input()
			return
		if do == 1:
			return ATTACK
		elif do == 2:
			return USE_ITEM
		elif do == 3:
			return RUN
		elif do == 4:
			return EXIT
		else:
			print "invalid choice"
			raw_input()
			return
	def item_menu(self):
		"draws the items menu based on the user's inventory. When an item is used, it's 'use' method is called, and then it is removed from their inventory."
		inv = self.player.inventory
		print ".------------------->"
		for i in range(0, len(inv)):
			print "| %s. %s (%s)" % (i+1, inv[i].name, inv[i].extraText)
		print "| X. Back"
		print "'------------------->"
		do = raw_input()
		if do == "X" or do == "x":
			return False
		else:
			try:
				i = int(do)-1
				if i < 0:
					raise ValueError
				item = inv[i]
				item.use(self.player)
				left = inv[0:i]
				right = inv[i+1:len(inv)]
				if i-2 < 0:
					left = []
				if i >= len(inv)-1:
					right = []
				self.player.inventory = left+right
				return True
			except (LookupError,ValueError):
				print "invalid input"
				raw_input()
				return self.item_menu()
	def exit(self):
		"exits the game"
		print "Goodbye"
		exit()

# start the game
if __name__ == "__main__": # only run the game if we're the main script
	rpg = RPG()
	rpg.main()
