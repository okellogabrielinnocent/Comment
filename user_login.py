import subprocess as sp

def start():
    '''start menu for cmd and sp is call for subprocess'''
    tmp = sp.call('cls',shell=True)
    print('Please enter the option number you would like.')
    print('i.e. If I wanted to register, I would type 2')
    print('[1] User')
    print('[2] Register')
    print('[3] Moderator Controls')
    print('[4] Admin Controls')
    
    option = input('Option number: ') # Get human input
    if option == '1':
        login()
    elif option == '2':
        register()
    elif option == '3':
        moderator()
    elif option == '4':
        adminlogin()
    else:
        print('Option does not match the choices!')
        anykey = input('Press Enter to continue.')
        start()

def login():
    '''Get login info from user'''
    tmp = sp.call('cls',shell=True)
    print('Enter your login information.')
    name = input('Enter your username: ')
    password_ = input('Enter your password: ')
    logintest( name, password_ )
    
def register():
    '''Get registration info from user in cmd'''
    tmp = sp.call('cls',shell=True)
    print('Enter your username and password to login.')
    name_ = input('Enter your username: ')
    password__ = input('Enter your password: ')
    registerwrite( name_, password__ )

def registerwrite( username, password ):
    '''Write registration to file to file'''
    n = username+'.txt'
    f = open(n, 'w')
    f.write(username+'\n')
    f.write(password+'\n')
    f.write("Login sys made by User")
    f.close()

def logintest( username, password ):
    '''Check login from file '''
    n = username+'.txt'
    p = password
    try:
        file = open(n, 'r')
        file.close()
        worked = true
        
    except:
        print('File was not able to be opened. Does it exist?')
        yn = input('y/n: ')
        if yn == 'y':
            login()
        elif yn == 'n':
            start()
    
    if worked == true:
        f = open(n, 'r')
        _username_ = f.readline()
        _password_ = f.readline()
        if _password_ == password:
            loginpass( username, password )

def loginpass( un, pw ):
    # Get an user to start
    print('Please give the name of user to start.')
    print('User not registerd!')
    userinput = input('user Name:')
    userstart( userinput )


def moderator():
    '''Moderator login'''
    _username = input('Moderator Username: ')
    _pass = input('Moderator Password: ')
    _secrete_code = input('Secrete Code: ')
   
    if _username == 'moderator':
        if _pass == 'moderator123':
            if _secrete_code == '1234':
                moderator()
            else:
                print("Username is incorrect!")
        else:
            print('Password is incorrect!')
    else:
        print('Secrete Code is incorrect!')

def adminlogin():
    # Admin logij
    _username = input('Admin Username: ')
    _pass = input('Admin Password: ')
    _secrete_code = input('Secrete Code: ')
   
    if _username == 'admin':
        if _pass == 'admin123':
            if _secrete_code == '12345':
                admincontrol()
            else:
                print("Username is incorrect!")
        else:
            print('Password is incorrect!')
    else:
        print('Secrete Code is incorrect!')
            

def admincontrol():
    # Admin Control
    tmp = sp.call('cls',shell=True)
    print('Welcome to Admin Control!')    
    ai = input('Press enter to go back to the start screen.')
    if ai != 'Edit':
        start()
    else:
        start()
    
def comment_open(comment_open ):
    '''This starts an application which is in text'''
    f = open('okellogabriel.txt', 'r')
    for line in f:
        comment = [item.split('\n')[0] for item in comments]
        comment.append(line)
        f.close()
    for item in comment:
        if item == comment_open:
            print('Comment is deleted; cannot open! Contact your app administrator.')
            enter_to_continue = input('Press Enter to continue.')
            login()
        
start()
