def outer():
  print("In Outer function")

  def inner():
    print("In inner funtion")
    
  inner()
  
outer()
inner = 