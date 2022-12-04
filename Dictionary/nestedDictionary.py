myDictionary = {
    "class":{
        "student":{
            "name" : "Onkar",
            "marks" : {
                "python" : 90,
                "web": {
                    "practical": 65,
                    "theory": 30
                }
            }
        }
    }
}
print(myDictionary["class"]["student"]["marks"]["web"]["practical"])