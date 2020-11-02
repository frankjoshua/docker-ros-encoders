FROM ros:noetic-ros-base

RUN apt-get update &&\
  apt-get install -y python3-pip &&\
  apt-get -y clean &&\
  apt-get -y purge &&\
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN python3 -m pip install pyserial

COPY node.py /

ENV ROS_NODE=encoders

HEALTHCHECK CMD /ros_entrypoint.sh rosnode info $ROS_NODE || exit 1

CMD ["python3", "/node.py"]