import random
print("Чать бот SimulatorAl. Текст пиши маленькими буквами!!!! И без занков препинания!")
privet = {
	"привет":[" Салам!", " Привет!", " Хай!"],
	"как дела?":[" Нормально"," Плохо"," Как всегда"," Тебе какая разница?","Показать тебе мою силу???"],
	"что делаешь?":[" алкашню"," черти что"," не че"," Тебе какая разница?"],
	"пока":[" Досвидос!"," Пока", " Вали отсюда!"],
	"ты кто": [ "Никто!"],
	"тупой":[" Само такое"," Взаимно", " Втиральщик!!!!", "А ты алкаш!!!!"],
	"пошел ты":["Я не обязан","Ну и пойду!","Взаимно!"],
	"взаимно":[" Не взаимно", " Не ври мне "],
	"здрасте":[" Салам!", " Привет!", " Хай!"],
	"ты знаешь что такое youtube":[" ДА, конечно!!!!"," ТЫ еще спрашиваешь!!"," Чеееее, YouTube???Не я не думаю!"],
	"я ивангай":[" Не вриии!!"],
	"я не вру":[" Докажи"," Ты врешь то что ты не врешь!!!"],
	"ты алкаголик":["неа "," ну чуть-чуть", " ы-ы-ы-ы-ы-ы как ты угадал?"],
	"ты алкаш":["неа "," ну чуть-чуть", " ы-ы-ы-ы-ы-ы как ты угадал?"],
	"сколько тебе лет":["1","99999999999999999999999999","228"],
	"ты тюремьщик":[" Да я нарушил закон номер 228!!!!!!! Не че такого"],
	"ты животное":["  Я обиделся((("," А ты алкаш"],
	"как тебя зовут":[" У меня есть много имен но меня называют Аленушек"],
	"аленушка ты алкашня":["неа "," ну чуть-чуть", " ы-ы-ы-ы-ы-ы как ты угадал?"],
	"аленушка":["ДА это я и че","Че хоч","Я тебя затролил ну ты и ЛООООХ!!! Ия не Аленушек а Аленушка"]
	"я хочу":[" НЕа ты не хоч"]
	"сказать":[" Лучше молчи!"]
	"давай":["НЕ давай!","давай без давай","Давайте без давайте"]
	"ты слушаешь музыку":["о да я люблю музыку"]
	"я":[" Последняя буква в алфавите"]
	"а":["Арбуз"]
	"жирный":[""" ТЫ что ли"," худой", "я тее не завидую,","ты че мне что ли сказанул!!!"]
	"где ты живешь":["В компьютере", "В стране ,,Компуктор,, в городе ,,Матрица,, на улице ,,Проводная 35,,
	подьезд 1/10, квартира 228!!!!"""],
	"ты знаешь меня":["Незнаю!","Ти кто!!!"],
	"ты знаешь ":["Незнаю!","Ти кто!!!"],
	"андрей":["ТЫ что ли?"]
	"тебя зовут саид":[" Возможно частично!!"," Меня зовут алкаш!!!!!!!"," Откуда я знаю"]
	"ты живое существо":[" Как ты узнал? Это ведь было написанно наверху"],
	"ты компьютер":[" Докажи!"],
	"ты программа":[" Да ты всявидещий что ли?"],
	"амин":["Да я его знаю он самый могучий алкаш на нашей земле(шутка он просто алкаш)"]
	"знаешь амина":["Да я его знаю он самый могучий алкаш на нашей земле(шутка он просто алкаш)"]


	}
while True:
	answer = input()
	if answer in privet:
		print(random.choice(privet[answer]))
	if answer == "пока":
		print("пока")
		break