set terminal pngcairo size 1200,800 enhanced font 'Arial,14'
set output 'matrix_plot.png'

set xlabel 'Offset (relative to midpoint)'
set ylabel 'Fragment Length'
set title 'Fragment Length vs Offset Matrix Plot'

set palette defined (0 "white", 1 "blue", 2 "yellow", 3 "red")

set view map
unset key

set xrange [-500:500]
set yrange [50:300]

plot 'matrix_wide_form.csv' matrix using 2:1:3 with image

