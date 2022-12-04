#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from gpiozero import CPUTemperature


def getInfo():
    try:
        cpu = CPUTemperature()
        return cpu.temperature

    except Exception as ex:
        rospy.logerr(ex)
    finally:
        return cpu.temperature


def run():
    dados = String
    rate = rospy.Rate(1)
    pub = rospy.Publisher('/cpu_temp', String, queue_size=10)
    rospy.loginfo("sensor temperatura da cpu. iniciado com sucesso.")

    while not rospy.is_shutdown():
        dados = str(getInfo())
        pub.publish(dados)
        rate.sleep()


if __name__ == '__main__':
    rospy.init_node("SystemInfo")
    rospy.loginfo("Iniciando node sensor temperatura da cpu.")
    run()
