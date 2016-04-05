try() { 
  echo "Trying $T"
  echo "  LC_ALL=$LC_ALL"
  echo "  LANG=$LANG"

  echo "  python2"
  python2 py-has-utf8.py > /dev/null 2>&1
  echo "    script has utf-8: $?"
  python2 py-read-utf8.py > /dev/null 2>&1
  echo "    script can read utf-8: $?"

  echo "  python2"
  python3 py-has-utf8.py > /dev/null 2>&1
  echo "    script has utf-8: $?"
  python3 py-read-utf8.py > /dev/null 2>&1
  echo "    script can read utf-8: $?"
}

export T='Current NCBI setting'
export LC_ALL=POSIX
unset LANG
try

export T='Unset both'
unset LC_ALL
unset LANG
try

export T='Set LC_ALL'
export LC_ALL=en_US.UTF-8
unset LANG
try

export T='Set LANG'
unset LC_ALL
export LANG=en_US.UTF-8
try