import random

class Character() :
	def __init__(self):
		self.name = ""
		self.health = 0
		self.power =0

	def alive(self):
		if self.name == "Zombie":
			return True
		else :
			return self.health > 0
    
	def attack(self,enemy):
		#if self.name == "Hero" and random.random() < 0.2 :
		#	self.power = 2 * self.power
		#	print("Double damage!")
		
		if self.name == "Shadow":
			self.attackcount += 1
		
		if enemy.name == "Shadow" and enemy.attackcount == 9 :
			enemy.health -= self.power
			enemy.attackcount = 0
		elif enemy.name != "Shadow" :
			if self.name == "Hero" and random.random() < 0.2 :
				print("Double damage!")
				enemy.health = enemy.health - (2* self.power)
				print("{} does {} damage to {}".format(self.name, 2 * self.power, enemy.name))
			else :
				enemy.health -= self.power
				print("{} does {} damage to {}.".format(self.name, self.power, enemy.name))

		if not enemy.alive() :
			if enemy.name != "Hero":
				#print("{} is dead.".format(enemy.name))
				print("The {} is dead.".format(enemy.name))
				self.coin += enemy.prize
			else :
				print("You are dead.")
		else :
			if enemy.name == "Medic" and random.random() < 0.2 :
				enemy.health += 2
				print("{} recuperate 2 health points!".format(enemy.name))

	def print_status(self):
		print("{} has {} health and {} power".format(self.name, self.health, self.power))

class Hero(Character):
	def __init__(self):
		self.name = "Hero"
		self.health = 10
		self.power = 5
		self.coin = 0
    
class Goblin(Character):
	def __init__(self):
		self.name = "Goblin"
		self.health = 6
		self.power = 2
		self.prize =  5

class Medic(Character):
	def __init__(self):
		self.name = "Medic"
		self.health = 20
		self.power = 2
		self.prize = 4

class Shadow(Character):
	def __init__(self):
		self.name = "Shadow"
		self.health = 1
		self.power = 0.5
		self.attackcount = 0
		self.prize = 7

class Zombie(Character):
	def __init__(self):
		self.name = "Zombie"
		self.health = 6
		self.power = 2
		self.prize = 100

hero = Hero()
enemies = [Goblin(),Medic(),Shadow(),Zombie()]
#goblin = Goblin()
#enemy_input = 0

#while enemy_input != "2" and enemy_input != "1" and enemy_input != "3" and enemy_input != "4" :
#	print("What do you want to attack?")
#	print("1. Goblin")
#	print("2. Medic")
#	print("3. Shadow")
#	print("4. Zombie")
#	enemy_input = input("> ")

#if enemy_input == "1":
#	enemy = Goblin()
#	enemyname = "Goblin"

#if enemy_input == "2" :
#	enemy = Medic()
#	enemyname = "Medic"

#if enemy_input == "3":
#	enemy = Shadow()
#	enemyname = "Shadow"

#if enemy_input == "4":
#	enemy = Zombie()
#	enemyname = "Zombie"

for enemy in enemies :
	while enemy.alive() and hero.alive():
		hero.print_status()
		enemy.print_status()
		print()
		print("What do you want to do?")
		print("1. fight {}".format(enemy.name))
		print("2. do nothing")
		print("3. flee")
		print("> ", end=' ')
		raw_input = input()
		if raw_input == "1":
			hero.attack(enemy)
		elif raw_input == "2":
			pass
		elif raw_input == "3":
			print("Goodbye.")
			break
		else:
			print("Invalid input {}".format(raw_input))

		if enemy.alive():
			enemy.attack(hero)

	if hero.alive():
		print("--------------")
		print("You have earn {} coins!".format(enemy.prize))
		print("You have {} coins now.".format(hero.coin))
		print("--------------")





        


