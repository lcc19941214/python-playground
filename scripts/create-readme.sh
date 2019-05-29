#!/bin/bash

root=$(pwd)
README="$root/README.md"
echo -e '# Python Playground\n' >$README

ignore_names=(
  'README.md'
  '__init__.py'
)

function contains() {
  local list=$1
  local filename=$2
  local in=0
  for item in ${list[@]}; do
    if [ $item == $filename ]; then
      in=1
      break
    fi
  done
  return $in
}

function generate() {
  local DIR=$1
  local anchor=$2
  local filenames=$(ls $DIR)
  local files=()
  local dirs=()

  for filename in ${filenames[@]}; do
    local dir="$DIR/$filename"
    contains "${ignore_names[*]}" $filename
    local shouldIgnore=$?
    if [ $shouldIgnore -eq 1 ]; then
      continue
    fi

    if [[ $filename == *'.pyc'* ]]; then
      continue
    fi

    if [ -d $dir ]; then
      dirs=(${dirs[@]} $filename)
    elif [ -f $dir ]; then
      files=(${files[@]} $filename)
    fi
  done

  for file in ${files[@]}; do
    local dir="$DIR/$file"
    echo "- [$file]($dir)" >>$README
  done

  for file in ${dirs[@]}; do
    local dir="$DIR/$file"
    if [ -e "$dir/README.md" ]; then
      echo -e "\n[$anchor $file]($dir/README.md)\n" >>$README
    else
      echo -e "\n$anchor $file\n" >>$README
    fi

    generate "$dir" "$anchor#"
  done
}

generate './src' '##'
echo 'done'
