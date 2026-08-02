# Mongod

blob:[https://app.hackthebox.com/3f1ac36f-756b-41df-a396-10f3abf85456](https://app.hackthebox.com/3f1ac36f-756b-41df-a396-10f3abf85456)

mongodb
curl -O [https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.4.7.tgz](https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.4.7.tgz)
tar xvf mongodb-linux-x86_64-3.4.7.tgz
cd mongodb-linux-x86_64-3.4.7/bin
./mongo mongodb://\{target_IP\}:27017
db.flag.find().pretty();

*[image unavailable]*

*[image unavailable]*
