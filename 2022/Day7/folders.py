class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Dir
    def __init__(self, name, within=None):
        self.name = name
        self.within = within
        self.dirContents = [] # List of directories in currrent directory
        self.fileContents = [] # List of files in currrent directory
        
    def addFile(self, fileName, size):
        if not [file for file in self.fileContents if file.name == file_name]:
            self.dirContents.append(File(fileContents, int(size)))
    
    def cd(self, dirName):
        dirContents = next((dir for dir in self.dirContents if dir.name == dirName), None)
        if not subDir:
            subDir = Dir(dirName, self)
            self.dirContents.append(subDir)
        return subDir
    def back(self):
        if self.within:
            return self.within
        else:
            print("No Dir above root")
    
    def getSize(self):
        size = sum([file.size for file in self.fileContents]) + sum([subDir.size for subDir in self.dirContents])
        return size # could add this to above
    
    def getAllSubDirs(self):
        return self.dirContents + list(chain.from_iterable([subDir.getAllSubDirs for subDir in self.dirContents]))
            
    def getTotal(self, minSize):
        return sum([subDir.size for subDir in self.getAllSubDirs if subDir.size <= minSize])

    def getMinSubSize(self, maxSize):
        return min([subDir.size for subDir in self.getAllSubDirs if subDir.size >= maxSize])
                                                           
with open('day7.txt', 'r') as f:
          lines = f.readlines()
          rootDir = Dir('root')
          for line in lines:
              if line == '$ cd ..':
                  
          
        
        
