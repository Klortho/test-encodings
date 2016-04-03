#!/usr/bin/env perl
use utf8;
binmode(STDOUT, ":utf8");

print "Content-type: application/javascript; charset=utf-8\n\n";
print "document.write('Here be unicode: 我的气垫船装得满是鳗鱼');\n";
