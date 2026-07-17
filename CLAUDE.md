# ftlr — Project Guide

## Что это

Python CLI для батч-правки XMP-файлов (sidecar файлы RAW-фото). Позволяет применить поправки экспозиции, контраста и др. ко всем фотосетам разом — до обработки в Lightroom.

---

## Место в экосистеме

```
Карта памяти → justin import → stage2.develop
                                    ↑
                               ftlr (XMP batch edit)
```

Запускается перед или во время работы в Lightroom. Например: снял в пасмурную погоду — хочешь поднять экспозицию сразу во всех 6000 фото перед тем как открывать Lightroom.

---

## Стек

- Python, Typer

---

## Поддерживаемые параметры

Определены в `src/ftlr/config.py`:

| Ключ XMP | Флаг CLI | Диапазон |
|----------|----------|----------|
| `crs:Exposure2012` | `-e / --exposure` | -5 … +5 |
| `crs:Contrast2012` | `-c / --contrast` | -100 … +100 |

Добавить новый параметр = одна строка в `__descriptions` в `config.py`.

---

## Структура

```
src/ftlr/
├── runner.py       # Точка входа, Typer app; сигнатура команды строится из CONFIG
├── config.py       # Список поддерживаемых параметров (Config dataclass)
├── xmp.py          # Xmp — чтение/запись XMP (построчный парсинг)
├── xmp_types.py    # XmpType, Factory — типы значений (real, integer)
└── modification.py # Modification — применение изменения к Xmp
```

---

## Git

Semantic commits: `feat:`, `fix:`, `refactor:`, `chore:`
