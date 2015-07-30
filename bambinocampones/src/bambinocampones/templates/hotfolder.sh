cd "in"

while sleep 1; do
    for i in *; do
        if [ -e "$i" ]; then
            convert -thumbnail 640x640 "$i" "$i"
            mv "$i" ../out/
            echo "$i convertido"
        fi
    done
done
