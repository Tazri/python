# let's do something error

try :
    print(10/0);
except :
    print(">>>> error is here. <<<<");
finally :
    print(">>> it run whatever what <<<");

try : 
    print("\n\n>>> No error <<<");
except :
    print(">>> It can not run because no error here <<<");
else : 
    print(">>> it run because try block code is correct <<<");
finally :
    print(">>> it run whatever what <<<");