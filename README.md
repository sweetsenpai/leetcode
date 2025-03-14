# 🚀 LeetCode Solutions

📚 **Коллекция решений задач с LeetCode** на **Python**.  
🔹 Решения разделены по темам.  
🔹 Включают пояснения и альтернативные способы решения.  
🔹 Все решения протестированы с помощью `pytest`.

---

## 📁 **Структура репозитория**

- **`Arrays/`** — задачи по массивам:
    - 📌 [`two_sum.py`](Arrays/two_sum.py) — решение задачи *Two Sum*.

- **`Tests/`** — тесты для решенных задач.

---
# Решения
---
## 📝 **Two Sum Problem**
### 📌 Задача:
Найти два числа, которые в сумме дают заданное число.

### 💡 **Решение (Python)**:
```python
from typing import List

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

## 🏆 **Прогресс**

| Категория             | Решено |
|----------------------|-------|
| **Массивы**         | ✅ 1/1 |

(Обновляется вручную)
