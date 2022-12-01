with open('main.txt', 'r') as f:
    temp = f.read()
 
code = compile(temp, 'main.txt', 'exec')
exec(code)
