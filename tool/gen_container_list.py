#!/usr/bin/env python

import yaml

def gen_container_list(fp="docker-compose.yml", Loader=yaml.SafeLoader):
    with open(fp) as file:
        compose_yml = yaml.load(file, Loader)

    L = set()
    for i in compose_yml["services"]:
        for j in compose_yml["services"][i]:
            L.add(compose_yml["services"][i]["container_name"])
    return L

def get_container_list(container_list, fp="./tool/container_list"):
    with open(fp, mode='w') as file:
        file.write("google.com\n")
        for i in container_list:
            file.write(i + "\n")

def main():
    get_container_list([i for i in gen_container_list()])

if __name__ == "__main__":
    main()
