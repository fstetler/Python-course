nats = []

for i in range(1000):
	if i % 3 == 0:
		nats.append(i)
	elif i % 5 == 0:
		nats.append(i)

#print(nats)		
print(sum(nats))