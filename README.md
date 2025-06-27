# new_codex

Этот репозиторий содержит примеры тестов и документацию. Подробнее о метафорах см. [docs/metaphors.md](docs/metaphors.md).

## Генератор иерархии классов

В папке `scripts` находится утилита `generateClassHierarchy.js`, которая создаёт иерархию классов по описанию в формате JSON.

### Использование

```bash
node scripts/generateClassHierarchy.js input.json output.js
```

Файл `input.json` должен описывать корневой класс и его потомков следующей структурой:

```json
{
  "name": "Animal",
  "methods": ["speak"],
  "children": [
    {
      "name": "Dog",
      "methods": ["bark"]
    },
    {
      "name": "Cat",
      "methods": ["meow"]
    }
  ]
}
```

В результате выполнения будет создан файл `output.js` с классами и наследованием между ними.

Tests and docs

## Инструмент перекрёстных ссылок
Файл `crossref.py` собирает все функции, методы и переменные во всём проекте и выводит их координаты в виде списка. Скрипт помогает быстро находить определения объектов.

Запуск:
```
python crossref.py -o crossref.txt
```
После выполнения в файле `crossref.txt` появится перечень ссылок на объекты и строки, где они объявлены.

См. раздел о шаблонах: [docs/templates.md](docs/templates.md).

