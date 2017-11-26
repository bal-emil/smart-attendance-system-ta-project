from pymongo import MongoClient

id_name = ["Alec", "Emil", "Greg", "Phong", "Thinh"]
photo_url = ["https://image.ibb.co/mPMU7m/Alec_0.jpg",
             "https://image.ibb.co/ccA0DR/Emil_4.jpg",
             "https://image.ibb.co/ixsQf6/Greg_3.jpg",
             "https://image.ibb.co/miKexm/Phong_8.png",
             "https://image.ibb.co/eXA8q6/Thinh_2.png"]

# Connect to MongoDb
client = MongoClient('mongodb://localhost:27017')
db = client['ta_sas']

# Insert to UserClassifyID Database
# Drop this database if exist
db.drop_collection('UserClassifyId')

# Push to this database name and id
db_to_push = db['UserClassifyId']

for i in xrange(len(id_name)):
    post = {"userName": id_name[i],
            "classifyId": i,
            "photo": photo_url[i]}
    post_id = db_to_push.insert_one(post).inserted_id
    print(post_id)