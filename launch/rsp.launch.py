from launch import LaunchDescription
from launch_ros.actions import Node
import os
from launch.substitutions import LaunchConfiguration ,Command
from launch.actions import DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    # Get the path to the URDF file
    urdf_file_name = 'my_robot.urdf.xacro'
    urdf_file_path = os.path.join(
        get_package_share_directory('my_bot'),
        'desc',
        urdf_file_name)

    robot_description_content = Command(['xacro ', urdf_file_path])


    # Create a dictionary to pass the robot_description parameter
    params = {'robot_description': robot_description_content, 'use_sim_time': use_sim_time}

    # Node for robot_state_publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[params]
    )
    # LaunchDescription defines the nodes to be launched
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),
        robot_state_publisher_node,
    ])
