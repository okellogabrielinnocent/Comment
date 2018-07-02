import pickle


def load_users():
    with open('users.pickle', 'rb') as handle:
        users = pickle.load(handle)
    if users:
        return users
    return False


def save_users(data):
    with open('pickles/users.pickle', 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_comments():
    with open('pickles/comments.pickle', 'rb') as handle:
        comment = pickle.load(handle)
    if comment:
        return comment
    return False


def save_comments(data):
    with open('pickles/comments.pickle', 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_responses():
    with open('pickles/responses.pickle', 'rb') as handle:
        comment = pickle.load(handle)
    if comment:
        return comment
    return False


def save_responses(data):
    with open('pickles/responses.pickle', 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_logs():
    with open('pickles/logs.pickle', 'rb') as handle:
        comment = pickle.load(handle)
    if comment:
        return comment
    return False


def save_logs(data):
    with open('pickles/logs.pickle', 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)