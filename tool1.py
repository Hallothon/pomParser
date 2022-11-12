# %%
import requests
from pomParser import pomParser
import time
obj=pomParser()
from selenium import webdriver

print(obj.clash)
data=obj.dependencies['dependency']
print(data)


# %%
all_new_data=[]    #contains latest version of aall dependencies
def findversions(data):
    group=data["groupId"]
    arti=data["artifactId"]
    url="https://search.maven.org/solrsearch/select?q=g:{}+AND+a:{}&core=gav&rows=20&wt=json".format(group,arti)

    # g:com.google.inject
    # guice
    response=requests.get(url)

    jsondata=response.json()
    # 
    #print(jsondata)
    newvers=[]
    # newvers=[jsondata['response']['docs'][0]['v'],jsondata['response']['docs'][1]['v']]
    for i in range(19):
        d={}
        d["groupId"]=jsondata['response']['docs'][i]['g']
        d["artifactId"]=jsondata['response']['docs'][i]['a']
        d["version"]=jsondata['response']['docs'][i]['v']
        newvers.append(d)
    print(newvers[0])
    if(newvers[0]['version']>data['version']):
        print(data['artifactId'],newvers[0]['version'],"is the latest version ","not ",data['version'])
    
    all_new_data.append(newvers[0])
    # all_new_data.add(newvers[0])



# %%


    


# %%
# from selenium import webdriver
# def find_dep(gid,aid,v):
#     driver = webdriver.Edge()
#     all_dependencies=[]
#     t=[]
#     tempk=[]
#     print('https://mvnrepository.com/artifact/{}/{}/{}'.format(gid,aid,v))
#     try:
#         driver.get('https://mvnrepository.com/artifact/{}/{}/{}'.format(gid,aid,v))
        
#     except:
#         return
#     try:

#         elements = driver.find_element("xpath","/html/body/div/main/div[1]/div[5]/div/table")
#         k=elements.text.split("\n")
#         print("elements:",elements.text)
#         for i in k:
#             if "org." in i:
#                 tempk.append(i)
#         for i in tempk:
#             t.append(i.split(" "))
#         for i in tempk:
#             json_all_dep['groupId']=i[0].strip()
#             json_all_dep['artifactId']=i[2].strip()
#             json_all_dep['version']=i[3].strip()
#             json_all_dep['newversion']=i[-1].strip()
#             all_dependencies.append(json_all_dep)
        
#     except:
#         elements = driver.find_element("xpath","/html/body/div/main/div[1]/div[4]/div/table")
#         print("elements:",elements.text)
#         k=elements.text.split("\n")
#         for i in k:
#             if "org." in i:
#                 tempk.append(i)
#         for i in tempk:
#             t.append(i.split(" "))
#         for i in tempk:
#             json_all_dep['groupId']=i[0].strip()
#             json_all_dep['artifactId']=i[2].strip()
#             json_all_dep['version']=i[3].strip()
#             json_all_dep['newversion']=i[-1].strip()
#             all_dependencies.append(json_all_dep)
#         # k=elements.text.split("Apache 2.0\norg.seleniumhq.selenium »")
#         if(k):
#             for i in range(1,len(k)):
#                 json_all_dep={}
#                 allfile=k[i].split(" ")
#                 json_all_dep['dependecy']=allfile[1]
#                 json_all_dep['oldversion']=allfile[2]
#                 json_all_dep['newversion']=allfile[3]
#                 all_dependencies.append(json_all_dep)
    
    
    
#     #print(elements.text)
#     #print(">>>>>>>>>>>>>>>>>>>>>>>>>")

    
#     #print("temp:",k)
    
    
#     # print("tempk::",tempk)
    
#     # print("t   ==",t)
    
#     print(all_dependencies)
#     return (all_dependencies)



#     # for i in range(1,len(k)):
#     #     json_all_dep={}
#     #     allfile=k[i].split(" ")
#     #     gid=k[0]
#     #     print(gid)
        
#     #     json_all_dep['artifactId']=allfile[1]
#     #     json_all_dep['version']=allfile[2]
#     #     json_all_dep['newversion']=allfile[3]
#     #     json_all_dep['groupId']=gid
        
#     # print(all_dependencies)
#     # return (all_dependencies)

    
#     # m=k[1].split(' ')
#     # json_all_dep={}
#     # json_all_dep['dependency']=m[0]
#     # json_all_dep['oldversion']=m[0]
#     # json_all_dep['newversion']=m[0]

