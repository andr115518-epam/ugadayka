import random
num_ran = random.randint(1,101)
def check_num():
    num = -1
    while num != num_ran:
        num = int(input('Угадайте число от 1 до 100'))
        if num > num_ran:
            print('Слишком много, попробуйте еще раз')
        elif num < num_ran:
            print('Слишком мало, попробуйте еще раз')
        else:
            print('Вы угадали, поздравляем!')
            break

def again():
    ans = ''
    while ans != 'да' or ans != 'нет':
        ans = input('Сыграем еще?')
        if ans == 'да':
            print(('Отлично!'))
            check_num()
        elif ans == 'нет':
            print('Хорошо, в следующий раз! Пока!')
            break

check_num()
again()