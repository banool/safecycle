#!/bin/sh

if [ $# -lt 2 ]; then
    echo 'Please supply static and API port'
    exit 1
fi

STATIC_PORT=$1
API_PORT=$2


# GNU parallel use to make sure both keep running
cat <<EOF | parallel --halt now,done=1  
echo 'Running Static Server'; python3 -m http.server $STATIC_PORT --directory web; exit 0
echo 'Running API Server'; python3 scripts/server.py $API_PORT; exit 0
EOF
echo "One of the two servers failed"
