def appendJSON(JSONname, update_data):
    with open(JSONname, "r+") as f:
        import json
        import os
        loaded = json.load(f)
        loaded.update(update_data)
        f.seek(0)
        json.dump(loaded, f)


def searchJSON(JSONname):
    import json
    import os
    try:
        with open(JSONname, "r") as jsonfile:
            data = json.load(jsonfile)
            return True
    except:
        return False


'''
def createJSON():

def deleteJSON():

def printJSON():

def overwriteJSON():
'''
