from extras import checkAddr, logo
from character import character
from random import randint

def main():
	print("\n" + logo)
	print("    v0.0.01 // 09.01.2019 // @cvasqxz\n")
	addr1 = input("> Enter valid address #1: ")
	addr2 = input("> Enter valid address #1: ")

	addr1 = "cRomsSTmwGCn2aGSrxik26iqTf655juUBR"
	addr2 = "coHGHzJSWLpUjbVrcNhKg4uckdfCDmNzU1"

	if checkAddr(addr1) and checkAddr(addr2) and not addr1 == addr2:
		player1 = character(addr1)
		player2 = character(addr2)
		player1.print()
		player2.print()

		print("\n\n- BATTLE BEGINS !!!")
		firstTurn = randint(0, 1)
		print("- Player #%i Starts" % (firstTurn + 1))
		turn = 1

		while player1.isAlive() and player2.isAlive():
			print("\n- TURN #%i" % turn)
			print("\t* HP: (%i) vs (%i)" % (player1.hp, player2.hp))

			chrATK1 = player1.getDamage(player1.moves[randint(0, 3)])
			chrATK2 = player2.getDamage(player2.moves[randint(0, 3)])

			print("\t* Player #1 move: %s" % chrATK1)
			print("\t* Player #2 move: %s" % chrATK2)

			if firstTurn:
				player1.takeDamage(chrATK2)
				if player1.hp == 0: break
				player2.takeDamage(chrATK1)
			else:
				player2.takeDamage(chrATK1)
				if player2.hp == 0: break
				player1.takeDamage(chrATK2)
			
			firstTurn = not firstTurn
			turn += 1

		winner = 'player #1' if player1.hp > player2.hp else 'player #2'
		print("\n- WINNER: %s" %winner)

if __name__ == '__main__':
	main()
