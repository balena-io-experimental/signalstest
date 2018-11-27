#!/bin/sh

trap 'increment' 2 3 6 15

increment()
{
  echo "Caught SIGNAL ..."
  X=`expr ${X} + 500`
  if [ "${X}" -gt "1000" ]
  then
    echo "Okay, I'll quit ..."
    exit 1
  fi
}

### main script
X=0
while :
do
  echo "X=$X"
  X=`expr ${X} + 1`
  sleep 1 & wait $!
done
