#######################################################
#
#   The issue is that Julia saves integers as a 64bit int which can only be
#        so big or small
#
#
#   Python is a little smarter and automatically switches to a BigInt style
#        when the numbers are growing too large
#
#######################################################



println("\nThe smallest integer Julia handles is  ", typemin(Int64), "\n" )

println("The largest integer Julia handles is  ", typemax(Int64), "\n"  )


println("If you force it to go even a little too small, stuff goes wrong  " , typemin(Int64) - 1, "\n" )

println("A little too big also ruins your world  ", typemax(Int64) +1, "\n" )
