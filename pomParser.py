import xml.etree.ElementTree as ET
import re
import os


class pomParser:
    fileName='pom.xml'
    directory=os.getcwd()
    subDepObj={}
    clash=0
    clashedDep={}
    def __init__(self):
        self.paths=[]
        self.dependencies=[]
        self.createPomObject()
        self.findDependencies()

    def findPom(self,path):
        obj={}
        pomFile=open(path,"r")
        xmlString=pomFile.read()
        xmlString=re.sub(' xmlns="[^"]+"', '', xmlString, count=1)
        treeRoot=ET.fromstring(xmlString)
        obj['groupId']=treeRoot.find('groupId').text
        obj['artifactId']=treeRoot.find('artifactId').text
        obj['version']=treeRoot.find('version').text
        dependencies=treeRoot.find('dependencies')
        dependency=[]
        for x in dependencies.findall('dependency'):
            dep={}
            dep['groupId']=x.find('groupId').text
            dep['artifactId']=x.find('artifactId').text
            dep['version']=x.find('version').text
            dependency.append(dep)
        obj['dependency']=dependency
        self.dependencies=obj


    def findPath(self):
        for root, dir, files in os.walk(self.directory):
            if self.fileName in files:
                self.paths.append(os.path.join(root,self.fileName))
        
        
    def createPomObject(self):
        self.findPom(self.directory+'/'+self.fileName)
        self.findPath()
        if self.directory+'/'+self.fileName in self.paths:
            self.paths.remove(self.directory+'/'+self.fileName)
        #for x in self.paths:
        #    self.findPom(x)
    def findDependencies(self):
        for path in self.paths:
            pomFile=open(path,"r")
            xmlString=pomFile.read()
            xmlString=re.sub(' xmlns="[^"]+"', '', xmlString, count=1)
            treeRoot=ET.fromstring(xmlString)
            dependencies=treeRoot.find('dependencies')
            for x in dependencies.findall('dependency'):
                dep={}
                dep['groupId']=x.find('groupId').text
                artifactId=x.find('artifactId').text
                dep['version']=x.find('version').text
                if artifactId in self.subDepObj.keys():
                    self.clash+=1
                    self.clashedDep[artifactId]=dep
                else:
                    self.subDepObj[artifactId]=dep
        

if __name__=="__main__":
    obj=pomParser()
    print(obj.clash)
    print(obj.subDepObj)
    print(obj.clashedDep)
    print(obj.dependencies)
