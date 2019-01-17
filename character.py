from extras import b58check

class character:
	def __init__(self, address):
		self.address = address
		self.base = [b58check.index(i) for i in address]

		self.name = self.address[1:8]

		self.VIT = sum(self.base[8:10])
		self.STR = sum(self.base[10:12])
		self.INT = sum(self.base[12:14])
		self.DEX = sum(self.base[14:16])
		self.AGI = sum(self.base[16:18])

		self.hp = int(round(2.63157*self.VIT) + 700)

		self.moves = [i%29 + 1 for i in self.base[18:22]]

	def takeDamage(self, attack):
		if attack['type'] == self.getCharacterType():
			self.hp -= int(round(attack['damage']*0.7, 0))
		else:
			self.hp -= attack['damage']

		if self.hp < 0: self.hp = 0 

	def getCharacterType(self):
		attacks = [self.getDamage(move) for move in self.moves]
		damages = [attack['damage'] for attack in attacks]
		
		for attack in attacks:
			if attack['damage'] == max(damages):
				return attack['type']

	def getDamage(self, move):
		if 1 <= move < 15:
			# Magical Attack (INT + DEX)
			attackType = 'Magic'
			baseATK = int(self.INT*0.75 + self.DEX*0.25)
		elif 15 < move <= 29:
			# Physical Attack (STR + AGI)
			attackType = 'Neutral'
			baseATK = int(self.STR*0.75 + self.AGI*0.25)
		elif move == 15:
			# Special Attack
			attackType = 'Special'
			baseATK = 120

		# Neutral move intensity
		neutralMove = move - 15 if move > 15 else move
		attackDamage = int(round(0.8772*baseATK, 0) + neutralMove)

		return {'type' : attackType, 'damage': attackDamage}

	def print(self):
		print("\n- Name: %s" % self.name)
		print("- HP: %i" % self.hp)
		print("- Type: %s" % self.getCharacterType())
		attacks = [self.getDamage(i) for i in self.moves]
		print("- Attacks:")

		for i in attacks:
			print("\t* %i (%s)" % (i['damage'], i['type']))

	def isAlive(self):
		return self.hp > 0
