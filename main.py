import hashlib
s='betabeta'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
