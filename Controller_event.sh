echo "....SCRIPT STARTED...."
echo "....KILL PREVIOUS BACKGROUND PROCESSES...."
pkill -f Fetch_input.py
sleep 1
echo "....STARTING python-evdev BACKGROUND PROCESS, PROCESS WILL BE KILLED WITH TERMINAL...."
python Fetch_input.py &
echo "....SLEEPING TO INITIALIZE EVDEV...."
sleep 10
PATH=$(python Find_device.py)
echo 'Event input path:'
echo $PATH
sed="/bin/sed"
sh="/bin/sh"
$sed -i "8s/.*/evdev = $PATH/" Swarms.xboxdrv
echo "....CHANGED .xboxdrv-FILE...."


xboxdrv="/usr/bin/xboxdrv"
$xboxdrv -c Swarms.xboxdrv