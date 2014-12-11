kill -9 `ps auxw | grep site | grep $USER | awk '{print $2}'`