#     # for i  in range(len(elements)):
#     #     json_all_dep={}
#     #     depend=driver.find_element("xpath","/html/body/div/main/div[1]/div[5]/div/table/tbody/tr[{}]/td[3]/a[2]".format(i))
#     #     oldversion=driver.find_element("xpath","/html/body/div/main/div[1]/div[5]/div/table/tbody/tr[{}]/td[4]/a".format(i))
#     #     newversion=driver.find_element("xpath","/html/body/div/main/div[1]/div[5]/div/table/tbody/tr[{}]/td[5]/a[2]".format(i))
#     #     json_all_dep['depend']=depend.text
#     #     json_all_dep['old_version']=oldversion.text
    
#     #     json_all_dep['new_version']=newversion.text
#     #     all_dependencies.append(json_all_dep) 1

# # elem = driver.find_elements_by_class_name('grid')  # Find the search box
# # print(elem)
# i=0

# while(i<len(all_new_data)):
#     try:
#         print(all_new_data[i]['groupId'],all_new_data[i]['artifactId'],all_new_data[i]['version'])
#         a=find_dep(all_new_data[i]['groupId'],all_new_data[i]['artifactId'],all_new_data[i]['version'])
#         for j in a:
#             if(j not in all_new_data):
#                 all_new_data.append(j)
#         i+=1
#     except:
#         break
    
# print(all_new_data)

# # temp=[]

# # for i in all_new_data:
# #     print(i["groupId"],i["artifactId"],i["version"])
# #     a=find_dep(i["groupId"],i["artifactId"],i["version"])
# #     if(a):

# #         for j in a:
# #             temp.append(j)
# # print(temp)



# %%

depObj={}
conflicts={}



def find_dep(gid,aid,v):
    time.sleep(2)
    print('https://mvnrepository.com/artifact/{}/{}/{}'.format(gid,aid,v))
    # driver = webdriver.Edge()
    print(driver.get('https://mvnrepository.com/artifact/{}/{}/{}'.format(gid,aid,v)))
    try:
        elements = driver.find_element("xpath","/html/body/div/main/div[1]/div[5]/div/table")
    except:
        elements = driver.find_element("xpath","/html/body/div/main/div[1]/div[4]/div/table")
        
    all_dependencies=[]
    
    print(elements.text)
    k=elements.text.split("\n")
    temp=[]
    
    for i in k:
        if "»" in i:
            temp.append(i.strip())

    print(temp)
    if temp==[]:
        return []
    else:
         for j in temp:
            display_json={}
            a=j.split(" ")  
            a=a[:1]+a[2:]
            display_json["groupId"]=a[0]
            display_json["version"]=a[2]
            display_json["artifactId"]=a[1]
            display_json["newVersion"]=a[3]
            all_dependencies.append(display_json)
            if a[1] in depObj.keys():
                   if a[2]!=depObj[a[1]]['version']:
                        if a[2] in conflicts.keys():
                            conflicts[a[1]].append(a[2])
                        else:
                            conflicts[a[1]]=[a[2]]
            else:
                depObj[a[1]]=display_json
         return(all_dependencies)




    
    # if(k):
    #     for i in range(1,len(k)):
    #         json_all_dep={}
    #         allfile=k[i].split(" ")
    #         json_all_dep['dependecy']=allfile[1]
    #         json_all_dep['oldversion']=allfile[2]
    #         json_all_dep['newversion']=allfile[3]
    #         all_dependencies.append(json_all_dep)
    # print(all_dependencies)



print("""

      _   ____    __  __ 
     | | |  _ \  |  \/  |
  _  | | | | | | | |\/| |
 | |_| | | |_| | | |  | |
  \___/  |____/  |_|  |_|
                         
                            Java Dependency Manager
""")

time.sleep(5)
driver = webdriver.Edge()
for i in range(len(data)):
    findversions(data[i])
# print(all_new_data)

i=0
n=len(all_new_data)
while(i<n):
    # print(len(all_new_data))
    try:
        # print(all_new_data[i]['groupId'],all_new_data[i]['artifactId'],all_new_data[i]['version'])
        a=find_dep(all_new_data[i]['groupId'],all_new_data[i]['artifactId'],all_new_data[i]['version'])
        for j in a:
            if(j not in all_new_data):
                all_new_data.append(j)
        n=len(all_new_data)
        i+=1
    except:
        break
    

print("Total Number of Dependencies: ",len(all_new_data))

print("Scanned Dependencies: ")
for i in all_new_data:
    print("> ",i)

if(len(conflicts)==0):
    print("No Conflicts Were Found")
    print("Happy Building!!!!!")

else:
    for i in conflicts:
        print("{} Conflicting Versions: {}".format(i,conflicts[i]))

# %%