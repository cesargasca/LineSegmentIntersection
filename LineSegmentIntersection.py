import poly_point_isect
class Point:
    def __init__(self, x, y):
      self.x = x
      self.y = y
    def __str__(self):
      return "x: " + str(self.x) + " y: " + str(self.y)
    def minX(self,p2):
      if self.x < p2.x:
        return self.x
      else:
        return p2.x
    def maxX(self,p2):
      if self.x > p2.x:
        return self.x
      else:
        return p2.x
    def minY(self,p2):
      if self.y < p2.y:
        return self.y
      else:
        return p2.y
    def maxY(self,p2):
      if self.y > p2.y:
        return self.y
      else:
        return p2.y   
    def resta(self,p1):
      return Point(self.x - p1.x,self.y - p1.y)
    def productoCruz(self,p1,p2):
      return (p1.x * p2.y) - (p2.x * p1.y)
    def direccion(self,p1,p2,p3):
      ax = p3.resta(p1)
      bx = p2.resta(p1)
      return ax.productoCruz(ax,bx)
    def estaSegmento(self,p1,p2,p3):
      if p3.x >= p1.minX(p2) and p3.x <= p1.maxX(p2) and p3.y >= p1.minY(p2) and p3.y <= p1.maxY(p2):
        return True
      else:
        return False
    def interseccion(self,p1,p2,p3,p4):
      d1 = p1.direccion(p3,p4,p1)
      d2 = p1.direccion(p3,p4,p2)
      d3 = p1.direccion(p1,p2,p3)
      d4 = p1.direccion(p1,p2,p4)
      if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0 )):
        return True
      elif d1 == 0 and p1.estaSegmento(p3,p4,p1) == True:
        return True
      elif d2 == 0 and p1.estaSegmento(p3,p4,p2) == True:
        return True
      elif d3 == 0 and p1.estaSegmento(p1,p2,p3) == True:
        return True
      elif d4 == 0 and p1.estaSegmento(p1,p2,p4) == True:
        return True  
      else:
        return False

def getIntersections(data): 
  isect = poly_point_isect.isect_segments(data) #recibe tuplas (puntos)
  return isect #regresa intersecciones

class Segment:
  def __init__(self,p1,p2):
    self.p1 = p1
    self.p2 = p2
  def __str__(self):
    return "Linea: " + str(self.p1) + " , " + str(self.p2)
  def intersection(self,a,b):
    p = Point(0,0)
    return p.interseccion(a.p1,a.p2,b.p1,b.p2)
  def puntoInterseccion(self,a,b):
    ma = (a.p2.y - a.p1.y) / (a.p2.x - a.p1.x)
    mb = (b.p2.y - b.p1.y) / (b.p2.x - b.p1.x)
    x =  (ma*a.p1.x - mb*b.p1.x - a.p1.y + b.p1.y) / (ma-mb)
    y =   ma*(x-a.p1.x) + a.p1.y
    return Point(x,y)
if __name__ == "__main__":
  p1 = Point(0,0)
  p2 = Point(2,2)
  q1 = Point(0,2)
  q2 = Point(2,0)
  p = Segment(p1,p2)
  q = Segment(q1,q2)
  data = (
  ((0.000000, 0.000000), (2.000000, 2.000000)),
  ((0.000000, 2.000000), (2.000000, 0.000000)),
  )
  data2 = (
    ((1,0),(1,3)),
    ((2,0),(2,3)),
    ((0,1),(3,1)),
    ((0,2),(3,2)),
  )
  i = q.intersection(p,q)
  pi = q.puntoInterseccion(p,q)
  print(i)
  print(pi)
  print(getIntersections(data))
  print(getIntersections(data2))