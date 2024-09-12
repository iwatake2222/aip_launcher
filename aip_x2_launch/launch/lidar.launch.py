from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import GroupAction
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import EnvironmentVariable
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import PushRosNamespace
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument("launch_driver", default_value="true"),
        DeclareLaunchArgument("use_concat_filter", default_value="true"),
        DeclareLaunchArgument(
            "vehicle_id",
            default_value=EnvironmentVariable("VEHICLE_ID", default_value="default")
        ),
        DeclareLaunchArgument("vehicle_mirror_param_file"),
        DeclareLaunchArgument(
            "use_pointcloud_container",
            default_value="false",
            description="launch pointcloud container"
        ),
        DeclareLaunchArgument("pointcloud_container_name", default_value="pointcloud_container"),
        DeclareLaunchArgument(
            "dual_return_filter_param_file",
            default_value=[
                FindPackageShare("aip_x2_launch"),
                "/config/dual_return_filter.param.yaml"
            ]
        ),
        DeclareLaunchArgument("enable_blockage_diag", default_value="true"),


        GroupAction([
            PushRosNamespace("lidar"),

            GroupAction([
                PushRosNamespace("front_lower"),
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(
                        [
                            FindPackageShare("aip_x2_launch"),
                            "/launch/pandar_node_container.launch.py"
                        ]
                    ),
                    launch_arguments={
                        "model": "Pandar40P",
                        "frame_id": "pandar_40p_front",
                        "device_ip": "192.168.110.201",
                        "lidar_port": "2321",
                        "gps_port": "10121",
                        "scan_phase": "270.0",
                        "angle_range": "[90.0, 270.0]",
                        "distance_range": "[0.5, 200.0]",
                        "blockage_range": "[90.0, 270.0]",
                        "vertical_bins": "40",
                        "horizontal_ring_id": "12",
                        "return_mode": "Dual",
                        "min_azimuth_deg": "135.0",
                        "max_azimuth_deg": "225.0",
                        "is_channel_order_top2down": "true",
                        "horizontal_resolution": "0.4",
                        "enable_blockage_diag": LaunchConfiguration("enable_blockage_diag"),
                        "calibration": [
                            FindPackageShare("individual_params"),
                            "/config/",
                            LaunchConfiguration("vehicle_id"),
                            "/aip_x2/pandar/front_lower.csv"
                        ],
                        "launch_driver": LaunchConfiguration("launch_driver"),
                        "dual_return_filter_param_file": LaunchConfiguration(
                            "dual_return_filter_param_file"
                        ),
                        "vehicle_mirror_param_file": LaunchConfiguration(
                            "vehicle_mirror_param_file"
                        )
                    }.items()
                ),
            ]),

            GroupAction([
                PushRosNamespace("front_upper"),
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(
                        [
                            FindPackageShare("aip_x2_launch"),
                            "/launch/pandar_node_container.launch.py"
                        ]
                    ),
                    launch_arguments={
                        "model": "PandarQT",
                        "frame_id": "pandar_qt_front",
                        "device_ip": "192.168.120.211",
                        "lidar_port": "2331",
                        "gps_port": "10131",
                        "scan_phase": "270.0",
                        "angle_range": "[90.0, 270.0]",
                        "blockage_range": "[90.0, 270.0]",
                        # for j6#1#2
                        # "scan_phase": "300.0",
                        # "angle_range": "[120.0, 300.0]",
                        # "blockage_range": "[120.0, 300.0]",
                        "distance_range": "[0.1, 20.0]",
                        "vertical_bins": "64",
                        "horizontal_ring_id": "40",
                        "return_mode": "First",
                        "is_channel_order_top2down": "false",
                        "horizontal_resolution": "0.6",
                        "enable_blockage_diag": LaunchConfiguration("enable_blockage_diag"),
                        "calibration": [
                            FindPackageShare("individual_params"),
                            "/config/",
                            LaunchConfiguration("vehicle_id"),
                            "/aip_x2/pandar/front_upper.csv"
                        ],
                        "launch_driver": LaunchConfiguration("launch_driver"),
                        "dual_return_filter_param_file": LaunchConfiguration(
                            "dual_return_filter_param_file"
                        ),
                        "vehicle_mirror_param_file": LaunchConfiguration(
                            "vehicle_mirror_param_file"
                        )
                    }.items()
                ),
            ]),

            GroupAction([
                PushRosNamespace("left_upper"),
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(
                        [
                            FindPackageShare("aip_x2_launch"),
                            "/launch/pandar_node_container.launch.py"
                        ]
                    ),
                    launch_arguments={
                        "model": "Pandar40P",
                        "frame_id": "pandar_40p_left",
                        "device_ip": "192.168.110.202",
                        "lidar_port": "2322",
                        "gps_port": "10122",
                        "scan_phase": "305.0",
                        "angle_range": "[90.0, 305.0]",
                        "distance_range": "[0.5, 200.0]",
                        "blockage_range": "[90.0, 305.0]",
                        "vertical_bins": "40",
                        "horizontal_ring_id": "12",
                        "min_azimuth_deg": "225.0",
                        "max_azimuth_deg": "315.0",
                        "is_channel_order_top2down": "true",
                        "horizontal_resolution": "0.4",
                        "enable_blockage_diag": LaunchConfiguration("enable_blockage_diag"),
                        "return_mode": "Dual",
                        "calibration": [
                            FindPackageShare("individual_params"),
                            "/config/",
                            LaunchConfiguration("vehicle_id"),
                            "/aip_x2/pandar/left_upper.csv"
                        ],
                        "launch_driver": LaunchConfiguration("launch_driver"),
                        "dual_return_filter_param_file": LaunchConfiguration(
                            "dual_return_filter_param_file"
                        ),
                        "vehicle_mirror_param_file": LaunchConfiguration(
                            "vehicle_mirror_param_file"
                        )
                    }.items()
                ),
            ]),

            GroupAction([
                PushRosNamespace("left_lower"),
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(
                        [
                            FindPackageShare("aip_x2_launch"),
                            "/launch/pandar_node_container.launch.py"
                        ]
                    ),
                    launch_arguments={
                        "model": "PandarQT",
                        "frame_id": "pandar_qt_left",
                        "device_ip": "192.168.120.212",
                        "lidar_port": "2332",
                        "gps_port": "10132",
                        "scan_phase": "270.0",
                        "angle_range": "[90.0, 270.0]",
                        "distance_range": "[0.1, 20.0]",
                        "blockage_range": "[120.0, 240.0]",
                        "vertical_bins": "64",
                        "horizontal_ring_id": "24",
                        "is_channel_order_top2down": "false",
                        "horizontal_resolution": "0.6",
                        "enable_blockage_diag": LaunchConfiguration("enable_blockage_diag"),
                        "return_mode": "First",
                        "calibration": [
                            FindPackageShare("individual_params"),
                            "/config/",
                            LaunchConfiguration("vehicle_id"),
                            "/aip_x2/pandar/left_lower.csv"
                        ],
                        "launch_driver": LaunchConfiguration("launch_driver"),
                        "dual_return_filter_param_file": LaunchConfiguration(
                            "dual_return_filter_param_file"
                        ),
                        "vehicle_mirror_param_file": LaunchConfiguration(
                            "vehicle_mirror_param_file"
                        )
                    }.items()
                ),
            ]),

            GroupAction([
                PushRosNamespace("right_upper"),
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(
                        [
                            FindPackageShare("aip_x2_launch"),
                            "/launch/pandar_node_container.launch.py"
                        ]
                    ),
                    launch_arguments={
                        "model": "Pandar40P",
                        "frame_id": "pandar_40p_right",
                        "device_ip": "192.168.120.203",
                        "lidar_port": "2323",
                        "gps_port": "10123",
                        "scan_phase": "270.0",
                        "angle_range": "[55.0, 270.0]",
                        "distance_range": "[0.5, 200.0]",
                        "blockage_range": "[55.0, 270.0]",
                        "vertical_bins": "40",
                        "horizontal_ring_id": "12",
                        "min_azimuth_deg": "45.0",
                        "max_azimuth_deg": "135.0",
                        "is_channel_order_top2down": "true",
                        "horizontal_resolution": "0.4",
                        "enable_blockage_diag": LaunchConfiguration("enable_blockage_diag"),
                        "return_mode": "Strongest",
                        "calibration": [
                            FindPackageShare("individual_params"),
                            "/config/",
                            LaunchConfiguration("vehicle_id"),
                            "/aip_x2/pandar/right_upper.csv"
                        ],
                        "launch_driver": LaunchConfiguration("launch_driver"),
                        "dual_return_filter_param_file": LaunchConfiguration(
                            "dual_return_filter_param_file"
                        ),
                        "vehicle_mirror_param_file": LaunchConfiguration(
                            "vehicle_mirror_param_file"
                        )
                    }.items()
                ),
            ]),

            GroupAction([
                PushRosNamespace("right_lower"),
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(
                        [
                            FindPackageShare("aip_x2_launch"),
                            "/launch/pandar_node_container.launch.py"
                        ]
                    ),
                    launch_arguments={
                        "model": "PandarQT",
                        "frame_id": "pandar_qt_right",
                        "device_ip": "192.168.120.213",
                        "lidar_port": "2333",
                        "gps_port": "10133",
                        "scan_phase": "270.0",
                        "angle_range": "[90.0, 270.0]",
                        "distance_range": "[0.1, 20.0]",
                        "blockage_range": "[150.0, 240.0]",
                        "vertical_bins": "64",
                        "horizontal_ring_id": "24",
                        "is_channel_order_top2down": "false",
                        "horizontal_resolution": "0.6",
                        "enable_blockage_diag": LaunchConfiguration("enable_blockage_diag"),
                        "return_mode": "First",
                        "calibration": [
                            FindPackageShare("individual_params"),
                            "/config/",
                            LaunchConfiguration("vehicle_id"),
                            "/aip_x2/pandar/right_lower.csv"
                        ],
                        "launch_driver": LaunchConfiguration("launch_driver"),
                        "dual_return_filter_param_file": LaunchConfiguration(
                            "dual_return_filter_param_file"
                        ),
                        "vehicle_mirror_param_file": LaunchConfiguration(
                            "vehicle_mirror_param_file"
                        )
                    }.items()
                ),
            ]),

            GroupAction([
                PushRosNamespace("rear_lower"),
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(
                        [
                            FindPackageShare("aip_x2_launch"),
                            "/launch/pandar_node_container.launch.py"
                        ]
                    ),
                    launch_arguments={
                        "model": "Pandar40P",
                        "frame_id": "pandar_40p_rear",
                        "device_ip": "192.168.110.204",
                        "lidar_port": "2324",
                        "gps_port": "10124",
                        "scan_phase": "180.0",
                        "angle_range": "[90.0, 270.0]",
                        "distance_range": "[0.5, 200.0]",
                        "blockage_range": "[90.0, 270.0]",
                        "vertical_bins": "40",
                        "horizontal_ring_id": "12",
                        "min_azimuth_deg": "135.0",
                        "max_azimuth_deg": "225.0",
                        "is_channel_order_top2down": "true",
                        "horizontal_resolution": "0.4",
                        "enable_blockage_diag": LaunchConfiguration("enable_blockage_diag"),
                        "return_mode": "Strongest",
                        "calibration": [
                            FindPackageShare("individual_params"),
                            "/config/",
                            LaunchConfiguration("vehicle_id"),
                            "/aip_x2/pandar/rear_lower.csv"
                        ],
                        "launch_driver": LaunchConfiguration("launch_driver"),
                        "dual_return_filter_param_file": LaunchConfiguration(
                            "dual_return_filter_param_file"
                        ),
                        "vehicle_mirror_param_file": LaunchConfiguration(
                            "vehicle_mirror_param_file"
                        )
                    }.items()
                ),
            ]),

            GroupAction([
                PushRosNamespace("rear_upper"),
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(
                        [
                            FindPackageShare("aip_x2_launch"),
                            "/launch/pandar_node_container.launch.py"
                        ]
                    ),
                    launch_arguments={
                        "model": "PandarQT",
                        "frame_id": "pandar_qt_rear",
                        "device_ip": "192.168.120.214",
                        "lidar_port": "2334",
                        "gps_port": "10134",
                        "scan_phase": "180.0",
                        "angle_range": "[90.0, 270.0]",
                        "blockage_range": "[90.0, 270.0]",
                        # for j6#1#2
                        # "scan_phase": "200.0",
                        # "angle_range": "[110.0, 290.0]",
                        # "blockage_range": "[110.0, 290.0]",
                        "distance_range": "[0.1, 20.0]",
                        "vertical_bins": "64",
                        "horizontal_ring_id": "40",
                        "is_channel_order_top2down": "false",
                        "horizontal_resolution": "0.6",
                        "enable_blockage_diag": LaunchConfiguration("enable_blockage_diag"),
                        "return_mode": "First",
                        "calibration": [
                            FindPackageShare("individual_params"),
                            "/config/",
                            LaunchConfiguration("vehicle_id"),
                            "/aip_x2/pandar/rear_upper.csv"
                        ],
                        "launch_driver": LaunchConfiguration("launch_driver"),
                        "dual_return_filter_param_file": LaunchConfiguration(
                            "dual_return_filter_param_file"
                        ),
                        "vehicle_mirror_param_file": LaunchConfiguration(
                            "vehicle_mirror_param_file"
                        )
                    }.items()
                ),
            ]),

            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    [
                        FindPackageShare("aip_x2_launch"),
                        "/launch/pointcloud_preprocessor.launch.py"
                    ]
                ),
                launch_arguments={
                    "base_frame": "base_link",
                    "use_intra_process": "true",
                    "use_multithread": "true",
                    "use_pointcloud_container": LaunchConfiguration("use_pointcloud_container"),
                    "container_name": LaunchConfiguration("pointcloud_container_name")
                }.items()
            ),

        ])
    ])
