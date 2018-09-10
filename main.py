#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import re
import sys

host_file = '/etc/hosts'
hosts = ["baidu.com", "v2ex.com"]
CONTROL_LINE = "#self_controlled"

def write_to_hosts(host_map):
    initted = False
    with open(host_file, "a+") as f:
        for host in hosts:
            if host_map.get(host) == None:
                if initted == False:
                    f.write(CONTROL_LINE + "\n")
                    initted = True
                host += '\n'
                f.write("0.0.0.0 " + host)
                f.write(":: " + host)
                f.write("0.0.0.0 www." + host)
                f.write(":: www." + host)
            else:
                print("\n host %s exists, skip" % host)
        if initted == True:
            f.write(CONTROL_LINE + "\n")


def delete_hosts():
    with open(host_file, "r") as f:
        content = f.readlines()
    contents = [x.strip().split("\t") for x in content]

    skip = True
    remove_list = []
    for x in contents:
        content = x[0]
        if content == CONTROL_LINE:
            skip = ~skip;
        elif skip == True:
            continue
        else:
            print("---------\n")
            print(x)
            remove_list.append(x)
            print("---------\n")
    for x in remove_list:
        contents.remove(x)
    print(contents)

def parse_hosts():
    with open(host_file, "r") as f:
        content = f.readlines()
    contents = [x.strip().split("\t") for x in content]

    skip = True
    host_map = {}
    for x in contents:
        content = x[0]
        if content == CONTROL_LINE:
            skip = ~skip;
        elif skip == True:
            continue
        else:
            content_map = content.strip().split(" ")
            print(content_map)
            host_map[content_map[1]] = content_map[0]
    print(host_map)
    return host_map

def main():
    if len(sys.argv) != 2:
         print("请在 python3 后加上 你要控制的时间\n")
         exit()
    time = sys.argv[1]
    host_map = parse_hosts()
    write_to_hosts(host_map)
    delete_hosts()

if __name__ == "__main__":
    main()
