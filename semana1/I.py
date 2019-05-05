class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.slope = (start[1] - end[1])/(start[0] - end[0])

    def get_y(self, x):
        return self.slope*(x-self.start[0])+self.start[1]

class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def contain_line(self, line):
      (xs, ys) = line.start
      (xe,ye) = line.end
      for x in range(xs, xe):
          if self.contain_point(x,line.get_y(x)):
              return True
              break
      return False

    def contain_point(self, x, y):
        if x > self.top_left[0] and x < self.bottom_right[0] and y > self.bottom_right[1] and y < self.top_left[1] :
            return True
        return False

def i(case):
    l = str.split(case, " ")
    line = Line((int(l[0]), int(l[1])),(int(l[2]), int(l[3])))
    rectangle = Rectangle((int(l[4]), int(l[5])),(int(l[6]), int(l[7])))
    if rectangle.contain_line(line):
        return "T"
    else:
        return "F"

def test_cases():
   return ["4 9 11 2 1 5 7 1", "4 3 11 2 1 5 7 1"]

def run():
    for case in test_cases():
        print(i(case))

run()
