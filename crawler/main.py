import requests
from bs4 import BeautifulSoup
url = "https://nbk.acad.ncku.edu.tw/netcheckin/index.php?c=quall_rwd&m=qu"

	
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
 
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "html.parser")
# title = soup.findall("姓名")
# print(title.text)
ans = soup.find("table",class_= "table table-striped")
print(ans)
