path=$1
for file in $path"/*"
do
  gunzip "$file"
done

