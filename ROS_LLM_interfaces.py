class Request():

    """Emulates the ROS-LLM request object"""
    request_text = ""

    def __init__(self, request_text):
        self.request_text = request_text

class Response():

    """Emulates the ROS-LLM response object"""
    response_text = ""

    def __init__(self, response_text):
        self.response_text = response_text
