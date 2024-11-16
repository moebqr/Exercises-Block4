# Print each multiplication table separately
for(i in 1:12) {
  cat(sprintf("\nTimes table for %d:\n", i))
  cat("--------------------\n")
  for(j in 1:12) {
    cat(sprintf("%d x %d = %d\n", i, j, i*j))
  }
  cat("\n")
}

