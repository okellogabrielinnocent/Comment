import pickle


class Storage:
    @staticmethod
    def load_users():
        try:
            with open('pickles_users.pickle', 'rb+') as handle:
                comment = pickle.load(handle)
        except FileNotFoundError:
            try:
                with open('pickles_users.pickle', 'w+') as handle:
                    comment = pickle.load(handle)
            except Exception as ep:
                return ep
        return comment

    @staticmethod
    def save_users(data):
        try:
            with open('pickles_users.pickle', 'wb+') as handle:
                pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as ex:
            return ex
        return True

    @staticmethod
    def load_comments():
        try:
            with open('pickles_comments.pickle', 'rb+') as handle:
                comment = pickle.load(handle)
        except FileNotFoundError:
            try:
                with open('pickles_comments.pickle', 'wb') as handle:
                    comment = pickle.load(handle)
            except Exception as ep:
                return ep
        return comment

    @staticmethod
    def save_comments(data):
        try:
            with open('pickles_comments.pickle', 'wb+') as handle:
                pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as ex:
            return ex
        return True

    @staticmethod
    def load_responses():
        try:
            with open('pickles_responses.pickle', 'rb+') as handle:
                comment = pickle.load(handle)
        except FileNotFoundError:
            try:
                with open('pickles_responses.pickle', 'wb') as handle:
                    comment = pickle.load(handle)
            except Exception as ep:
                return ep
        return comment

    @staticmethod
    def save_responses(data):
        try:
            with open('pickles_responses.pickle', 'wb+') as handle:
                pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as ex:
            return ex
        return True

    @staticmethod
    def load_logs():
        try:
            with open('pickles_logs.pickle', 'rb+') as handle:
                comment = pickle.load(handle)
        except Exception as ex:
            try:
                with open('pickles_logs.pickle', 'wb') as handle:
                    comment = pickle.load(handle)
            except Exception as ep:
                return ep
        return comment

    @staticmethod
    def save_logs(data):
        try:
            with open('pickles_logs.pickle', 'wb+') as handle:
                pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as ex:
            return ex
        return True
