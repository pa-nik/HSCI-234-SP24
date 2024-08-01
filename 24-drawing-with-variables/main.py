import js as p5

def setup():
  p5.createCanvas(300, 300)    

def draw():
  p5.background(255)  # white background
  p5.fill(255)  # white fill
  
  y = 60 # variable for vertical position
  d = 75 # variable for circle diameter
  
  # draw 3 circles:
  p5.ellipse(60, y, d, d) 
  p5.ellipse(150, y, d, d) 
  p5.ellipse(240, y, d, d) 

  p5.fill(150)  # gray fill
  
  # draw circles with a simple loop:
  for i in range(3):
    x = 60 + i*90 
    y = 150
    p5.ellipse(x, y, d, d) 
    
  # draw circles with a loop using 3 parameters (start, stop, step):
  for x in range(60, 250, 90):
    gray = 255 - x
    p5.fill(gray)
    p5.ellipse(x, 240, d, d) 



  
