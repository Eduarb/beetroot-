# 1.    Ви - злий касир в АТБ і продаєте алкогольні напої лише особам старше 18 років. Людям, старше 14 років і молодше 18 років, ви продаєте лише енергетичні напої. Всім решта - лише Живчик:).
# Напишіть функціонал на пайтоні, який реалізує цей алгоритм.

# 2.    Ви працюєте на проекті, який займається тим, що опрацьовує дані по платежах клієнтів від різних платіжних систем. Дані зберігаються в csv-файлах на Linux сервері. При перекидуванні даних на Windows сервер виявилось, що віндовс додає специфічні символи на позначення початку (“;”) і закінчення стрічки (“%”) з зашифрованим Transaction ID (було “yu7i9om0iymn”, стало “;yu7i9om0iymn%“). Це критичний баг для проекту. Реалізуйте механізм на пайтоні, який буде видаляти непотрібні символи з початку і кінця Transaction ID.
# 3.    Умова та ж сама, але тепер віндовс рандомно додає знак “&” в будь-яку позицію в стрічці Transaction ID (Було “yu7i9om0iymn”, стало “yu&7i9om&0iym&n”).
# Реалізуйте функціонал, який буде видаляти знак “&” зі стрічки.
vind = "yu7i9om0iymn"
vind_copy = "yu&7i9om&0iym&n"
output_vind_copy = vind.replace("&", "") 
print(output_vind_copy )
# 4.   Створіть програму, яка перевіряє, чи може користувач отримати кредит в банку. Задайте для користувача дані про його дохід, вік та наявність роботи. Врахуйте різні умови, такі як мінімальний дохід, максимальний вік та наявність роботи.

income = 30000
age = 20
work = "працюе"
if income > 10000 and age > 18 and work == "працюе" :
    print("Вам одобрен кредит")
elif income < 10000 or age < 18 :
    print("Вам не погоджено кредит")
else:
    print("Приходи в след раз")












