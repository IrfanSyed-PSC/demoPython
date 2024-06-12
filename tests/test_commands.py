import logging
from core.utils.docker_cmd import DockerManager

docker = DockerManager()

def test_docker_list_containers():
    
    logging.info("Testing DockerManager.list_containers")
    containers = docker.list_containers()
    logging.info(containers)
    assert containers is not None


def test_docker_list_images():
    logging.info("Testing DockerManager.list_images")
    logging.debug(docker.list_images())


    docker_list = docker.list_images()
    logging.debug(docker_list)

    assert len(docker_list) > 0

    ## for loop to print the list of images
    for image in docker_list:
        logging.info(image)

## This test might fail if you don't have the image locally
def test_docker_list_image():
    logging.info("Testing DockerManager.list_image")
    #assert len(docker.list_image('influxdb')) > 0

    