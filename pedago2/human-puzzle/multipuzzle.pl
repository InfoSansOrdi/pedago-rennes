#! /usr/bin/perl

# Script to generate several puzzles in one shot, from a single file
# The syntax of this file is very simple.
#  Each line describe a given puzzle, the first char is the back character while the rest of this line is the content of the board
#
# Copyright (C), Martin Quinson 2018. This file is distributed under the terms of
# the GNU General Public License version 3 (http://www.gnu.org/licenses/gpl.html).
#
# This is free software: you can use it, study it, share it, and improve it (as you see fit),
# provided the same rights remain attached to all derivatives of this work.

die "Usage: multipuzzle.pl inputfile.txt\n" if ($#ARGV != 0);

my ($inputfile) = shift @ARGV;
die "Cannot open $inputfile: $!\n" unless (-e $inputfile && -r $inputfile);

my ($dataname) = $inputfile;
$dataname =~ s/\..*//g;

my ($files) = "";

open FH, "<$inputfile" || die "Cannot read from $filename: $!\n";
my ($count) = 0;
while (my $line = <FH>) {
    print "XXXX ./humanpuzzle.pl $line\n";
    $line =~ s/#.*//;
    next unless $line =~ m/[a-zA-Z]/;
    $line =~ s/;/\\;/g;
    $line =~ s/"/\\"/g; # "
    $line =~ s/'/\\'/g; # '
    qx,./humanpuzzle.pl $line,; # && die "Cannot generate this file: $!\n";
    print "mv board.pdf $dataname-$count.pdf\n";
    system("mv board.pdf $dataname-$count.pdf") && die "Cannot rename this file: $!\n";
    $files .= " $dataname-$count.pdf";
    $count++;
}
close FH;

qx,pdfjoin --outfile ${dataname}.pdf $files, && die "Cannot run pdfjoin: $!\n";
qx,rm $files, && die "Cannot remove temp files: $!\n";
