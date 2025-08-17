from utils.Load__Json import Loading_Json_file


class complete_API_URL :


    @staticmethod
    def Post_URL():
        return Loading_Json_file.function() + "/public/v2/users"

    @staticmethod
    def Put_User(ID):
        return Loading_Json_file.function() + f"/public/v2/users/{ID}"


    @staticmethod
    def Get_URL(id):
        return Loading_Json_file.function() + f"/public/v2/users/{id}"


    @staticmethod
    def delete_user(ids):
        return Loading_Json_file.function() + f"/public/v2/users/{ids}"

