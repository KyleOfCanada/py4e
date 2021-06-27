str = 'X-DSPAM-Confidence: 0.8475 '

spcPos = str.find(' ')
strNums = str[spcPos:]
strNums = strNums.strip()
floatNums = float(strNums)
print(floatNums)
