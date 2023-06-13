# problem link : https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S?fbclid=IwAR1cupDCZHgOy-nd6SFY-Sh1SsJjisLOREeLAKSpTXWggunF_siIkIcy2wA
# problem name : S. Max Split
# judge name : codeforce
# language version : Python 3.9.2
# status : accepted

string = input();
string_list = [];
r = 0;
l = 0;
sub_string = "";

for ch in string:
    if ch == "R":
        r+=1;
    elif ch == "L":
        l += 1;
    sub_string += ch;
    # check it balanced or not
    if r == l :
        string_list.append(sub_string);
        r = 0;
        l = 0;
        sub_string = "";

print(len(string_list));
for sub in string_list:
    print(sub);
