input_answer = input('1から1000までの数字を選んで入力してください。')

if type(input_answer) == int:
    answer = int(input_answer)
    if answer > 0 and answer <= 1000:
        print(f'あなたが入力した値は{answer}です。')

        answer += 4
        print(f'その数に4を足すと{answer}です。')

        answer *= 2
        print(f'さらに倍にすると{answer}です。')

        answer -= 6
        print(f'そこから6を引くと{answer}です。')

        answer /= 2
        print(f'その値を2で割ると{answer}です。')

        print('最後に、最初に入力した値を引いてください。')
        answer = answer - int(input_answer)
        print(f'最終的な答えは{answer}です。')
    else:
        print('1から1000の数字を入力してください。')
else:
    print('1から1000の数字を入力してください。')

