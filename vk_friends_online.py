import vk


APP_ID = 5786100 


def get_user_login():
    return input('Input your user name: ')
    

def get_user_password():
    return input('Input your password: ')
   

def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friend_ids = api.friends.getOnline()
    return api.users.get(user_ids=friend_ids)


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    if password and login:
        friends_online = get_online_friends(login, password)
        output_friends_to_console(friends_online)
    else:
        print('Authentication failed')
