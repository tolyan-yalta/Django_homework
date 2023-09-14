### Домашние задания по курсу "Фреймворк Django (семинары)"

### Добавлено д/з 1 (homework_1_app)

### Добавлено д/з 2 (homework_2_app)

### Добавлено д/з 3 (homework_3_app)

### Добавлено д/з 4 (homework_4_app)

### Добавлено д/з 5

Для проекта создан "Superuser":   
Username: admin   
Password: admin

В файле settings.py применена настройка "LANGUAGE_CODE = 'ru-ru'"

Через административную панель создан пользователь (Права доступа: Активный и Статус персонала):   
Имя пользователя: user   
Пароль: User123456#

В приложении  (homework_2_app) в файле admin.py создано подключение к административной панели модели "User" из файла models.py. Добавлено отображение полей "list_display", сортировка по имени "ordering", фильтрация "list_filter" (по телефону, адресу и дате регистрации) и поиск по имени "search_fields".

Там же создано подключение к административной панели модели "Product". Добавлено отображение полей "list_display", сортировка по имени "ordering", фильтрация "list_filter" (по цене, количеству и дате добавления) и поиск по имени "search_fields". Создана детальная настройка отображения полей "fieldsets": 
* Поле описания товара "description" сделано сворачиваемым
* Поле изображения товара "image" то же сделано сворачиваемым и добавлено дополнительное поле "preview" предпросмотра, выводящее изображение товара в урезанном размере.

Там же создано подключение к административной панели модели "Order". Добавлены медтоды для получения PrimaryKey ордера, получения имени связанного пользователя и названия связанного товара. Добавлено отображение полей "list_display" (ID ордера, дата создания ордера, имя пользователя и название товара), сортировка по ID ордера "ordering", фильтрация "list_filter" (по дате создания ордера, имени пользователя и названию товара) и поиск по ID ордера "search_fields".
