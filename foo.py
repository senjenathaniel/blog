from pymongo import MongoClient as p

client = p('mongodb+srv://krystl-pilot:VzBWa92kkCGp@cluster0.kzqda.mongodb.net/sample_training?ssl=true&ssl_cert_reqs=CERT_NONE')

companies = client.sample_training.companies

print(companies.find_one())
