seconds_since_birth <- function(day, month, year) {
  # Create birth date using ISOdate
  birth_date <- ISOdate(year, month, day)
  
  # Get current date and time
  current_date <- Sys.time()
  
  # Calculate difference in seconds
  seconds_lived <- difftime(current_date, birth_date, units="secs")
  
  return(as.numeric(seconds_lived))
}

# Example usage
seconds <- seconds_since_birth(7, 7, 2005)
cat(sprintf("You have lived %d seconds", as.integer(seconds)))

