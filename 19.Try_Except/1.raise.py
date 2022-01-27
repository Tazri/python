# try to throw error
x = 'throw';

if type(x) != int :
    raise Exception("This is error.");

print(">>> this line could't not execute.");