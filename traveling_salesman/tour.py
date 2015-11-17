import util

class Tour:
    _tour = []


    def set_tour(self, cities_list):
        self._tour = list(cities_list)


    def get_tour(self):
        list_tour = []
        for city in self._tour:
            list_tour.append(city.__dict__)
        return list_tour


    def get_binary_tour(self, origin, step):
        i = origin
        binary = []
        while True:
            current = self._tour[i - 1]._id
            binary += util.to_bin(current)
            i += step
            if i > len(self._tour):
                i -= len(self._tour)
                i -= 1
            if i == origin:
                break
        return binary