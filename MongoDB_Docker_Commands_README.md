
# MongoDB with Docker - Useful Commands

### כניסה לממשק הטרמינל של MongoDB בדוקר
1. **רשימת כל הקונטיינרים הרצים**
   ```bash
   docker ps
   ```
   מציג את כל הקונטיינרים הפעילים במערכת שלך עם מזהי קונטיינרים ושמות.

2. **כניסה לקונטיינר MongoDB דרך הטרמינל**
   ```bash
   docker exec -it <container_name_or_id> mongo
   ```
   מחליף `<container_name_or_id>` במזהה הקונטיינר של MongoDB כדי להיכנס ישירות לקונסול MongoDB.

---

### פקודות בסיסיות לממשק MongoDB

1. **התחברות לבסיס נתונים**
   ```javascript
   use <database_name>
   ```
   יוצר או עובר לבסיס הנתונים בשם `<database_name>`.

2. **הצגת בסיסי נתונים קיימים**
   ```javascript
   show dbs
   ```
   מציג רשימה של בסיסי הנתונים הקיימים.

3. **הצגת כל הקולקציות במסד הנתונים**
   ```javascript
   show collections
   ```
   מציג את כל הקולקציות הקיימות במסד הנתונים.

---

### עבודה עם קולקציות

- **יצירת מסמך חדש בקולקציה (Insert)**
  ```javascript
  db.collection_name.insertOne({ key1: "value1", key2: "value2" })
  ```
  יוצר מסמך חדש בתוך קולקציה.

- **הוספת מסמכים מרובים בקולקציה (Insert Many)**
  ```javascript
  db.collection_name.insertMany([{ key1: "value1" }, { key1: "value2" }])
  ```
  יוצר מסמכים מרובים בקולקציה אחת בפעולה אחת.

---

### שליפת נתונים (Find)

1. **שליפת כל המסמכים בקולקציה**
   ```javascript
   db.collection_name.find()
   ```
   מציג את כל המסמכים בקולקציה.

2. **שליפת מסמכים עם קריטריונים (Filter)**
   ```javascript
   db.collection_name.find({ key: "value" })
   ```
   מציג את כל המסמכים התואמים לקריטריון.

3. **שליפת מסמך אחד בלבד**
   ```javascript
   db.collection_name.findOne({ key: "value" })
   ```

4. **מיון תוצאות**
   ```javascript
   db.collection_name.find().sort({ key: 1 }) # 1 לסדר עולה, -1 לסדר יורד
   ```

5. **הגבלת מספר התוצאות**
   ```javascript
   db.collection_name.find().limit(5)
   ```

---

### עדכון נתונים (Update)

1. **עדכון מסמך אחד**
   ```javascript
   db.collection_name.updateOne(
     { key: "value" },
     { $set: { key_to_update: "new_value" } }
   )
   ```

2. **עדכון מסמכים מרובים**
   ```javascript
   db.collection_name.updateMany(
     { key: "value" },
     { $set: { key_to_update: "new_value" } }
   )
   ```

3. **החלפה מוחלטת של מסמך**
   ```javascript
   db.collection_name.replaceOne(
     { key: "value" },
     { new_key1: "new_value1", new_key2: "new_value2" }
   )
   ```

---

### מחיקת נתונים (Delete)

1. **מחיקת מסמך אחד**
   ```javascript
   db.collection_name.deleteOne({ key: "value" })
   ```

2. **מחיקת מסמכים מרובים**
   ```javascript
   db.collection_name.deleteMany({ key: "value" })
   ```

3. **מחיקת כל המסמכים בקולקציה**
   ```javascript
   db.collection_name.deleteMany({})
   ```

---

### פקודות נוספות

1. **ספירת מסמכים בקולקציה**
   ```javascript
   db.collection_name.countDocuments({ key: "value" })
   ```

2. **אגרגציות (Aggregations)**
   ```javascript
   db.collection_name.aggregate([
     { $match: { key: "value" } },
     { $group: { _id: "$group_key", total: { $sum: "$amount" } } }
   ])
   ```

3. **מחיקת קולקציה**
   ```javascript
   db.collection_name.drop()
   ```

4. **מחיקת מסד נתונים**
   ```javascript
   db.dropDatabase()
   ```

---

### טיפים נוספים
- השתמש ב-`find().pretty()` כדי להציג את המסמכים בפורמט קריא יותר.
- השתמש במפעילים כמו `$gte`, `$lte`, ו-`$in` לביצוע חיפושים מורכבים.
