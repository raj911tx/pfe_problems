str = 'X-DSPAM-Confidence:0.8475'
# print(str.find(':'))
new_str=str[str.find(':')+1:]
print(float(new_str))