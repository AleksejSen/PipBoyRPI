docker run --rm -it \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v ${PWD}:/pip \
    -e DISPLAY=$DISPLAY \
    -u qtuser \
    jozo/pyqt5 python3 /pip/tab_pipboy.py
