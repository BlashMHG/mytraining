input_ = int(input("Введрте число от 3 до 20 - "))
if input_ < 3 or input_ > 20:
    print("""   Введенное число не подходит
   Пожалуйста, следуйте условиям ввода""")
else:
    input_list = list(range(1, input_)) 
    answer = []
    for i in input_list:
        for j in input_list:
            i_IL = i  #IL = input list
            j_IL = j
            if i_IL >= j_IL:
                continue
            else:
                kratnost = input_ % (i_IL + j_IL)
                if kratnost == 0:
                    answer.append([i_IL, j_IL])
    print(*answer)