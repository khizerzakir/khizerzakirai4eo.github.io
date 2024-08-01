import time

print("|---------------------------------------------|")
print("| Hello Friends, Welcome to TicTacToe Game!!! |")
print("| -------------Let's Start!!!!--------------- |")
print("|---------------------------------------------|")
time.sleep(0.8)
print('\nGame is loading ...\n')
time.sleep(0.8)

	

player_1 = [input("Player1 enter your name: "),'X']
player_2 = [input("Player2 enter your name: "),'O']



player_1_status = True
player_2_status = False
game_status = 'playing'
used_numbers = []

table = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]


def display_table():
	print("\n")
	for i in table:
		print("-------------")
		for j in i:
			print('| ', end="")
			print(j, end=" ")
		print("|", end="\n")
	print("-------------")
	print("\n")

def check_column():

	row_1 = [i[0] for i in table]
	row_2 = [i[1] for i in table]
	row_3 = [i[2] for i in table]

	if row_1.count(row_1[0])==3 or row_2.count(row_2[0])==3 or row_3.count(row_3[0])==3:
		return True
	else:
		return False

def check_row():

	col_1 = table[0]
	col_2 = table[1]
	col_3 = table[2]

	if col_1.count(col_1[0])==3 or col_2.count(col_2[0])==3 or col_3.count(col_3[0])==3:
		return True
	else:
		return False


def check_dioganal():
	d_1 = [table[i][i] for i in range(3)]
	d_2 = [
		table[0][2],
		table[1][1],
		table[2][0],
	]

	if d_1.count(d_1[0])==3 or d_2.count(d_2[0])==3:
		return True
	else:
		return False


def check_status(player):
	global game_status
	if check_dioganal() or check_column() or check_row():
		print(f"GOOD JOB {player[0]}, You are the winner !!!")
		game_status = "stop"
		return True
	else:
		return False


def update_table(player, choice):
	global table
	for i in table:
		for j in i:
			if j==choice:
				print(j)
				table[table.index(i)][i.index(j)]=player[-1]
	display_table()
	check_status(player)


def validate(choice):
	global used_numbers
	if choice not in used_numbers:
		used_numbers.append(choice)
	else:
		print("Already used, Choose again!!!".title())
		play()

def play():
	display_table()
	global player_1_status, player_2_status
	while game_status == 'playing':

		if player_1_status:
			choice = int(input(f"{player_1[0]} enter your choise: "))
			validate(choice)
			player_1_status = False
			player_2_status = True
			update_table(player_1, choice)
			
		elif player_2_status:
			choice = int(input(f"{player_2[0]} Enter your choise: "))
			validate(choice)
			player_2_status = False
			player_1_status = True
			update_table(player_2, choice)

play()



