## SpApi - Pyhon библиотека для простого доступа к api серверов #СП
Поддерживаемые сервера:
Список поддерживаемых серверов - https://github.com/ronanru/spapi

### Установка
```
Создаёте в корне своего проекта папку modules(или любое другое имя) в неё копируете папку spapi из этого репозитория
```
### Использование
```python
from modules import spapi

api = spapi.SpApi("spm") # вместо spm пишете нужный сервер если он есть во вкладке 'Поддерживаемые сервера' выше
```
#### Получение сообщений в чате
```python
data = api.getLastChatMessages(5).messages # 5 - лимит сообщений, максимум 50
print(data)
```
Пример вывода:
```json
[
  {
    "name": "POHAH", // Ник
    "time": "1605443729874", // Время отправки 
    "message": "Привет!", // Сообщение
    "uuid": "a3211a1b-510d-440d-8442-070028b7a313" // UUID профиля отправителя
  }
]
```

#### Получение игроков онлайн
```python
data = api.getOnlinePlayers().players # 5 - лимит сообщений, максимум 50
print(data)
```
Пример вывода:
```json
{
	"players": [{
		"nickname": "Steve",
		"uuid": "8667ba71-b85a-4004-af54-457a9734eed7"
	}],
	"count": 1,
	"max": 69
}
```

#### Получение времени на сервере
```javascript
spapi.getServerTime().then({ timeOfDay, ticks, formated } => {
	//timeOfDay - 'DAY' или 'NIGHT'
	//ticks - Время в тиках
	//formated - Время в 24 часовом формате
	//Подробнее про тики и т.д. - https://minecraft.gamepedia.com/Daylight_cycle#24-hour_Minecraft_day
	console.log({ timeOfDay, ticks, formated });
}).catch(err => console.errror(err));
```
Пример вывода:
```json
{
	"timeOfDay": "DAY",
	"ticks": 6000,
	"formated": "12:00"
}
```

#### Получение погоды на сервере
```javascript
spapi.getServerWeather().then(weather => {
	//weather - 'CLEAR', 'RAIN' или 'THUNDER'
	console.log(weather);
}).catch(err => console.errror(err));
```
Тут и так все понятно, примеры не нужны
