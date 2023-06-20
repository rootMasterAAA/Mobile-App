from kivy.storage.jsonstore import JsonStore
store = JsonStore("user.json")
def checkUserLoginStatus():
    if store.get("user_state")["loginState"]:
        return True
    return False
