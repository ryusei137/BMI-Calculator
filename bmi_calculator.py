height = float(input("身長を小数(m)で入力してください: "))

weight = float(input("体重を小数(kg)で入力してください: "))

bmi = weight / (height ** 2)

result = ""

if bmi < 18.5:
    result = "低体重(痩せ)"

elif 18.5 <= bmi < 22:
    result = "スリムな普通"

elif 22 <= bmi < 24:
    result = "健康的な普通"

elif 24 <= bmi < 25:
    result = "がっしり・ぽっちゃり"

elif bmi >= 25:
    result = "肥満"

else:
    result = "数値を正しく入力してください。"

print(f"あなたのBMIは {bmi}です。")
print(f"判定結果：{result}")