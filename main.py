import requests
import json
result=requests.get('https://saral.navgurukul.org/api/courses')
data=result.json()
with open("availableCourses.json","w")as f:
    json.dump(data,f,indent=4)
def opt(select,var2,slug,data2):
    while True:
        x=var2
        print(".....................")
        options=input("enter your option :up,next,exit,back :-")
        if options=="up":
            print(x)
            x-=1
            req=requests.get("https://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getBySlug?slug="+str(slug[x]))
            r=req.json()
            print("content",r["content"])
            print(x)
        elif options=="next":
            x+=1
            req=requests.get("https://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getBySlug?slug="+str(slug[x-1]))
            r1=req.json()
            print("content",r1["content"])
            print(x)
        elif options=="back":
            c=1
            for dic1 in data2["data"]:
                print(c,dic1["name"])
                c+=1
                for i in dic1["childExercises"]:
                    print("    ",c,i["name"])
                    c+=1
        else:
            break
def course():
    index=0
    for i in data["availableCourses"]:
        print(index+1,i["name"],i["id"])
        index+=1
    for courses in data["availableCourses"]:
        course=int(input("enter your index of course= "))
        select=data["availableCourses"][course-1]["id"]
        var=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercises")
        data2=var.json()
        count=1
        slug=[]
        for dic_data2 in data2["data"]:
            print(count,dic_data2["name"])
            slug.append(dic_data2["slug"])
            count=count+1
            for child in dic_data2["childExercises"]:
               print("      ",count,child["name"])
               slug.append(child["slug"])
               count+=1
        var2=int(input("select content slug:"))
        var3=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getBySlug?slug="+str(slug[var2-1]))
        data3=var3.json()
        opt(select,var2,slug,data2)

course()



# import requests
# import json
# result = requests.get("https://saral.navgurukul.org/api//courses")
# data = result.json()
# with open("avalableCourses","w")as f:
#     json.dump(data,f,indent=4)
# def opt(select,var2,slug,data2):
#     while True:
#         x = var2
#         print("*******************")
#         options = input("enter your option : up,next,exit,back :-")
#         if options == "up":
#             print(x)
#             x = x - 1
#             req = requests.get("https://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getByeSlug?slug="+str(slug[x]))
#             r = req.json()
#             print("content",r["content"])
#             print(x)
#         elif options == "next":
#             x = x + 1
#             req = requests.get("https://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getByeSlug?slug="+str(slug[x-1]))
#             r1 = req.json()
#             print("content",r1["content"])
#             print(x)
#         elif options == "back":
#             c = 1
#             for dic1 in data2["data"]:
#                 print(c,dic1["name"])
#                 c = c + 1
#                 for i in dic1["childExercises"]:
#                     print(" ",c,i["name"])
#                     c = c + 1
#         else:
#             break
# def course():
#     index = 0
#     for i in data["avalableCourses"]:
#         print(index+1,i["name"],i["id"])
#         index = index + 1
#     for courses in data["avalableCourses"]:
#         course = int(input("enter your index of course = "))
#         select = data["avalibleCourses"][course-1]["id"]
#         var = requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercise")
#         data2 = var.json()
#         count = 1
#         slug =[]
#         for dic_data2 in data2["data"]:
#             print(count,dic_data2["name"])
#             slug.append(child["slug"])
#             count = count + 1
#             for child in dic_data2["childExercises.json"]:
#                 print(" ",count,child["name"])
#                 slug.append(child["slug"])
#                 count = count + 1
#         var2 = int(input("select content slug:"))
#         var3 = requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getBySlug?slug="+str(slug[var2-1]))
#         data3 = var3.json()
#         print("content",data3["content"])
#         opt(select,var2,slug,data2)
# course()
            




        




























                    




























