### Note day du model duoc export ra va cac su dung.
___
**Install requests**
```bash
python -m pip install requests
```
**1: check login**
```python

tester = login() # login la class
print(tester.verify('admin','admin'))

```
**Cac ham trong Class login:**

1. verify
```python
verify(username, password) # 
```
return array gom 3 gia tri status, error, token. Token chi co khi dang nhap thanh cong.