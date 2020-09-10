
run = function(){
  num = sample(0:14,1)

  if (num < 8) {
    return (TRUE)
  } else {
    return (FALSE)
  }
}

countdist = function(x,n){
  
  
  output = numeric(n)
  for (i in 1:n){
    num_wrong = x
    max_rounds = 2^(n+2)
    
    end = FALSE
    round_counter = 0
    end_counter = 0
    
    while (end == FALSE){
      round_counter = round_counter + 1
      if (round_counter > max_rounds){
        end = TRUE
      }
      
      var = run()
      
      if (var == TRUE){
        end_counter = 0
      }
      else{
        end_counter = end_counter + 1
      }
      
      if (end_counter == num_wrong){
        end = TRUE
      }
      
      
      
    }
    output[i] = round_counter
    
  }
  
  return (output)
  
}

