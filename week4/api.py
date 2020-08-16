import requests

def main():
	#example of API
	res = requests.get("http://api.fixer.io/latest?base=USD&symbols=EUR") #doesn't work because I don't have a key
	if res.status_code != 200:
		raise Exception("ERROR: API request unsuccessful.")
	data = res.json()
	print(data)

	#another example:
	base = input("First Currency: ")
	other = input("Second Currency: ")
	res = requests.get("http://api.fixer.io/latest", params={"base": base, "symbols": other})
	data = res.json()
	rate = data["rates"][other]
	print(f"1 {base} is equal to {rate} {other}")

if __name__ == "__main__":
	main()

"""
HTTP METHODS:
	-GET: retrieve resource
	-POST: create a new resource
	-PUT: replace
	-PATCH: update
	-DELETE: delete a resource

STATUS CODES:
	-200 OK (Success!)
	-201 Created (Success!)
	-400 Bad Request
	-403 Forbidden
	-404 Not Found
	-405 Method Not Allowed
	-422 Unprocessable Entity

Sometimes you need an API keys
"""