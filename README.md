# ROS encoders in Docker [![](https://img.shields.io/docker/pulls/frankjoshua/ros-encoders)](https://hub.docker.com/r/frankjoshua/ros-encoders) [![Build Status](https://travis-ci.org/frankjoshua/docker-ros-encoders.svg?branch=master)](https://travis-ci.org/frankjoshua/docker-ros-encoders)

## Description

Publishes topics:<br>
/left_wheel (Int32)<br>
/right_wheel (Int32)<br>
Parses CSV output from an Arduino over serial<br>
Example Arduino Code<br>
[https://github.com/frankjoshua/arduino-dual-ls7366r](https://github.com/frankjoshua/arduino-dual-ls7366r)

## Example

```
docker run -it \
    --network="host" \
    --env="ROS_IP=$ROS_IP" \
    --env="ROS_MASTER_URI=$ROS_MASTER_URI" \
    --device "/dev/ttyACM1:/dev/ttyACM0"
    frankjoshua/ros-encoders
```

## Testing

Travis CI expects the DOCKER_USERNAME and DOCKER_PASSWORD variables to be set in your environment.

## License

Apache 2.0

## Author Information

Joshua Frank [@frankjoshua77](https://www.twitter.com/@frankjoshua77)
<br>
[http://roboticsascode.com](http://roboticsascode.com)
