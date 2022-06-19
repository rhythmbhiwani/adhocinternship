import os
for i in range(1,11):
    print("launching .... adhoc{}".format(i))
    os.system("kubectl run adhoc{} --image=alpine --command ping 8.8.8.8".format(i))
