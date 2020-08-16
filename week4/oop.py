class Flight:
	def __init__(self, origin, destination, duration): #example of constructor
		self.origin = origin
		self.destination = destination
		self.duration = duration
		self.passengers = []
	def __str__(self):
		return "origin: " + self.origin + " destination: " + self.destination + " duration: " + str(self.duration)

def main():
	#creates flight:
	f = Flight("New York", "Paris", 540)

	print(f)

if __name__ == "__main__": #if I am running this file, I should do main() we basically only this if we import this file
	main()
