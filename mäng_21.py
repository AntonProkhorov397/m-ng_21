import random
igrok = 0
bot = 0
koloda = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4
print("Поиграем в 21? \nЕсли хотите играть нажмите Enter, если хотите выйти, то нажмите Ctrl+C")
input()
while True:
	if igrok == 21:
		print("Больше карт не надо, у вас 21")
		print("Вы автоматически победили бота, так как у вас 21.")
		input("Нажмите Enter, чтобы закрыть окно."); break
	if igrok>21:
		print("Вы проиграли, так как набрали больше 21")
		print("Попытайте свою попытку в другой раз.")
		input("Нажмите Enter, чтобы закрыть окно."); break
	yes_or_no = input("Будете ли вы брать карту?\nВведите yes, если хотите брать карту или введите no, если не берете карту.\n")
	if yes_or_no == 'yes':
		karti = random.choice(koloda)
		print("Вы взяли карту выпало:", karti)
		igrok += karti
		print("Сейчас у вас ", igrok)
	if yes_or_no == 'no':
		print("У вас ", igrok, "очков.")
		print("Ход бота")
		while True:
			if bot<15:
				print("Бот берет карту")
				karti = random.choice(koloda)
				print("Боту выпало", karti, "очков.")
				bot += karti
				print("У бота ", bot, "очков.")
			if bot>21:
				print("Бот проиграл.\nТак как у него", bot, "очков, а у вас ", igrok)
				input("Нажмите Enter, чтобы закрыть"); exit(0)
			if bot>igrok:
				print("Бот победил.\nТак как у него", bot, "очков, а у вас ", igrok, "\nНе растраивайтесь. Попробуйте ещё раз.")
				input("Нажмите Enter, чтобы закрыть"); exit(0)
			if bot == igrok:
				print("Вы набрали равное количество очков и у вас ничья")
				input("Нажмите Enter, чтобы закрыть"); exit(0)
