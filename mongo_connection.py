from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.cast
data=db.repos.find()
f = open('cast.txt','w')
count=0
a=set()
def recur_keys(i,j,count):
	if isinstance(i,dict):
		if 'language' in i:
			f.write(str(i))
			exit(0)
		count=count+1
		for j in i:
			if isinstance(i[j],dict):
				recur_keys(i[j],j,count)
for i in data:
	recur_keys(i,'',count)
print(a)
f.close()
ans = db.repos.distinct("payload.pull_request.base.repo.language")
print(ans)
