#!/usr/bin/env python
import time
import rospy
from math import pi, sin, cos, acos
import random
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
"""
Topics To Write on:
type: std_msgs/Float64
/tangs/waist_position_controller/command
"""

class TangsJointMover(object):

    def __init__(self):
        rospy.init_node('onejointmover_demo', anonymous=True)
        rospy.loginfo("Tangs OneJointMover Initialising...")
        
        self.pub_tangs_waist_joint_position = rospy.Publisher('/tangs/waist_position_controller/command',
                                                            Float64,
                                                            queue_size=1)
        
        joint_states_topic_name = "/tangs/joint_states"
        rospy.Subscriber(joint_states_topic_name, JointState, self.tangs_joints_callback)
        tangs_joints_data = None
        while tangs_joints_data is None:
            try:
                tangs_joints_data = rospy.wait_for_message(joint_states_topic_name, JointState, timeout=5)
            except:
                rospy.logwarn("Time out " + str(joint_states_topic_name))
                pass

        self.tangs_joint_dictionary = dict(zip(tangs_joints_data.name, tangs_joints_data.position))

    """
    def move_tangs_all_joints(self, roll, pitch, yaw):
        angle_roll = Float64()
        angle_roll.data = roll
        angle_pitch = Float64()
        angle_pitch.data = pitch
        angle_yaw = Float64()
        angle_yaw.data = yaw
        self.pub_mira_roll_joint_position.publish(angle_roll)
        self.pub_mira_pitch_joint_position.publish(angle_pitch)
        self.pub_mira_yaw_joint_position.publish(angle_yaw)
    """

    def move_tangs_waist_joint(self, position):
        """
        limits radians : lower="-1.57" upper="1.57"
        :param position:
        :return:
        """
        angle = Float64()
        angle.data = position
        self.pub_tangs_waist_joint_position.publish(angle)

    def tangs_joints_callback(self, msg):
        """
        sensor_msgs/JointState
        std_msgs/Header header
        uint32 seq
        time stamp
        string frame_id
        string[] name
        float64[] position
        float64[] velocity
        float64[] effort

        :param msg:
        :return:
        """
        self.tangs_joint_dictionary = dict(zip(msg.name, msg.position))

    def tangs_check_joint_value(self, joint_name, value, error=0.1):
        """
        Check the joint by name 'pitch_joint', 'roll_joint', 'yaw_joint' is near the value given
        :param value:
        :return:
        """
        similar = self.tangs_joint_dictionary.get(joint_name) >= (value - error ) and self.tangs_joint_dictionary.get(joint_name) <= (value + error )

        return similar

    def convert_angle_to_unitary(self, angle):
        """
        Removes complete revolutions from angle and converts to the positive equivalent
        if the angle is negative
        :param angle: Has to be in radians
        :return:
        """
        # Convert to angle between [0,360)
        complete_rev = 2 * pi
        mod_angle = int(angle / complete_rev)
        clean_angle = angle - mod_angle * complete_rev
        # Convert Negative angles to their corresponding positive values
        if clean_angle < 0:
            clean_angle += 2 * pi

        return clean_angle

    def assertAlmostEqualAngles(self, x, y,):
        c2 = (sin(x) - sin(y)) ** 2 + (cos(x) - cos(y)) ** 2
        angle_diff = acos((2.0 - c2) / 2.0)
        return angle_diff

    def tangs_check_continuous_joint_value(self, joint_name, value, error=0.1):
        """
        Check the joint by name 'pitch_joint', 'roll_joint', 'yaw_joint' is near the value given
        We have to convert the joint values removing whole revolutions and converting negative versions
        of the same angle
        :param value:
        :return:
        """
        joint_reading = self.tangs_joint_dictionary.get(joint_name)
        clean_joint_reading = self.convert_angle_to_unitary(angle=joint_reading)
        clean_value = self.convert_angle_to_unitary(angle=value)

        dif_angles = self.assertAlmostEqualAngles(clean_joint_reading, clean_value)
        similar = dif_angles <= error

        return similar

    def tangs_movement_sayno(self):
        """
        Make Mira say no with the head
        :return:
        """
        check_rate = 5.0
        position = 0.7


        rate = rospy.Rate(check_rate)
        for repetition in range(2):
            similar = False
            while not similar:
                self.move_tangs_waist_joint(position=position)
                # WARNING: THE COMMAND HAS TO BE PUBLISHED UNTIL THE GOAL IS REACHED
                # This is because, when publishing a topic, the first time doesn't always work.
                similar = self.tangs_check_continuous_joint_value(joint_name="waist_joint", value=position)

                rate.sleep()
            position *= -1

        


if __name__ == "__main__":

    # Supondo que TangsJointMover seja uma classe definida anteriormente
    tangs_bot = TangsJointMover()
    ang_min = -1.57
    ang_max = 1.57
    step = 0.1  # Incremento desejado

    angle = ang_min
    while angle <= ang_max:
        tangs_bot.move_tangs_waist_joint(angle)
        rospy.sleep(0.3)
        angle += step  # Incrementa o ângulo

