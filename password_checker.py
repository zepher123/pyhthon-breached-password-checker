import requests

url = 'https://haveibeenpwned.com/api/v3/range/' + 'CBFDA' #kate anomity
res = requests.get(url)
print(res) #200 means good
