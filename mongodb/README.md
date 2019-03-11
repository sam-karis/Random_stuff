## Mongo Database Basics

---

Show available databases

```
show dbs
```

Create/connect to a new database

```
 use mongoBasics
```

Add a new document to a collection(posts)

```
db.posts.insert({title: 'Hello world'})
```

View available collection in the

```
show collections
```

Load seeded data from a file

```
load("./mongodb/seeds.js")
```

Count documents in a collection

```
db.users.count() # gives a total count of users documents
db.posts.count() # gives a total count of post documents

```

query all documenets in a collection

```
db.users.find()
db.posts.find()

```

Limit the number of documents

```
db.posts.find().limit(2) # return only two documents
```

query specific user

```
db.users.find()[1]
db.posts.find()[2]

```

#### Manage collections

Get database corrections

```
db.getCollectionNames() # returns a list of all collections

```

Create collection index

```
db.posts.createIndex({title: 1})
```

Get collection index

```
db.posts.getIndexes()
```

Delete collection index

```
db.posts.dropIndex('title_1')
```

Get one document from a collection

```
db.posts.findOne()
```

Queries with query parameters

```
db.posts.findOne({})
db.posts.find({})
```

Queries with Projections(2nd parametes)

```
db.posts.findOne({}, {body:false, description:false})   # do not return body and description
db.posts.find({}, {body:false, description:false})
db.posts.find({},{_id:false})   # mute id field
db.posts.find({},{title:true, _id:false}) # return documents titles only
db.posts.find({title:'How to workout'}) # return document with specific title
db.posts.find({title:'does not exist'})  # returns nothing
```

Query for multiple documents using or oparator

```
db.posts.find({$or: [{title:'How to workout'}, {title:'Parenting 101'}]}) # return 2 documents
```

Update a document

```
db.posts.update(
    {author: ObjectId("5c8632b4523762ad70b69223")},
    {$set:{tags:['foo', 'bar', 'interesting'],
    title: "I'm an updatesd title"}})
```

FInd available fields for a document

```
Object.keys(db.posts.findOne())
Object.keys(db.posts.find()[1])
```

Sort documents by a field

```
b.posts.find({}, {title: true}).sort({title: 1}) # sort title in ascending order
db.posts.find({}, {title: true}).sort({title: -1}) # sort title in descending order
```

Pagination of documents from a collection  
Pagination formula: limit = number of records on each page, skip = number of records on each page \* (page number - 1)

```
db.posts.find({}, {title: true}).limit(2) # return the first 2
db.posts.find({}, {title: true}).limit(2).skip(2) # return after first 2
db.posts.find({}, {title: true}).sort({title: 1}).limit(2).skip(3) # return after first 3 in a sorted order
```
