from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #Ordered segments
    segments=sorted(segments,key=lambda x:x.end)
    """
    If condition ,finds those segments that are overlap ,
    else adds another point for those times when the segment its not
    """
    for s in segments:
        if points and s.start<=points[-1]<=s.end:
            continue
        else:
           points.append(s.end)
    return points

if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
