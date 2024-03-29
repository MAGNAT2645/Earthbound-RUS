[![Новая форма QIWI](https://i.imgur.com/DXbNi1L.png)](https://my.qiwi.com/Yvan-ZjZkejXn2O) [![Группа ВК](https://i.imgur.com/xmwABcp.png)](https://vk.com/mother123) [![Steam Group](https://i.imgur.com/BQMjWqb.png)](https://steamcommunity.com/groups/earthbound-mother-ru)

# О проекте
Полноценная русская локализация игры Earthbound.
Не забудьте прочитать [статью по установке патча](https://github.com/MAGNAT2645/Earthbound-RUS/wiki/%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0).
Если Вы нашли ошибку в переводе (или любой другой баг) или хотите помочь улучшить качество перевода, обращайтесь [сюда](https://vk.com/topic-75212704_40416271).

**[ОСНОВА ПЕРЕВОДА И ИНСТРУМЕНТЫ ДЛЯ ЛОКАЛИЗАЦИИ ВЗЯТЫ ОТСЮДА](https://github.com/Crystalwarrior/EarthBound-Russian-Translation)**

# Известные баги (**рекомендовано** к прочтению)
* **Улучшенное меню экипировки**: когда у игрока доступно несколько экипируемых предметов для одного слота, игра может резко закрыть меню экипировки и последующее открытие любого окна может вызвать глитч, который обычно исправляется путём закрытия и повторного открытия главного меню команд (кнопка **X**).
  Этот баг возникает из-за ограничений самой игры. Чтобы его избежать, старайтесь выбрасывать из инвентаря старые предметы перед экипировкой нового ЛИБО экипируйте предметы через меню `Вещи` (командой `Исп.` по предмету).
* **Инвентарь** (`Вещи`): иногда предметы с длинным названием могут не влезать в окно инвентаря и вызывают переполнение нижних рядов инвентаря (предметы из нижних рядов будто исчезают, хотя это не так).
  Для избежания этого бага мы стараемся сокращать названия предметов (на момент написания именно этого текста баг больше не возникал).
  Если баг всё же возник, достаточно `навести порядок` в инвентаре т.е. передать любой предмет самому себе (иногда нужно делать это несколько раз). Таким образом владелец предмета переместит этот предмет в конец своего инвентаря.
* **Тайлсеты** (графическая составляющая мира): некоторые тайлсеты прозрачны, если зайти за них. Данный баг возникает лишь в некоторых местах, а значит не помешает игре.

# Отличия от оригинальной игры
* Добавлена поддержка патча MSU-1. Что он делает? Добавляет новые ощущения для Ваших ушей.
  Во вкладке Wiki есть [статья](https://github.com/MAGNAT2645/Earthbound-RUS/wiki/%D0%9F%D0%B0%D1%82%D1%87-MSU-1) по установке/применению этого патча.
* Исправлены некоторые недочёты оригинальной игры.
* Возвращены многие удалённые в EarthBound элементы из оригинальной Mother 2 (подобных изменений будет много).
* Некоторые элементы перевода похожи на русский перевод от Chief-Net для EB Zero (так было решено, потому что в EB многое взято из EB Zero).
* Улучшено меню экипировки (больше информации об экипировке).
* Добавлен спринт (ускоренное передвижение), работает при удержании кнопки Y.
* Быстроброды (Skip Sandwich) больше не ускоряют игрока (т.к. спринт взял на себя эту роль), но временно отключают спавн врагов.
* Добавлены иконки в боевое и главное меню команд (перед текстом `Бить`, `Вещи`, `Защита` и т.д.).
* Добавлены заголовки с именами для диалоговых окон.
* Переработано управление:
    - A/L: Говорить или проверить (больше не будет текста `Никаких проблем.` и `С кем ты разговариваешь?`).
    - X: Открывает главное меню команд (`Вещи`, `Экипир.` и т.д.).
    - B: Открывает окно ОЗ/ОП и отображает количество налички.
    - Y: Спринт при удержании кнопки.
    - Start: Открывает/закрывает карту.
* Уникальные внешние (вне боя) спрайты для каждого врага в игре (придаёт атмосферу Mother 3).
* Спрайты некоторых персонажей были отредактированы так, чтобы они больше походили на глиняные фигурки с Wiki.
* Уникальные спрайты для всех 4 роботов (в конце игры).
* Добавлены диагональные варианты для спрайтов персонажей, которые могут временно вступить в команду (Порки, Пики, Кинг, Тони, Бубль-гумыч, Летуны, Человек-Данж). Сюда также входят:
    - Все крохотные спрайты в Затерянном Подземелье (Несс, Пола, Джефф, Пу).
    - Все призрачные спрайты (Нормальные и крохотные).
    - Кристаллизованный спрайт (Нормальный и крохотный).
    - Мишка Тедди (Нормальный и крохотный).
* Перерисованы греческие символы, указывающие ранг ПСИ-способностей.
* Добавлена возможность экипировать предмет прямо через инвентарь (команда `Исп.`).
* Полноценный перевод ATM Debug Menu и разные исправления для MOTHER 2 ROM DEBUG.
* Расширена способность Джеффа "изучать" врагов:
    - Добавлены следующие разделы:
      - `Статус`:
        - Добавлена возможность просматривать ОЗ и ОП врагов (но у некоторых боссов просмотреть нельзя)
        - Добавлены остальные характеристики: `Скорость`, `Воля` и `Удача`
      - `Уязвимости`
      - `Описание`:
        - Добавлена небольшая информация (в том числе стратегии) о каждом враге

# Благодарности
* [MrTenda](https://github.com/mrtenda): основной инструмент для работы с ROM'ом - [CoilSnake](https://mrtenda.github.io/CoilSnake/).
* [CrystalWarrior](https://github.com/Crystalwarrior): первоначальная работа с ROM'ом, исходный текст игры (и скрипты), перевод начала игры и некоторых отдельных участков.
* [ShadowOne333](https://github.com/ShadowOne333): огромная помощь с редактированием труднодоступных элементов игры, предоставил разные скрипты.
* [MaternalBound Redux](https://github.com/ShadowOne333/MaternalBound-Redux): многие изменения взяты с этого хака.
* [alt6502](https://forum.starmen.net/members/alt6502): иконки (кроме меча) и скрипт для боевого меню.
* [limonow1](https://vk.com/id205829687): большая помощь с большим переводом большого количества большого текста.
* [ВК Сообщество по играм Mother (и все участники)](https://vk.com/mother123): огромная поддержка, идеи и помощь с вычиткой перевода.
* Все, кто снимал (или стримил) прохождение игры с переводом в период его вычитки.
* и другие.

# Скриншоты
![](https://i.imgur.com/bvLK0qL.png)
![](https://i.imgur.com/raQQ8rk.png)
![](https://i.imgur.com/6CXjwnT.png)
