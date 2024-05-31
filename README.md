# To enable live reload install:
1. `sudo npm i -g nodemon`
2. `nodemon --exec python3 tab_pipboy.py`

# Run from docker
https://github.com/jozo/docker-pyqt5

docker run --rm -it \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e DISPLAY=$DISPLAY \
    -u qtuser \
    jozo/pyqt5 python3 /tmp/hello.py
