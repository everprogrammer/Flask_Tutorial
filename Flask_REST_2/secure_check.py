from user import User

users = [ User(1, 'Amir', 'mypass'), User(2, 'Sina', 'secret') ]

username_table = {u.username: u for u in users}
# print(username_table['Amir'])
userid_table = {u.id: u for u in users} 

def authenticate(username, password):
    # check if the user exists
    # if so, return user

    user = username_table.get(username)
    if user and password == user.password:
        return user 
    
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
