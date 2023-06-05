s  = input('Enter text ').split()
r = [i.strip('.,?\n').lower() for i in s]
print(r)
r = set(r)
print(len(r))