#! /usr/bin/perl

# Script to create the material for a Human Puzzle from the sentence to encode.
#
# Usage: just provide a symbol to print on the back and a text file containing your sentence (or directly your sentence).
#
# Copyright (C), Martin Quinson 2018. This file is distributed under the terms of
# the GNU General Public License version 3 (http://www.gnu.org/licenses/gpl.html).
#
# This is free software: you can use it, study it, share it, and improve it (as you see fit),
# provided the same rights remain attached to all derivatives of this work.
  

use strict;

die "Usage: humanpuzzle-generate.pl pagenum sentence.txt\n" if ($#ARGV == 0);

my $pageback = shift @ARGV;


sub readfile ($) {
    my $filename = shift;
    die "Cannot read from $filename: file not found.\n" unless (-e $filename);
    
    open FH, "<$filename" || die "Cannot read from $filename: $!\n";
    my ($res) = do { local $/; <FH> };
    close FH;
    
    return $res;
}
sub writefile ($$) {
    my $filename = shift;
    my $ctn = shift;
    
    open FH, ">$filename" || die "Cannot write into $filename: $!\n";
    print FH $ctn;
    close FH || die "Cannot write into $filename: $!\n";
}

my (@words);
my ($dataname) = ("board");
if (-e $ARGV[0]) {
    $dataname = shift @ARGV;
    print "Reading the sentence from '$dataname'...";
    @words = split(" ", readfile($dataname));
} else {
    print "Reading the sentence from the command line...";
    @words = @ARGV;
}
my ($word_count) = scalar @words;

print "Input has $word_count words: ";
map { print "'".$_."' " } @words;
print "\n";

# Create the pageback we'll need
my $pageback_ctn = readfile("pageback.svg");
$pageback_ctn =~ s/P°/${pageback}/gm;
writefile("tmp-back.svg", $pageback_ctn);
qx,inkscape --export-pdf=tmp-back.pdf tmp-back.svg, && die "Cannot use inkscape to convert svg files into pdf files\n";
unlink("tmp-back.svg");

# Compute the geometry of the pages to build
my ($sizeX,$sizeY);
if ($word_count eq 12) {
    ($sizeX, $sizeY) = (4,3);
} elsif ($word_count eq 24) {
    ($sizeX, $sizeY) = (6,4);
} elsif ($word_count eq 30) {
    ($sizeX, $sizeY) = (5,6);
} elsif ($word_count eq 36) {
    ($sizeX, $sizeY) = (6,6);
} else {
    die "I cannot deal with $word_count words yet. Please extend me.\n";
}
die "Bug: my settings for $word_count cells is buggy: ${sizeX}x${sizeY}\n" unless ($sizeY*$sizeX == $word_count);

# Compute how the placement of cells on the printed pages
my (@fullP); # $fullP[x][y]: page number on which the cell (x,y) of the full puzzle is placed
my (@fullC); # $fullC[x][y]: cell number on the printed page for the cell (x,y) of the full puzzle
my (@page);  # $page[P][C]{'x'}: x coordinate on full puzzle of the cell printed in cell C on page P
             # $page[P][C]{'y'}: y coordinate on full puzzle of the cell printed in cell C on page P
             # $page[P][C]{'txt'}: text to print in the cell printed in cell C on page P
             # $page[P][C]{'a'}: top border, 'b': right border, 'c': bottom border, 'd': left border

my ($cellidx) = 0;
for my $y (0..($sizeY-1)) {    
    for my $x (0..($sizeX-1)) {
	my ($P,$C) = (int($cellidx / 12), $cellidx % 12);	
	$fullP[$x][$y] = $P;
	$fullC[$x][$y] = $C;
	$page[$P][$C]{'x'} = $x;
	$page[$P][$C]{'y'} = $y;
	$page[$P][$C]{'txt'} = $words[$cellidx];
	$cellidx++;	
	print "p".$fullP[$x][$y]."c".$fullC[$x][$y]." ";
    }
    print "\n";
}

my ($page_count) = $word_count / 12 + (($word_count % 12) eq 0? 0 : 1);

for my $P (0..$page_count) {
    for my $C (0..12) {
	print "($P,$C)".$page[$P][$C]{'txt'}.'    ';
	print "\n" if (($C+1) % 4 eq 0);
    }
}

# Compute the values of the cells' borders
my (%borders); # if $border{blah} is defined, then it was already used
$borders{"66"} = $borders{"69"} = $borders{"96"} = $borders{"99"} = 1; # forbid these
sub newborder() {
    my ($res);
    do {
	$res = int(rand(89)+1);
#	print "[$res] " if defined($borders{$res});
    } while (defined($borders{$res}));
    $borders{$res}="1";
#    print "$res ";
    return $res;
}
for my $x (0..($sizeX-1)) { 
    $page[ $fullP[$x][0]        ][ $fullC[$x][0]        ]{'a'} = newborder(); # Unmatched top neighbor on top
    $page[ $fullP[$x][$sizeY-1] ][ $fullC[$x][$sizeY-1] ]{'c'} = newborder(); # Unmatched bottom neighbor on bottom
}
for my $y (0..($sizeY-1)) { 
    $page[ $fullP[0][$y]        ][ $fullC[0][$y]        ]{'d'} = newborder(); # Unmatched left neighbor on left
    $page[ $fullP[$sizeX-1][$y] ][ $fullC[$sizeX-1][$y] ]{'b'} = newborder(); # Unmatched right neighbor on right
}
for my $y (0..($sizeY-1)) { 
    for my $x (1..($sizeX-1)) {
	my ($border) = newborder();
	$page[ $fullP[$x-1][$y] ][ $fullC[$x-1][$y] ]{'b'} = $border; # right border of left cell
	$page[ $fullP[$x]  [$y] ][ $fullC[$x]  [$y] ]{'d'} = $border; # left border of the right cell
    }
}
for my $y (1..($sizeY-1)) { 
    for my $x (0..($sizeX-1)) {
	my $border = newborder();
	$page[ $fullP[$x][$y-1] ][ $fullC[$x][$y-1] ]{'c'} = $border; # bottom border of top cell
	$page[ $fullP[$x][$y]   ][ $fullC[$x][$y]   ]{'a'} = $border; # top border of the bottoù cell
    }
}

# Generate the pages
my ($file_list) = "";
for my $P (0..$page_count-1) {
    print "Generate page ".($P+1)."\n";
    my ($ctn)=readfile("inputpuzzle.svg");
    for my $C (0..12) {
	my ($a,$b,$c,$d,$txt)=($page[$P][$C]{'a'},$page[$P][$C]{'b'},$page[$P][$C]{'c'},$page[$P][$C]{'d'},$page[$P][$C]{'txt'});
	my ($id) = $C+1; # the input file starts counting on 1 while we count on 0 in this program
	$txt =~ s/_/ /g;
	$txt =~ s/\\n/\n/g;
	$ctn =~ s|>${id}a</tspan|>${a}</tspan|gm;
	$ctn =~ s|>${id}b</tspan|>${b}</tspan|gm;
	$ctn =~ s|>${id}c</tspan|>${c}</tspan|gm;
	$ctn =~ s|>${id}d</tspan|>${d}</tspan|gm;
	$ctn =~ s|>TXT${id}</tspan|>${txt}</tspan|gm;
    }
    writefile("tmp-page-$P.svg",$ctn);
    qx,inkscape --export-pdf=tmp-page-$P.pdf tmp-page-$P.svg, && die "Cannot use inkscape to convert svg files into pdf files\n";
    unlink("tmp-page-$P.svg");    
    $file_list .= "tmp-page-$P.pdf tmp-back.pdf ";
}

$dataname =~ s/\..*//g;
print "Join the pages and remove temp files\n";
qx,pdfjoin --outfile ${dataname}.pdf $file_list, && die "Cannot run pdfjoin: $!\n";
unlink("tmp-back.pdf") || die "Cannot remove tempfile: $!\n";
for my $P (0..$page_count-1) {
    unlink("tmp-page-$P.pdf") || die "Cannot remove tempfile: $!\n";
}

exit 0;