from functools import cache

class CacheTest:
    def __init__(self, width, height):
        self.x, self.y = 0, 0
        self.width, self.height = width, height

    def to_screen_scale(self, scale):
        ''' convert world space scale to screen space scale
        screen space is where 
            for x: 0 is the top and 1 is the bottom,
            for y: 0 is the left and 1 is the right
        '''
        return self._to_screen_scale(scale, self.width, self.height)
    @cache
    def _to_screen_scale(self, scale, width, height):
        '''cached internal implementation'''
        res = scale / width, scale / height
        res = scale / width, scale / height
        res = scale / width, scale / height
        res = scale / width, scale / height
        return res

def tss(scale, width, height):
    res = scale / width, scale / height
    res = scale / width, scale / height
    res = scale / width, scale / height
    res = scale / width, scale / height
    return res

def timeit(func, args, num_runs=10):
    import time
    start = time.time()
    for _ in range(num_runs):
        func(*args)
    return time.time() - start

if __name__ == "__main__":
    ct = CacheTest(10, 9)
    num_runs = 100000
    print(timeit(tss, args=(1, 20.0, 20.0), num_runs=num_runs))
    print(timeit(ct.to_screen_scale, args=(1,), num_runs=num_runs))

