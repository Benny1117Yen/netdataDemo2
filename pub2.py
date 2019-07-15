#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
""" 
Publish some messages to queue
"""
import paho.mqtt.publish as publish
import requests
import json
import time


url = 'http://localhost:19999/api/v1/allmetrics?format=json'


def uc():
    user_cpu_usage = used0 / sum1
    return user_cpu_usage

def syc():
    system_cpu_usage = used4 / sum1
    return system_cpu_usage

def soc():
    softirq_cpu_usage = used5 / sum1
    return softirq_cpu_usage

def r():
    ram_usage = used1 / sum2 * 100
    return ram_usage

def d():
    disk_home_usage = used2 / sum3 * 100
    return disk_home_usage

def refresh_data():
    data0 =requests.get(url)
    data = data0.json()
    cpu = data["system.cpu"]
    used0 = cpu['dimensions']['user']['value']
    used4 = cpu['dimensions']['system']['value']
    used5 = cpu['dimensions']['softirq']['value']
    sum1 = 1
    ram = data["system.ram"]
    used1 = ram['dimensions']['used']['value']
    sum2 = sum(f['value'] for f in ram['dimensions'].values() if f)
    disk = data['disk_space._']
    used2 = disk['dimensions']['used']['value']
    sum3 = sum(g['value'] for g in disk['dimensions'].values() if g)
    msgs = [{'topic': "USER CPU used", 'payload': uc()},
            {'topic': "SYSTEM CPU used", 'payload': syc()},
            {'topic': "SOFTIRQ CPU used", 'payload': soc()},
            {'topic': "RAM used", 'payload': r()},
            {'topic': "HOME DISK used", 'payload': d()}]
    return data0, data, used0, used4, cpu, used5, sum1, ram, used1, sum2, disk, used2, sum3, msgs


host = "localhost"


if __name__ == '__main__':
    while True:
        data0 = requests.get(url)
        data = data0.json()
        cpu = data["system.cpu"]
        used0 = cpu['dimensions']['user']['value']
        used4 = cpu['dimensions']['system']['value']
        used5 = cpu['dimensions']['softirq']['value']
        sum1 = 1
        ram = data["system.ram"]
        used1 = ram['dimensions']['used']['value']
        sum2 = sum(f['value'] for f in ram['dimensions'].values() if f)
        disk = data['disk_space._']
        used2 = disk['dimensions']['used']['value']
        sum3 = sum(g['value'] for g in disk['dimensions'].values() if g)
        msgs = [{'topic': "USER CPU used", 'payload': uc()},
                {'topic': "SYSTEM CPU used", 'payload': syc()},
                {'topic': "SOFTIRQ CPU used", 'payload': soc()},
                {'topic': "RAM used", 'payload': r()},
                {'topic': "HOME DISK used", 'payload': d()}]
        publish.single(topic="Items", payload="percentage(%)", hostname=host)
        publish.multiple(msgs, hostname=host)
        data = refresh_data()
        time.sleep(1)
