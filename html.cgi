#!/usr/bin/env perl
use utf8;
binmode(STDOUT, ":utf8");

print "Content-type: text/html\n\n";
print "<p>HTML from a CGI with LC_ALL=$ENV{LC_ALL}, LANG=$ENV{LANG}:" .
      " 我的气垫船装得满是鳗鱼</p>\n";
