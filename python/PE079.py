successful = open("PE079.txt", 'r')
keys = [k for k in successful.read().split('\n')]
pre = [[] for i in range(10)]
post = [[] for i in range(10)]
for key in keys:
	k = [int(key[i]) for i in range(len(key))]
	if k[1] not in post[k[0]]:
		post[k[0]].append(k[1])
		pre[k[1]].append(k[0])
	if k[2] not in post[k[0]]:
		post[k[0]].append(k[2])
		pre[k[2]].append(k[0])
	if k[2] not in post[k[1]]:
		post[k[1]].append(k[2])
		pre[k[2]].append(k[1])
print(keys)
print(pre)
print(post)

# by inspecting, 2 non occuring integers and no integers appears more than twice.
# 73162890