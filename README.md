#Task
The task is to create an application that takes a single integer input. The application will download the raw data from the website above (https://mach-eight.uc.r.appspot.com) and print a list of all pairs of players whose height in inches adds up to the integer input to the application. If no matches are found, the application will print "No matches found"

Sample output is as follows:

	> app 139
		
	- Brevin Knight         Nate Robinson
	- Nate Robinson         Mike Wilks


The script asks for a number which is going to be searched by adding 2 heights values in the height list. The script will not iterate n*n times. We are assuming that we only need an unordered combination of heights which being added up will result in the number entered by the user. 

![Screenshot from 2022-02-01 16-23-10](https://user-images.githubusercontent.com/15699676/152055445-95fe5715-1add-42d6-8417-03df49ff1acd.png)

Run 

	python main.py
	
Code will ask for the number to search

	Please enter the desired number...
	Number:

The code will show the pairs of players whose height in inches adds up to the integer input adn the number of matches found.

	Number: 139
	Pair found: [['Brevin Knight'], ['Nate Robinson']] heights [70, 69] add up 139
	Pair found: [['Nate Robinson'], ['Mike Wilks']] heights [69, 70] add up 139
	Matches found: 2


If there are not pairs that satisfies the requested number the result will be:

	Number: 180
	Not matches found
