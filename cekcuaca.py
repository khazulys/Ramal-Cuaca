import requests, json, os, sys
from time import sleep

def main():
	try:
		os.system('cls' if os.name=='ntp' else 'clear')
		print ("\033[1;32m	  ╦═╗╔═╗╔╦╗╔═╗╦    ╔═╗╦ ╦╔═╗╔═╗╔═╗")
		print ("\033[1;36m	  ╠╦╝╠═╣║║║╠═╣║    ║  ║ ║╠═╣║  ╠═╣ ")
		print ("\033[1;32m	  ╩╚═╩ ╩╩ ╩╩ ╩╩═╝  ╚═╝╚═╝╩ ╩╚═╝╩ ╩ ")
		print ("\x1b[1;30;47m" + "		[+]©Code by Khazul[+]		" + "\x1b[0m")
		api_key = "82619e4af8fd42d0d2bc53791b2217b4"
		city_name = input("\n\033[1;30m[?]\033[1;36mNama kota:\033[1;33m ")
		print ("\033[1;30m[+]\033[1;36mMencoba meramal cuaca")
		sleep(3)
		base_url = "http://api.openweathermap.org/data/2.5/weather?"
		complete_url = base_url + "appid=" + api_key + "&q=" + city_name
		response = requests.get(complete_url)
		x = response.json()
		if x["cod"] != "404":
		    y = x["main"]
		    current_temperature = y["temp"]
		    current_pressure = y["pressure"]
		    current_humidiy = y["humidity"]
		    z = x["weather"]
		    weather_description = z[0]["description"]
		    print("\033[1;30m[√]\033[1;36mResult:\n\n\033[1;33m Suhu (dalam kelvin) = " +
		                    str(current_temperature) +
		          "\n Kecepatan angin (dalam satuan hPa) = " +
        		            str(current_pressure) +
		          "\n Kelembapan (dalam persen) = " +
        		            str(current_humidiy) +
	        	  "\n Cuaca kota",city_name,"= " +
        	        	    str(weather_description))

		else:
		    print("\033[1;31m[x]\033[1;33mKota tidak ditemukan! ")
	except:
		pass
if __name__=="__main__":

	main()
	try:
		a = True
		while a:
			ul = input("\n\033[1;32m[?]\033[1;31mRamal lagi?(y/n):\033[1;35m ")
			if ul == "y":
				main()
			if ul == "n":
				sys.exit("Goodbye Anjayy")

	except:
		pass

