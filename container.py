class Container:
    def __init__(self,id:int,length:int,breadth:int,height:int,pricePerSqrFt:int):
        self.id = id
        self.length = length
        self.breadth = breadth
        self.height = height
        self.pricePerSqrFt = pricePerSqrFt
    
    def findVolume(self):
        return self.length*self.breadth*self.height

class PackagingCompany:
    def __init__(self,containerList:list):
        self.containerList=containerList
    
    def findContainerCost(self,id:int):
        for i in self.containerList:
            if i.id==id:
                return i.pricePerSqrFt*i.findVolume()
            
        return None
    
    def findLargestContainer(self):
        return max(self.containerList,key=lambda obj: obj.findVolume())


if __name__=="__main__":
    n = int(input())
    containerList = []

    for i in range(n):
        id = int(input())
        length = int(input())
        breadth = int(input())
        height = int(input())
        pricePerSqrFt = int(input())

        containerList.append(Container(id,length,breadth,height,pricePerSqrFt))
    
    packagingCompany = PackagingCompany(containerList)

    id = int(input())

    result = packagingCompany.findContainerCost(id)
    print(result) if result is not None else print("No Container Found")

    largestContainer = packagingCompany.findLargestContainer()
    print(largestContainer.id,largestContainer.findVolume())