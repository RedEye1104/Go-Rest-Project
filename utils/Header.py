

class Hearders():  # Created a class
    @staticmethod  # Add method so that you don't need to use self
    def GET_Header():  # Creating a function.
        header = {
            "Authorization": "Bearer d3f3e0ac65d8e05b88f76c76a7884eaac720b285f9b3979d54012e7730fdbb96",
            "Content-Type": "application/json"}  # This is header.
        return header