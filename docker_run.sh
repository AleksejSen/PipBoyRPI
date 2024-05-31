docker run --rm -it \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v ${PWD}:/pip \
    -e DISPLAY=$DISPLAY \
    -u qtuser \
    pyqt5 nodemon --watch /pip --exec python3 /pip/tab_pipboy.py
    # jozo/pyqt5 python3 /pip/tab_pipboy.py
