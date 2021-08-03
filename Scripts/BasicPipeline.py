import os
import subprocess

# EXECUTING ORBLSAM FROM TERMINAL
orb_slam2_video_command = "/home/noy/ORB_SLAM2/Examples/Monocular/mono_tum_save /home/noy/ORB_SLAM2/Vocabulary/ORBvoc.txt /home/noy/PycharmProjects/pilot/outputs/TUM1.yaml /home/noy/PycharmProjects/pilot/outputs/"
orb_slam2_camera_command = "/home/noy/ORB_SLAM2/Examples/Monocular/mono_tum_save_live /home/noy/ORB_SLAM2/Vocabulary/ORBvoc.txt /home/noy/PycharmProjects/pilot/outputs/TUM1.yaml"

# GNOME TERMINAL (separate process)
os.system("gnome-terminal -- " + orb_slam2_video_command)

# SUBPROCESS
# process = subprocess.Popen(orb_slam2_camera_command.split(), stdout=subprocess.PIPE)
# output, error = process.communicate()

print("END")