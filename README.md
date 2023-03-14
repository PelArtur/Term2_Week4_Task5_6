# Task 6
## **Коротко про сюжет**
Сюжет гри розгортається в світі під назвою Ардентія, де ви, як головний герой історії повинні спасти світ від страшного прокляття. Щоб це зробити вам необхідно зробити Божественний артефакт, у цьому вам допоможе маг на ім'я Аркандор. Знайти і поговорити з ним ви можете в місті Нірдер.
## **Щодо процесу і реалізації гри**
### **Файли**
Весь код розбитий на 4 модуля: classes.py, game_objects.py, function.py, main.py
- В __classes.py__ реалізовані всі необхідні класи для об'єктів та певний інструментарій для цих об'єктів
- В __game_objects.py__ описаті усі об'єкти гри: предмети, персонажі та локації, а також їх властивості. Реалізовано все за допомогою класів із модулю __classes.py__
- В __function.py__ реалізовані 3 допоможні функції для вибору предмету з списку для взаємодії з ним. Також там є функція для виконання процесу торгівлі та ще одна для взаємодії з персонажами
- __main.py__ є основним модулем, де проходять усі процеси гри із залученням інструментраію вище перерахованих модулів
### **Коротка довідка по процесу гри**
В термінал вам буде відображатись об'єкт, інформація про нього і всі можливі взаємодії з ним. Для взаємодій є передбачені декілька ключових слів:
- location або loc — зміна поточної локації;
- character або npc — вибір персонажа для взаємодії;
- item — вибір предмету, щоб додати його в інвертар%;
- item all — додати в інвентар усі предмети, доступні на локації;
- backpack — переглянути інвентар;
- tool — переглянути спорядження і за необхідністю змінити його;
- balance — дізнатись поточну кількість коштів;
- info — дізнатись усі інформацію про слабкості супротивників;

Також є ще два системних ключових слова:
- break — припинення гри, використовувати лише, коли знаходитесь в об'єкті локації;
- back — для поверння до останнього об'єкту локації. Можна застосовувати тільки в процесі вибору об'єктів за номером, або в інтервейсі персонажа