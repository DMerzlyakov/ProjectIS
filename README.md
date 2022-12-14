# ProjectIS
**Информационно-справочная система контроля проектов**

### Команда 2:

- Мерзляков Данила
- Саакян Давит
- Капралов Никита
- Телицын Егор
- Кучерявенко Никита
- Баранов Александр
- Костюченко Илья
Проект: https://github.com/DMerzlyakov/ProjectIS

Сценарии атрибутов качества: https://docs.google.com/spreadsheets/d/1vZhYrWvsmRe6hDoN15rkn3oRAOgsZTTs8LZ17UNmrIA/edit#gid=0

## Описание приложения
Целью проекта автоматизации учета ресурсов является повышение эффективности работы в области управления ресурсами. Компания планирует заключить договор с Подрядчиком, с целью разработки автоматизированной системы, которая будет интегрирована во внутренний IT ландшафт (интеграция с кадровой, бухгалтерской и другими системами). Пользователями системы будут сотрудники HR департамента, а также менеджеры проектов (ПМ) технические и линейные руководители. Также предполагается, что все остальные сотрудники будут иметь ограниченный доступ к своему профилю.

Софт Технолоджи как Заказчик рассчитывает, что Подрядчик в рамках этого проекта создаст единую систему автоматизации управления ресурсами, которая удовлетворит предъявляемым требованиям и будет реализована максимально эффективно с точки зрения последующего владения системой.

Ключевые аспекты, которые следует учитывать при создании системы:

Снижение расходов – применение системы должно снизить стоимость процессов управления (например, за счет экономии времени, затрачиваемого сотрудниками на задачи управления ресурсами)
Автоматизация – максимальное исключение ручного труда в процессах управления ресурсами

Интеграция – система должны быть интегрирована с кадровой подсистемой (API) бухгалтерской системой (API) и SSO системой ([тут гипотетическая ссылка на документацию])

Простота и эргономичность – общие подходы к интерфейсу (look and feel) для всех пользователей, ориентированность на бизнес-процессы, простые и понятные интерфейсы и действия

Гибкость – способность системы развиваться при росте и расширении профиля деятельности компании

Производительность – способность системы обеспечивать приемлемый уровень работоспособности даже при росте нагрузки и (или) проблемах с оборудованием.


## Правила работы с системой контроля версий Git
Каждый участник из команды имеет свою ветку. Работа ведется именно в своих ветках. Всех своих соотрудников мы просим граммотно называть 
коммиты, так как потом мы обращаем внимание на то, как он пришел к такому или иному решению. Так же мы стараемся как можно
чаще фиксировать код, и всегда работать только с последней версией кода. 

Используем ветвление проекта, который позволяет нам
выделять отдельные потоки разработки. Разработка каждой новой фичи ведется в отдельной ветке, и этот процесс предполагает 
наличие центрального хранилища. Вместо фиксации непосредственно в своей локальной основной ветке разработчики создают
новую ветку каждый раз, когда они начинают работу над новой функцией. Помимо изоляции разработки функций, ветви позволяют 
обсуждать изменения с командой при помощи pull request. 

Дальше нужно загрузить изменения из локального репозитория в удаленный, чтобы локальные изменения 
стали доступными для коллег. Бывает так, что несколько сотрудников работали над одним и тем же
файлом, и при их синхронизации могут быть конфликты. Необходимо эффективно распределять работу между участниками разработки, 
чтобы таких общих файлов было как можно меньше. После выбора нужных файлов добавляет их в коммит 
и пушим. 

Как только кто-то завершает разработку функции, он не сразу вливает 
ее в main. Вместо этого он отправляет ветвь функций на центральный сервер и делает pull request с просьбой влить изменение в main. 
Это дает другим разработчикам возможность ознакомиться с изменениями до того, как они станут частью основной кодовой базы.

В ветке main собираем весь рабочий код, после чего выпускаем релиз



## Схема архитектуры
![Архитектура](images/Architecture.png)

## Модель данных
![Модель БД](images/DB_model.png)

## Используемых технологии

- Python
  - FastApi
  - SqlAlchemy
- PostgreSQL
- JavaScript
- React
- Docker

## Софт Технолоджи
Почтовый адрес: contact@softtel.ru

Телефон: +7(985)111-11-11

Город: Москва


## Roadmap

- [x] Формирование архитектуры проекта
- [x] Формирование правила работы с контролем версий
- [x] контейнеризация всего приложения
- [x] Создание БД
  - [x] Схема БД
  - [x] Создание Docker образа
  - [x] ORM на python
- [ ] Сервер
  - [x] Часть функционала
  - [x] Создание Docker образа
  - [ ] Полный функционал
- [ ] Клиент
  - [x] Часть функционала
  - [x] Создание Docker образа
  - [ ] Отрисовать UI/UX
  - [ ] Полный функционал
- [ ] Тестирование
  - [ ] БД
  - [ ] Сервер
  - [ ] Клиент


