from pymongo import MongoClient


# פונקציה המתחברת למסד נתונים
def get_database():
    # URI לחיבור ל-MongoDB
    mongo_uri = "mongodb://localhost:27017"

    # יצירת לקוח MongoDB
    client = MongoClient(mongo_uri)

    # החזרת מסד הנתונים (ניתן לשנות את שם המסד בהתאם לפרויקט שלך)
    return client['transaction_db']


