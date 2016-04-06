#!/usr/bin/env perl
use utf8;
binmode(STDOUT, ":utf8");

print "Content-type: text/javascript; charset=utf-8\n\n";
print "document.write('LC_ALL=$ENV{LC_ALL}, LANG=$ENV{LANG}: 我的气垫船装得满是鳗鱼');\n";
