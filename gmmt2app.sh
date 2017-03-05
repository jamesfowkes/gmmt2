#!/bin/sh

### BEGIN INIT INFO
# Provides:          gmmt2app
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: GetMeToTown website
# Description:       Python Flask webserver querying TransportAPI
### END INIT INFO

# Change the next 3 lines to suit where you install your script and what you want to call it
DIR=/home/pi/gmmt2
DAEMON=$DIR/runapp.py
DAEMON_NAME=gmmt2app
LOGFILE=/var/log/gmmt2app/log
CONFIGFILE=/home/pi/gmmt2/config.yaml

# Source configuration options
[ -f /etc/default/gmmt2app/config ] && . /etc/default/gmmt2app/config

# Add any command line options for your daemon here
DAEMON_OPTS="$CONFIGFILE $LOGFILE --public --debug"

# This next line determines what user the script runs as.
# Root generally not recommended but necessary if you are using the Raspberry Pi GPIO from Python.
DAEMON_USER=pi

# The process ID of the script when it runs is stored here:
PIDFILE=/tmp/$DAEMON_NAME.pid

. /lib/lsb/init-functions

do_start () {
    log_daemon_msg "Starting system $DAEMON_NAME daemon"
    log_daemon_msg "Using API URL $TRANSPORT_API_URL"
    start-stop-daemon --start --background --pidfile $PIDFILE --make-pidfile --user $DAEMON_USER --chuid $DAEMON_USER --startas /bin/bash -- -c "exec $DAEMON $DAEMON_OPTS > /var/log/gmmt2app/stdout 2>&1"
    log_end_msg $?
}
do_stop () {
    log_daemon_msg "Stopping system $DAEMON_NAME daemon"
    start-stop-daemon --stop --pidfile $PIDFILE --retry 10
    log_end_msg $?
}

case "$1" in

    start|stop)
        do_${1}
        ;;

    restart|reload|force-reload)
        do_stop
        do_start
        ;;

    status)
        status_of_proc "$DAEMON_NAME" "$DAEMON" && exit 0 || exit $?
        ;;

    *)
        echo "Usage: /etc/init.d/$DAEMON_NAME {start|stop|restart|status}"
        exit 1
        ;;

esac
exit 0
