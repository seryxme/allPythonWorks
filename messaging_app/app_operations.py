import pathlib
import json

app_data = pathlib.Path("./json/app_users.json").resolve()
app_data.parent.mkdir(parents=True, exist_ok=True)
all_users = []
user_size = 0
user_list = []


def load_user_db():
    if data_reader() is not None:
        global all_users
        all_users = data_reader()

        global user_list
        user_list = [dict_['username'] for dict_ in all_users]

        global user_size
        user_size = len(user_list)


def data_store(init_data):
    all_users.append(init_data)
    with app_data.open(mode="w", encoding="utf-8") as user_data:
        json.dump(all_users, user_data, indent=4)


def data_reader() -> list:
    with app_data.open(mode="r", encoding="utf-8") as user_data:
        data = json.load(user_data)

    return data


def reg_processor(user_reg_data):
    field_list = ['name', 'username', 'password']

    init_data = {field_list[i]: user_reg_data[i] for i in range(len(field_list))}
    data_store(init_data)


def msg_data(box_type):
    msg_ids = [0]
    msg_fields = []

    if box_type == 'inbox':
        msg_fields = ['title', 'sender', 'message']
    else:
        msg_fields = ['title', 'receiver', 'message']

    msg_details = [None, None, None]

    init_in_msg_data = [{msg_fields[i]: msg_details[i] for i in range(len(msg_fields))}]
    msg_data_main = {msg_ids[i]: init_in_msg_data[i] for i in range(len(msg_ids))}

    return msg_data_main


def user_data_store(username):
    user_data = pathlib.Path(f"./json/{username}.json").resolve()
    user_data.touch(exist_ok=True)

    main_msg_fields = ['inbox', 'outbox', 'drafts']
    main_msg_data = []

    main_msg_data.append(msg_data('inbox'))
    main_msg_data.append(msg_data('outbox'))
    main_msg_data.append(msg_data('drafts'))

    all_msg_data = [{main_msg_fields[i]: main_msg_data[i] for i in range(len(main_msg_fields))}]

    with user_data.open(mode="w", encoding="utf-8") as user_data:
        json.dump(all_msg_data, user_data, indent=4)


def register():
    user_reg_data = []
    name = input("Enter your full name: ")
    user_reg_data.append(name)
    username = input("Enter your username: ")
    if user_list.__contains__(username):
        print("Username unavailable. Try again.")
        register()
    user_reg_data.append(username)
    password = input("Enter your password: ")
    user_reg_data.append(password)

    user_list.append(username)
    size = user_size + 1
    reg_processor(user_reg_data)

    user_data_store(username)

    app_home()


def user_check(username) -> bool:
    for user in user_list:
        if user == username:
            return True
    return False


def pw_check(username, password) -> bool:
    data = data_reader()

    for dict_ in data:
        if dict_.get('username') == username:
            if dict_.get('password') == password:
                return True
    return False


def login():
    username = input("Enter your username: ")

    if user_check(username):
        password = input("Enter your password: ")
        if pw_check(username, password):
            app_menu(username)
        else:
            print("Wrong password. Please try again")
            login()
    else:
        print("Wrong username or user not yet registered.")
        app_home()


def message_store(box, username, title, sender, message):
    data = message_reader(username)
    new_id = [len(data[0][box])]
    user_msg_fields = ['title', 'sender', 'message']
    if box is not 'inbox':
        user_msg_fields = ['title', 'receiver', 'message']
    new_msg = [title, sender, message]

    new_msg_data = [{user_msg_fields[i]: new_msg[i] for i in range(len(user_msg_fields))}]
    msg_data = {new_id[i]: new_msg_data[i] for i in range(len(new_id))}

    message_data = pathlib.Path(f"./json/{username}.json")

    data[0][box].update(msg_data)
    with message_data.open(mode="w", encoding="utf-8") as messages:
        json.dump(data, messages, indent=4)


def message_reader(username) -> list:
    message_data = pathlib.Path(f"./json/{username}.json")
    with message_data.open(mode="r", encoding="utf-8") as messages:
        data = json.load(messages)

    return data


def inbox(username):
    data = message_reader(username)
    sn = 0
    for message in data[0]['inbox']:
        if message[f'{sn}']['sender'] is not None:
            print(f"""
            {sn}.
            Title: {message[f'{sn}']['title']}
            Sender: {message[f'{sn}']['sender']}
            Message:
            {message[f'{sn}']['message']}
            """)
        sn += 1

    option = int(input(f"""
                1. Reply
                2. Delete
                3. Back
                """))
    match option:
        case 1:
            msg_num = int(input("Select the message number to reply: "))
            for message in data[0]:
                if message is message[f'{msg_num}']:
                    write(username, reply=f"Re: {message[f'{msg_num}']['title']}")
        case 2:
            delete(username)
            app_menu(username)
        case 3:
            app_menu(username)
        case other:
            print("Invalid selection.")
            inbox(username)


def outbox(username):
    data = message_reader(username)
    sn = 0
    for message in data[0]['outbox']:
        if message[f'{sn}']['message'] is not None:
            print(f"""
            {sn}.
            Title: {message[f'{sn}']['title']}
            To: {message[f'{sn}']['receiver']}
            Message:
            {message[f'{sn}']['message']}
            """)
        sn += 1


def recipient_check() -> str:
    receiver = input("Enter recipient username: ")
    if not user_list.__contains__(receiver):
        print("No such user. Please try again.")
        recipient_check()

    return receiver


def write(username, reply=None):
    title = input("Enter your title: \n")
    if reply is not None:
        title = reply
    message = input("Enter your message: \n")
    receiver = recipient_check()
    option = int(input(f"""
            1. Send
            2. Save Draft
            3. Cancel
            """))
    match option:
        case 1:
            message_store('inbox', receiver, title, username, message)
            message_store('outbox', username, title, receiver, message)
            app_menu(username)
        case 2:
            message_store('drafts', username, title, receiver, message)
            app_menu(username)
        case 3:
            app_menu(username)
        case other:
            print("Invalid selection.")
            write(username)


def delete(username, box):
    data = message_reader(username)

    msg_num = int(input("Select the message number to delete: "))
    for message in data[0][box]:
        if message is message[f'{msg_num}']:
            data[0][box].pop(msg_num - 1)
            for key in data[0][box]:
                key = f'{msg_num-1}'

def drafts(username):
    data = message_reader(username)
    sn = 0
    for message in data[0]['drafts']:
        if message[f'{sn}']['message'] is not None:
            print(f"""
                {sn}.
                Title: {message[f'{sn}']['title']}
                To: {message[f'{sn}']['receiver']}
                Message:
                {message[f'{sn}']['message']}
                """)
        sn += 1


def app_menu(username):
    option = int(input(f"""
        Welcome {username}!
        1. Inbox
        2. Write
        3. Sent Messages
        4. Drafts
        5. Delete Message
        6. Logout
        """))
    match option:
        case 1:
            inbox(username)
            response = input()
            app_menu(username)
        case 2:
            write(username)
        case 3:
            outbox(username)
            response = input()
            app_menu(username)
        case 4:
            drafts(username)
            response = input()
            app_menu(username)
        case 5:
            delete(username)
            response = input()
            app_menu(username)
        case 6:
            app_home()
        case other:
            print("Invalid selection.")
            app_menu(username)


def app_home():
    option = int(input("""
    Welcome to Simple Messaging!
    1. Register
    2. Login
    3. Exit
    """))
    match option:
        case 1:
            register()
        case 2:
            load_user_db()
            login()
        case 3:
            quit()
        case other:
            print("Please select 1 or 2.")
            app_home()
