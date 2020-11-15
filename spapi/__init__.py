from urllib.request import Request, urlopen
import json

# Ошибки
class Error(Exception):
    pass

class ApiError(Error):
    pass





class GetOnlinePlayers():
	def __init__(self, players, count, max):
		self.players = players
		self.count = count
		self.max = max

	def __repr__(self):
		return f"<GetOnlinePlayers max={self.max}, count={self.count}, players='{self.players}'>"
		


class GetLastChatMessages():
	def __init__(self, messages):
		self.messages = messages

	def __repr__(self):
		return f"<GetLastChatMessages messages='{self.messages}'>"
		


class GetServerTime():
	def __init__(self, timeOfDay, ticks, formated):
		self.timeOfDay = timeOfDay
		self.ticks     = ticks 
		self.formated  = formated

	def __repr__(self):
		return f"<GetServerTime timeOfDay='{self.timeOfDay}', formated='{self.formated}', ticks={self.ticks}>"
		


class GetServerWeather():
	def __init__(self, weather):
		self.weather = weather

	def __repr__(self):
		return f"<GetServerWeather weather='{self.weather}'>"
		






# Основной класс
class SpApi():
	def __init__(self, server):
		self.server = server

	def __repr__():
		return f"<SpApi server={self.server}>"


	def parsing(self, fetch):
		req = Request(f"https://sp-api.ru/{self.server}/{fetch}", headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urlopen(req).read().decode()

		try:
			api = json.loads(webpage)

			if api['error'] == True:
				raise ApiError("When requesting api, the key 'Error' returned True")

			return api


		except Exception as e:
			raise ApiError(str(e))


		


	# Вызываемые функции
	def getLastChatMessages(self, limit=50):
		return GetLastChatMessages(self.parsing("chat")['messages'][:limit])
		 

	def getOnlinePlayers(self):
		parse = self.parsing("online")

		return GetOnlinePlayers(parse['players'], parse['count'], parse['max'])


	def getServerTime(self):
		parse = self.parsing("time")

		minutes = round( (parse['ticks'] % 1000) * 0.06 )
		if len(str(minutes)) == 1:
			minutes = f'0{minutes}'
		formated = f"{round( parse['ticks'] / 1000 + 6) }:{minutes}"


		return GetServerTime(parse['time'], parse['ticks'], formated)

	def getServerWeather(self):
		return GetServerWeather(self.parsing("weather")['weather'])

