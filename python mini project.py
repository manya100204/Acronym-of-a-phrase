#defing the function to find the acronym
def acr(phrase):
#Ignore prepositions.
	clean_input=phrase.replace('of',"")
#converting the string to list
	lst=clean_input.split()
	output=""
#interating the list
	for word in lst:
		output+=word[0].upper()
#returning the output
	return output
#to take inputs
phrase=input('Enter the string to create a Acronym: ')
#calling the funtion and printing the Acronym
print("The Acronym for the phrase",phrase,"is",acr(phrase))

C:\Users\91700\PycharmProjects\pythonProject3\python mini project.py