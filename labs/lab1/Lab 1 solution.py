#Solution to Functional Programming Lab 1.

class SkiResort:



    def __init__(self,**kwargs):
        self.name = kwargs['name']
        self.state = kwargs['state']
        self.rating = float(kwargs['rating'])
        self.lifts = kwargs['lifts']
        self.dayprice = kwargs['price'].lstrip()


    def __lt__(self,other):
        return self.rating < other.rating

    def __str__(self):
        return f"Resort name: {self.name} Resort State {self.state} Resort Rating {str(self.rating)} Number of ski lifts: {self.lifts} Day Pass Price ${str(self.dayprice)}"


class SkiResorts:

    def __init__(self, resort_list = []):
       self.skiresorts_list = resort_list

    def add_skiresort(self,restaurant):
        self.skiresorts_list.append(restaurant)


    def get_list(self):
        return self.skiresorts_list

    def __iter__(self):
        self.indexvalue = 0
        return self

    def __next__(self):
        if len(self.skiresorts_list) == self.indexvalue:
            raise StopIteration
        else:
            returnvalue = self.skiresorts_list[self.indexvalue]
            self.indexvalue += 1
            return returnvalue


if __name__ == '__main__':
    skiresorts = SkiResorts()
    f = open('c:/Users/bbrel/functional_python/labs/lab1/data/ski_resorts.txt')
    for line in f:
        data = line.strip().split(',')
        skiresorts.add_skiresort(SkiResort(name=data[0], state = data[1], rating= data[2], lifts = data[3], price = data[4]))


#  Uncomment out the relevant lines to see the output for various sorting criteria.

   # for skiresort in skiresorts:
    #    print (skiresort)

    #sortedbyprice = sorted(skiresorts, key=lambda x: x.dayprice)

    #print ("Sorting by price ascending")
    #for s in sortedbyprice:
     #   print (s)

   # print ('Sort by price descending')
    #for s in sorted(skiresorts,key=lambda x: x.dayprice, reverse=True):
     #   print (s)

    print ('Sort by descending rating')
    for s in sorted(skiresorts,reverse=True):
        print (s)

