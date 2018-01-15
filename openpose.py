from ctypes import cdll

openpose_dll = cdll.LoadLibrary("OpenPoseDemo.dll")
openpose_dll.openPoseDemo()
