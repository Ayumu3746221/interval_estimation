class IntervalEstimation:

    useFile: str
    sampleDatas: list[int]
    sampleDatasLength: int
    dataAve: float
    dataVariance: float
    dataUnbiasedVariance :float

    def __init__(self , useFile) -> None:
        self.useFile = useFile
        self.sampleDatas = self.__getSampleDatas()
        self.sampleDatasLength = len(self.sampleDatas)
        self.dataAve = self.__getDataAve()
        self.dataVariance = self.__getDataVariance()
        self.dataUnbiasedVariance = self.__getDataUnbiasedVariance()

    def __getSampleDatas(self) -> list[int]:
        with open(self.useFile , "r") as file:
            #txtファイルの１行を1データとして扱う
            sampleDatas:list[int] = [int(line.strip()) for line in file.readlines()] 
            return sampleDatas
        
    def __getDataAve(self) -> float:
        dataSum:float = sum(self.sampleDatas)
        dataSize:float = len(self.sampleDatas)

        dataAve = dataSum / dataSize
        return dataAve 
    
    def __getDataVariance(self) -> float:
        tmpDataList:list[float] = [] 

        for num in range(0 , len(self.sampleDatas)):
            sampleData:float = self.sampleDatas[num]
            tmp:float = (sampleData -self.dataAve) ** 2
            tmpDataList.append(tmp)

        dataVariance = sum(tmpDataList) / self.sampleDatasLength
        return dataVariance

    def __getDataUnbiasedVariance(self) -> float:
        dataUnbiasedVariance:float = (self.sampleDatasLength / (self.sampleDatasLength -1)) * self.dataVariance
        return dataUnbiasedVariance
        
    # tはt分布表のa/nの値
    def estimateAve(self , t:float) -> None:
        sampleSize = self.sampleDatasLength
        dataAve = self.dataAve
        dataUnbiasedVariance = self.dataUnbiasedVariance
        
        estimateMin = dataAve - ((t * (dataUnbiasedVariance ** 0.5)) / (sampleSize ** 0.5))
        estimateMax = dataAve + ((t * (dataUnbiasedVariance ** 0.5)) / (sampleSize ** 0.5))

        print(f"\n平均値を区間推定すると\n{estimateMin} <= μ <= {estimateMax}\n")

    # x1は引数がa/2のx^2分布表の値
    # x2は引数が(1-a/2)のx^2分布表の値
    def estimateVariance(self ,x1:float , x2 : float) -> None:
        sampleSize = self.sampleDatasLength
        dataVariance = self.dataVariance

        estimateMin = (sampleSize * dataVariance) / x1
        estimateMax = (sampleSize * dataVariance) / x2

        print(f"\n分散を区間推定すると\n{estimateMin} <= σ^2 <= {estimateMax}")

    def dataDisplay(self) -> None:
        print(f"サンプルサイズ{self.sampleDatasLength}\nサンプルデータ平均\n{self.dataAve}\nサンプルデータ標本標準分散\n{self.dataVariance}\nサンプルデータ標本不偏分散\n{self.dataUnbiasedVariance}")