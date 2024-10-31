# Function List for LLM to call

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
        "description": "Publish target pose message to control the movement of arm robot, including x, y, z, roll, pitch, yaw",
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
                    "description": "The roll of the target pose",
                },
                "pitch": {
                    "type": "number",
                    "description": "The pitch of the target pose",
                },
                "yaw": {
                    "type": "number",
                    "description": "The yaw of the target pose",
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

