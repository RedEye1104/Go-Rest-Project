import json



class Loading_Json_file:
    @staticmethod
    def function():
        with open("D:\\GoRest_project\\Config\\URL_Points.json") as json_file:
            data = json.load(json_file)
            read_file =data ["environment"]["env"]
            return data[read_file]["base_URL"]
