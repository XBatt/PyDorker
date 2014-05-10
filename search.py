from google import search
import os.path

def main(search_term,amount):
	print "The results will now be printed and saved to a text file named results.txt in the directory of this python script\n"
	for url in search(search_term, stop=amount):
		print(url)	
		if os.path.isfile('results.txt'):
			txt2 = open("results.txt", "a")
			txt2.write(url)
			txt2.write("\n")
		else:
			txt2 = open("results.txt", "w")
			txt2.write(url)
			txt2.write("\n")
			
			
if __name__ == '__main__':
	print("""
______     ______           _             
| ___ \    |  _  \         | |            
| |_/ /   _| | | |___  _ __| | _____ _ __ 
|  __/ | | | | | / _ \| '__| |/ / _ \ '__|
| |  | |_| | |/ / (_) | |  |   <  __/ |   
\_|   \__, |___/ \___/|_|  |_|\_\___|_|   
       __/ |                              
      |___/         	by XBatt
""")
	input1 = raw_input("Enter the search term (Example: inurl:https, Penetration Testing): ")
	input2 = int(raw_input("Enter the maximum amount of results you want: "))
	main(input1,input2)
