# Function List for LLM to call
import json

robot_functions_list_1 = [
    {
        "name": "publish_cmd_vel",
        "description": "Publish cmd_vel message to control the movement of turtlesim, including rotation and movement,only used for turtlesim,not for robotic arm",
        "parameters": {
            "type": "object",
            "properties": {
                "linear_x": {
                    "type": "number",
                    "description": "The linear velocity along the x-axis",
                },
                "linear_y": {
                    "type": "number",
                    "description": "The linear velocity along the y-axis",
                },
                "linear_z": {
                    "type": "number",
                    "description": "The linear velocity along the z-axis",
                },
                "angular_x": {
                    "type": "number",
                    "description": "The angular velocity around the x-axis",
                },
                "angular_y": {
                    "type": "number",
                    "description": "The angular velocity around the y-axis",
                },
                "angular_z": {
                    "type": "number",
                    "description": "The angular velocity around the z-axis",
                },
            },
            "required": [
                "linear_x",
                "linear_y",
                "linear_z",
                "angular_x",
                "angular_y",
                "angular_z",
            ],
        },
    },
    {
        "name": "reset_turtlesim",
        "description": "Resets the turtlesim to its initial state and clears the screen,only used for turtlesim,not for robotic arm",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "publish_target_pose",
        "description": "Publish target pose message to control the movement of arm robot, including x, y, z, roll, pitch, yaw. For example,[0.2, 0.2, 0.2, 0.2, 0.2, 0.2] is a valid target pose.",
        "parameters": {
            "type": "object",
            "properties": {
                "x": {
                    "type": "number",
                    "description": "The x position of the target pose",
                },
                "y": {
                    "type": "number",
                    "description": "The y position of the target pose",
                },
                "z": {
                    "type": "number",
                    "description": "The z position of the target pose",
                },
                "roll": {
                    "type": "number",
                    "description": "The roll of the target pose in radians",
                },
                "pitch": {
                    "type": "number",
                    "description": "The pitch of the target pose in radians",
                },
                "yaw": {
                    "type": "number",
                    "description": "The yaw of the target pose in radians",
                },
            },
            "required": [
                "x",
                "y",
                "z",
                "roll",
                "pitch",
                "yaw",
            ],
        },
    },
]

class TurtleRobot():
    def __init__(self):
        pass

    def function_call_callback(self, request, response):
        req = json.loads(request.request_text)
        function_name = req["name"]
        function_args = req["args"]
        func_obj = getattr(self, function_name)
        try:
            function_execution_result = func_obj(**function_args)
        except Exception as error:
            self.get_logger().info(f"Failed to call function: {error}")
            response.response_text = str(error)
        else:
            response.response_text = str(function_execution_result)
        return response

    def publish_cmd_vel(self, **kwargs):
        """
        Publishes cmd_vel message to control the movement of turtlesim
        """
        linear_x = kwargs.get("linear_x", 0.0)
        linear_y = kwargs.get("linear_y", 0.0)
        linear_z = kwargs.get("linear_z", 0.0)
        angular_x = kwargs.get("angular_x", 0.0)
        angular_y = kwargs.get("angular_y", 0.0)
        angular_z = kwargs.get("angular_z", 0.0)

        print(f"COMMAND: publish_cmd_vel: {linear_x}, {linear_y}, {linear_z}, {angular_x}, {angular_y}, {angular_z}")
        

    def reset_turtlesim(self, **kwargs):
        """
        Resets the turtlesim to its initial state and clears the screen
        """
        print(f"COMMAND: reset_turtlesim")

    def publish_target_pose(self, **kwargs):

        x = kwargs.get("x", 0.0)
        y = kwargs.get("y", 0.0)
        z = kwargs.get("z", 0.0)
        roll = kwargs.get("roll", 0.0)
        pitch = kwargs.get("pitch", 0.0)
        yaw = kwargs.get("yaw", 0.0)

        print(f"COMMAND: publish_target_pose: {x}, {y}, {z}, {roll}, {pitch}, {yaw}")