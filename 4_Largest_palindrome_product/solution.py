def isPalindrome(x):
	chars = list(x)
	output = True
	for i in range(len(chars)):
		j = chars[i]
		k = chars[-i-1]
		if (j != k):
			output = False
			break
	return output

def findHighestPalindrome():
	h = 0
	numbers = range(100, 1000)
	for i in range(len(numbers)):
		num1 = numbers[-i-1]
		for j in range(len(numbers)):
			num2 = numbers[-j-1]
			p = num1*num2
			if isPalindrome(str(p)):
				if p > h:
					h = p
	return h

		
print(findHighestPalindrome())
		