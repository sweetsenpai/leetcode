# 🚀 LeetCode Solutions

📚 **Коллекция решений задач с LeetCode** на **Python**.  
🔹 Решения разделены по темам.  
🔹 Включают пояснения и альтернативные способы решения.  
🔹 Все решения протестированы с помощью `pytest`.

---
---

## 🏆 **Прогресс**

| Категория                 | Решено | Цель  |
|---------------------------|--------|-------|
| **Массивы & Хэш таблицы** | ✅ 5/5  | 🎯 5  |
| **Стэк & Очередь**        | ✅ 3/3  | 🎯 3  |
| **Всего**                 | ✅ 8/30 | 🎯 30 |

(Обновляется вручную)

---
## 📁 **Структура репозитория**

- **`Arrays_HashTables/`** — задачи по массивам и хэш-таблицам:
    - 📌 [`two_sum.py`](Arrays_HashTabls/two_sum.py) — решение задачи *Two Sum([↘](#-two-sum-problem))*.
    - 📌 [`contains_duplicate.py`](Arrays_HashTabls/contains_duplicate.py) — решение задачи *Contains Duplicate*.
    - 📌 [`valid_anagram.py`](Arrays_HashTabls/valid_anagram.py) — решение задачи *Valid Anagram*.
    - 📌 [`group_anagrams.py`](Arrays_HashTabls/group_anagrams.py) — решение задачи *Group Anagrams*.
    - 📌 [`TopKElements.py`](Arrays_HashTabls/TopKElements.py) — решение задачи *Top K Frequent Elements*.
- **`Stack_Queue/`** — задачи по стэкам и очередям:
  - 📌 [`MinStack.py`](Stack_Queue/MinStack.py) — решение задачи *Min Stack*.
  - 📌 [`Valid_Parentheses.py`](Stack_Queue/Valid_Parentheses.py) — решение задачи *Valid Parentheses*.
  - 📌 [`EvaluateReversePolishNotation.py`](Stack_Queue/EvaluateReversePolishNotation.py) — решение задачи *Evaluate Reverse Polish notation*.
- **`Tests/`** — тесты для решенных задач.

---
## 📌 Решенные задачи
---
## 📝 **Two Sum Problem**
### 📌 Задача:
Найти два числа, которые в сумме дают заданное число.

### ❌ Изначальное решение и его проблемы 😕
В первой версии решения я ухватил принцип:  
> `target - элемент списка = второе требуемое число`.

Я проходил по `nums`, создавая его копию, в которой заменял текущий элемент на `None`. Это нужно было, чтобы избежать дубликатов (например, `nums=[3,4,2]`, `target=6`, иначе я получал бы `[0,0]`).  
Далее я проверял, существует ли второе число в изменённом списке, а если да, то находил его индекс через `index()`.  

🔴 **Проблема**:  
> Поиск `index()` делает решение квадратичным `O(n²)`, что плохо для больших `nums`, но код хотя бы работал! ✌️

```python
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
      for index, item in enumerate(nums):
          search_num = nums.copy()
          second_num = target - item
          search_num[index] = None
          if second_num in search_num:
              return [index, search_num.index(second_num)]
      return []
```
### ✅ Оптимизированное решение 💡
В улучшенной версии я использую словарь (dict) для хранения элементов nums, которые мы уже прошли.
При каждом шаге вычитаем текущий num из target и проверяем, есть ли нужное число в dict. Если есть — задача решена!
> **🔹 Почему быстрее?**
> - Поиск в `dict` выполняется за **O(1)**.
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return [num_map[diff], index]
            num_map[num] = index
        return []
```
---
---
## 📝 **Contains Duplicate**
### 📌 Задача:
Проверить список на наличие дубликатов.

### ✅ Решение 

Задача оказалась очень легкой и решилась за минуту + минута на написание тестов.
Просто конвертируем изначальный список в `set()` который хранит только уникальные значение и сравниваем его длинну с длинной входного списка, если одинаковые то дубликатов нет, а если разные значит они есть 🤷‍♂️.
```python
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
```
---
## 📝 **Valid Anagram**
### 📌 Задача:
Проверить является ли одна строка анаграммой второй строки.

### ❌ Изначальные решения и их проблемы 😕

С начала задача мне показалась такой же простой как и предыдущая, и я использовал `set()` для сравнения двух строк и leetcode даже счел такое решение верным.
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return set(s) == set(t) and len(s) == len(t)
```
И всё бы было хорошо, если бы я не решил проверить свое решение с помощью chatgpt который предложил мне проверить свое решение с такими входными параметрами: `s = "aacc"`, `t = "ccac"`. И мое изначальное решение дало не верный ответ.
Проблема в том, что set не считает количество букв в слове, а лишь собирает уникальные значения из-за чего я получил не верный ответ.😢

### ✅ Мое решение 
Вторым моим решением было использовать словари `dict[буква]:частота появления в слове` для каждого из слов и в конце их сравнивать. И это рабочее решение, но не оптимальное по времени из-за двух полных циклов проходящих по строкам.
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {item: s.count(item) for item in set(s)}
        dict_b = {item: t.count(item) for item in set(t)}
        return dict_b == dict_s
```
### ✅ Оптимизированное решение 💡
Окончательное решение похоже на мое, но вместо тупого создания двух списков предусматривает два досрочных ответа, что экономит время:

    1. Сначала мы проверяем строки на длину, если длина разная, 
       то такие строки не могут быть анаграммами и мы выдаем ответ не вызвав ни одного цикла 
       
    2. В ходе второго цикла мы проверяем есть ли буква в первом словаре, 
       и если ее нет или количество букв не совпадает, мы так же досрочно выходим из цикла.
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        
        return True

```
---
---
## 📝 **Group Anagrams**
### 📌 Задача:
Найти все анаграммы во входном списке и сгруппировать их.

### ❌ Изначальное решение и его проблемы 😕

Изначальное решение работает, но имеет следующие недостатки:
- **Сложность алгоритма:** O(n² * k), где:
  - `n` — количество строк,
  - `k` — средняя длина строки.
- **Использование `.count()`:** Этот метод вызывается для каждого символа в каждой строке, что увеличивает время выполнения.
- **Удаление элементов из списка:** Метод `.remove()` требует дополнительной памяти

#### Логика работы: 

> Изначально создаем `unchecked_list` котрый хранит в себе все непроверенные слова из первоначального списка.
> Далее идем по `strs` и проверяем не вышло ли так, что уже все слова проверенны, если да то идем на выход.
> Если ещё не всё проверенно, но текущего слова нет в списке слов на проверку, то мы просто переходим к следующей итерации.
> Если нам не повезло и ни одна из проверок не дала нам пропустить текущее слово, то сначала мы делаем из слова частотный словар `item_dict`.
> Убираем текущее слово из списка не провереных, чтобы оно нам больше не мешало.
> И переходим к ещё одному циклу в котором проверяем оставшиеся на проверку слова, делаем из них такой же частотный словарь `sub_dict` и 
> сравниваем его с `item_dict`, если совпало то добавляем в списко анаграм и убираем это слово из слов на проверку.
> В конце записываем полученную группу в конечный список `result_list` и выдаем его.

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result_list = []
        unchecked_list = strs.copy()

        for item in strs:
            anagram_list = []
            anagram_list.append(item)

            if len(unchecked_list) == 0:
                break

            if item not in unchecked_list:
                continue

            item_dict = {letter: item.count(letter) for letter in set(item)}
            unchecked_list.remove(item)

            for sub_item in unchecked_list:
                sub_dict = {letter: sub_item.count(letter) for letter in set(sub_item)}

                if item_dict == sub_dict:
                    anagram_list.append(sub_item)
                    unchecked_list.remove(sub_item)

            result_list.append(anagram_list)
        return result_list
```

### ✅ Оптимизированное решение 💡

Тут все прекрасно и решение само по себе очень красивое, разберу его по строчно так как оно мне очень понравилось.
```python
class Solution:
    def bettergroupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            counts = [0] * 26  # все буквы английского алфавита
            for char in word:
                counts[ord(char) - ord("a")] +=1
            key = tuple(counts)
            groups[key].append(word)

        return list(groups.values())
```

Тут мы создаем словар с помощью `defaultdict(list)` который позволяет при обращении к ключу которого в словаре нет, 
не выдавать ошибку как классический dict, а присваевать такому ключу пустой список:

```python
groups = defaultdict(list)
```

Далее мы итерируем по `strs` и для каждого слова создаем список на 26 элементов, где каждый элемент изначально равен нулю.
Из условия задачи, мы знаем что на вход подаются только слова из букв в нижнем регистре английского алфавита которых 26.
`counts` мы будем использовать для хранения частоты появления букв в обрабатываемом на этом шаге `word`.
```python
for word in strs:
            counts = [0] * 26 
```
Далее мы итерируем по всем буквам в текущем `word` и с помощью `ord(char) - ord("a")` увеличиваем на один 
изначально нулевой счетчик букв в слове. Делается это следующим образом `ord()` преобразует входящий символ в Unix формат,
условно `a` становиться равной `100`, `b` = `101` и так далее, `ord(char) - ord("a")` позволяет нам определить индекс 
элемента списка `counts` соответствующего текущей буквые которую мы обрабатваем. Выходит, что `ord(a) - ord("a")` = `100 - 100`, 
что соответствует 0 элементу списка, `ord(b) - ord("a")` = `101 - 100` = 1 и так далее, таким орбазом мы формируем частотный список для текущего слова
```python
for char in word:
                counts[ord(char) - ord("a")] +=1
```

Далее конвертируем наш список в `tuple` чтобы сделать его ключом словаря и по этому ключу записываем наше слово в словарь.
Для анаграм `counts` будет одинаковым и соответственно они будут записаны по одному ключу в один список, 
так мы и сформируем списки анаграм.
```python
key = tuple(counts)
groups[key].append(word)
```

---
## 📝 **Top K Frequent Elements**
### 📌 Задача:
Дан целочисленный массив nums и целое число k. Верните k наиболее часто встречающихся элементов. Ответ можно вернуть в любом порядке.
### ✅ Решение 
Решение этой задачи основано на `bucket sort`, ниже разберу решение задачи построчно.

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counts = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            counts[num] +=1
        for key, value in counts.items():
            freq[value].append(key)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
```
На первом шаге мы инициализируем список `result` - в который будем складывать ответ, частотный словарь `counts`, 
и список `freq`.

`freq` - ключевая фигура в работе нашего кода и в `bucket sort`, длина списка `len(nums) + 1` - почему именно такая длина?
`freq` будет хранить в себе элементы `nums` таким образом, что индекс элемента будет соответствовать частоте появления этого
элемента в `nums`. 

Так как `index = 0` соответсвует часто те появления элемента 0, то такие элементы просто не появяться в списке `nums`,
Следовательно длина `freq` должен быть длинной равной `len(nums) + 1`, так как в крайнем случае все элементы в `nums` будут встречаться уникальное количество раз + 1 под нулевой индекс.

Если `nums = [1,3,3,3,6,7,7]`, то `freq` будет выглядить следующем образом:

| **Индекс (частота появления в nums)** | 0                                                                                          | 1     | 2   | 3   |
|--------------------------------------|--------------------------------------------------------------------------------------------|-------|-----|-----|
| **Элемент**                          | ноль всегда пустой | [1,6] | [7] | [3] |


Этот подход похож на инвертированный подход, который использовался в Group Anagram.
```python
result = []
counts = defaultdict(int)
freq = [[] for _ in range(len(nums) + 1)]
```
Далее мы заполняем частотный словарь `counts` и после заполняем `freq` согласно логике описаной выше, 
`index` - частоса появления элемента, `freq[index]` - список с элементами с частотой появление равной `index`.

```python
for num in nums:
  counts[num] +=1
for key, value in counts.items():
    freq[value].append(key)

```
На последнем шаге мы просто итерируем по `freq` с конца, так как нам нужно вывести элементы с наибольшей частотой появления, 
а такие элементы лежат ближе всего к концу списка.
Итерируем пока длина списка `result` не будет соответствовать `k` и мы, следовательно, не получим ответ.

---
---
## 📝 **Valid Parentheses**
### 📌 Задача:
На вход подается строка содержащая только символы  `(` `)`, `{` `}`, `[`  `]`. 
Необходимо проверить строку на правильность закрытия скобок.
### ✅ Мое Решение
Мое решение отходит от классического решения этой задачи, но я всё равно им горжусь.

Основная суть моего решения заключается в том, что если у нас есть открывающая скобка, 
то валидная закрывающая может находиться только в двух местах строки:
 1. Сразу после открывающей скобки: `(){}`
 2. Зеркально в строке: `({[]})`

И такой подход работает, хоть при проверках моего решения нейросети очень долго пытались меня убедить в обратном из-за
того, что мой подход не следует логике вложенности и закрытия/открытия скобок, а просто проверяет фиксированный места в строке.
Единственный кому удалось подорвать мою уверреность в себе это leetcode когда я попытался заsubmit-ить свое решение и мой код споткнулся
на строке, где были только закрывающие скобки `)}`. На таких строках я не получал не верного решения, я получал `IndexError`🙃.
В принципе, эту обшибку можно было бы решить слегка доработав мой код, но на тот момент я уже убил пару часов пытаясь разобраться
почему нейросети убеждают меня в неправильности моего кода и прогнал несколько десятков предложенных ими проверок
(ни в одной проверке не было строки только с закрывающими скобками🥲).

```python
def isValid_my(s: str) -> bool:
    breckit_dict = defaultdict(lambda: None)
    breckit_dict["("] = ")"
    breckit_dict["["] = "]"
    breckit_dict["{"] = "}"
    lenth = len(s)
    if lenth % 2 !=0:
        return False
    s_list = list(s)
    if not breckit_dict[s_list[0]]:
        return False
    for index, letter in enumerate(s_list):
        if breckit_dict[letter]:
            opposite_brecket = breckit_dict[letter]
            if s_list[index+1]!= opposite_brecket and s_list[len(s) - 1 - index]!=opposite_brecket:
                return False

    return True
```
Быстро пробегусь по своему коду, так как вдаваться в подробности не вижу смысла.
1. Создаем `breckit_dict` с помощью `defaultdict(lambda: None)` так, чтобы при запросе ключа которого нет в словаре нам возвращался
  None.
2. Далее заполняем наш словарь парами, `breckit_dict[открывающая скобка]` = `закрывающая скобка`
3. Проверяем длинну нашей входной строки, если длинна не четное число, то сразу идем на выход так как невозможно образовать пары в такой строке.
4. Дальше была небольшая агония с попыткой обработать `IndexError`, где я проверял не является ли первая скобка в строке закрывающей
   чтобы сразу пойти на выход, но на это не стоит обращать внимание.
5. Дальше всё просто, идем по строке проверяя каждый символ является ли он открывающей скобкой, если да то сразу проверяем
   строку на предмет закрывающей скобки сразу после текущего символа и зеркально в строке, если всё окей то идем дальше, в противном случае выдаем ошибку.

### ✅ Решение(общепризнаное)
Как не удивительно, но суть решения задачи по стэкам в использовании стека👍

Как всегда, разберем решение по строчно:
```python
def isValid(self, s: str) -> bool:
      bracket_dict = {')': '(', '}': '{', ']': '['}
      stack = []

      for bracket in s:
          if bracket in bracket_dict:
              if not (stack and stack.pop() == bracket_dict[bracket]):
                  return False
          else:
              stack.append(bracket)
      return not stack
```
И так, в начале мы создаем словарь `breckit_dict[закрывающая скобка]` = `открывающая скобка`.
Так же создаем пустой стэк который в `python` будет просто списком.
```python
bracket_dict = {')': '(', '}': '{', ']': '['}
stack = []
```
Далее итерируем по строке проверяя не является ли текущий символ закрывающей скобкой.
```python
for bracket in s:
        if bracket in bracket_dict:
```
Чтобы лучше понять решение, сначала разберем случай когда нам попалась открывающая скобка.
В такой ситуации мы просто записываем нашу скобку в стэк и идем дальше.
То-есть для входной строки `({[]})` первый три шага будут выглядить так:

| Шаг   | 0   | 1    | 2       | 3              |
|-------|-----|------|---------|----------------|
| stack | `[]` | `["("]` | `["(","{"]` | `["(","{","[",]` |

```python
else:
    stack.append(bracket)
```
Зафиксировали момент, что спустя три итерации наш стэк выглядит следующим образом `stack =  ["(","{","["]`.
На 4 шаге начинается всё самое интересное, текущем элементом становиться `]` и она удовлетворяет условию `if bracket in bracket_dict:`.
Теперь мы проверяем две вещи:
1. Есть у нас что-то в стэке?
2. Если мы сделаем `stack.pop()` - который удалит и вернет последний элемент нашего `stack`, то полученный элемент будет равен
   `bracket_dict[текущий элемент]`?

Если оба условия выполняются, то мы спокойно идем дальше, если нет, то возвращаем `False`.
```python
if not (stack and stack.pop() == bracket_dict[bracket]):
    return False
```
В конце мы проверяем как там дела у нашего стэка, если строка пришла корректная, то согласно условиям вложенности скобок,
мы от`pop`-или наш стэк так что он стал пустым и возвращаем `True`, а если что-то ещё осталось то возвращаем `False`.
---
---
## 📝 **Min Stack**
### 📌 Задача:
Разработайте стек, который поддерживает следующие операции с константной сложностью O(1):

    MinStack() — инициализирует объект стека.
    void push(int val) — добавляет элемент val в стек.
    void pop() — удаляет верхний элемент из стека.
    int top() — возвращает верхний элемент стека.
    int getMin() — возвращает минимальный элемент в стеке.

Реализация должна обеспечивать `O(1)` время выполнения для каждой операции.
Если по началу условие про `O(1)` пугает, то потом осознаешь, что это просто подсказка, так как тебе сразу говорят какие элементы тебе доступны.

За `O(1)` работает получение значения из словаря по ключу и получения элемента списка по индексу, 
и так как задачи у нас по стэкам, то выбор очевиден.
### ✅ Решение
Основная сложность этой задачи заключается в работе с минимальным элементом стэка, так как весь остальной функционал
реализовать легко, а вот что делать с минимальным элементом и что делать если при вызове `pop()` удаленный элемент оказался минимальным?
```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            val = min(val, self.min_stack[-1])
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```
Построчно разбирать код не вижу смысла, так как это у нас класс, то разберем его по методам которые нам интересны🔪.

И так `__init__` - основная идея в этом методе это инициализировать два стэка(_списка_):
1. `self.stack = []` - стэк куда мы просто будем просто добавлять новые элементы.
2. `self.min_stack = []` - стэк в котором мы будем хранить _иссторию_ минимальных элементов.

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

```

Теперь перейдем к самому главному методу `push`, главный потому-что в его работе и заключается вся "магия"
решения.

Получая новый элемент `val` на запись в наш стэк мы записываем его в основной стэк без каких-либо ухещрений,

А вот с `min_stack` немного повозимся, для начала проверяем, а существует ли `min_stack` вообще, 
если нет, то просто записываем `val` в наш стэк минимальных значений так как единственный элемент стэка у нас всегда будет и
минимальным и максимальным элементом.

Если `min_stack` у нас существует, то мы сначала сравниваем `val` с последним элементом стэка, так как последний элемент стэка является минимальным 
на данный момент. 

Если `val < self.min_stack[-1]`, то мы просто записываем `val` в конец `min_stack` и `val` становиться новым минимальным элементом списка. 

Если `val > self.min_stack[-1]`, то мы записываем в конец `min_stack` ещё раз последний 
элемент `min_stack` тем самым отображая, что минимальный элемент не изменился.

Нарисуем табличку, чтобы лучше понять о чем идет речь:

Допустим на вход будем подовать поочередно следующий элементы:
[1,2,0,1,-3]

| stack | []   | [1]   | [1,2]   | [1,2,0]   | [1,2,0,1]   | [1,2,0,1,-3]   |
|---------|------|-------|---------|-----------|-------------|----------------|
| min_stack  | `[]` | `[1]` | `[1,1]` | `[1,1,0]` | `[1,1,0,0]` | `[1,1,0,0,-3]` |

Теперь вызовем три раза подряд `pop()` и `getMin()`, чтобы посмотреть что будет происходить.


| pop() | stack | min_stack | getMin() |
|-------|-------|---------|----------|
| 0     | `[1,2,0,1,-3]` |`[1,1,0,0,-3]`| `-3`     |
| 1     | `[1,2,0,1]`|`[1,1,0,0]`| `0`      |
| 2     |`[1,2,0]`|`[1,1,0]`| `0`      |
| 3     |     `[1,2]`    |    `[1,1]`     | `1`       |
---
## 📝 **Valid Parentheses**
### 📌 Задача:
На вход подается строка содержащая только символы  `(` `)`, `{` `}`, `[`  `]`. 
Необходимо проверить строку на правильность закрытия скобок.
### ✅ Мое Решение
Мое решение отходит от классического решения этой задачи, но я всё равно им горжусь.
---