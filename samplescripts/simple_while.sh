#this is a simple while loop, which executes a piece of code while a control expression is true and stops when it is false

COUNTER=0

while [$COUNTER -lt 10]
do 
echo My count is at $COUNTER
let COUNTER=COUNTER+1
done
