import json
import types





class FEDict(dict):
	def __getattr__(self, key):
		if key in self:
			return self[key]
		else:
			raise AttributeError("Attribute not found:" + key)

	def __setattr__(self, key, val):
		self[key] = val

	def __delattr__(self, key):
		if key in self:
			del self[key]
		else:
			raise AttributeError("Attribute not found:" + key)

	def printAll(self):
		for key in self:
			print(str(key) + ": " + str(self[key]))

	def isClass(self, obj):
		return isinstance(obj, (type, types.ClassType))

class FEJStory(object):
	guid = 0
	name = ""
	seed = 0
	bg = ""
	title = ""
	intro = ""
	events = []
	rows = 0
	columns = 0

	def __init__(self, data):
		global rows, columns
		try:
			#self.fail = data["fail"]
			self.guid = data["guid"]
			self.name = data["storyName"]
			self.seed = data["seed"]
			self.bg = data["background"]
			self.title = data["title"]
			self.intro = data["introduction"]
			for sEvt in data["storyEvents"]:
				if (ord(sEvt[0])-48) > self.rows:
					self.rows = ord(sEvt[0])-48
				if (ord(sEvt[1].lower())-96) > self.columns:
					self.columns = ord(sEvt[1])-96
				evt = FEJEvents(sEvt, data)
				self.events.append(evt)
		except KeyError as kErr:
			print("Story key " + str(kErr) + " is not found in JSON.\nA Story Requires:\n  GUID\n  Story Name\n  Seed#\n  Background\n  Title\n  Introduction\n  Story Events")
			raise SystemExit

	def printStory(self):
		print("GUID:      " + str(self.guid))
		print("SN:        " + self.name)
		print("Seed:      " + str(self.seed))
		print("SBG:       " + self.bg)
		#Other info to print goes here
		print("Title:     " + self.title)
		print("Intro:     " + self.intro)

		print("\nEvents")
		#for r in range(self.rows):
		#	for c in range(self.columns):
		#		#if (lambda x: )
		#		print(c)
		for evts in self.events:
			evts.printEvent()


class FEJEvents(object):
	name = ""
	key = ""
	row = 0
	column= 0
	eType = ""
	background = ""
	

	def __init__(self, key, data):
		try:
			#self.fail = data["fail"]
			self.key = key
			evt = data["storyEvents"][key]
			self.name = evt["eventName"]
			self.bg = evt["background"]
			self.eType = evt["eventType"]
			self.row = ord(key[0].lower()) - 48
			self.column = ord(key[1].lower()) - 96
			if self.eType == "Choice":
				print("Choice")
				
				print("")
		except KeyError as kErr:
			print("Event key " + str(kErr) + " is not found in JSON.")
			raise SystemExit

	def printEvent(self):
		print("\tNode:\t" + self.key + ' (' + str(ord(self.key[0].lower())-48) + "," + str(ord(self.key[1].lower())-96) + ")")
		print("\t\tEvent:\t" + self.name)
		print("\t\tBG:\t" + self.bg)
		print("\t\tType:\t" + self.eType)


class FEChoice(object):
	choices = []

	def setChoice(self, option, key, data):
		if 1 == 2:
			print("False")
		self.choices.append()


json_file = open('/Users/gmorin/Documents/Program/FateEngine/testStory.json')
json_str = json_file.read()
json_data = json.loads(json_str)

fes = FEJStory(json_data)
fes.printStory()

#print(jsonToObj(json_data))



