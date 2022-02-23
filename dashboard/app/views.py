from cProfile import label
from django.shortcuts import render,HttpResponse
import matplotlib.pyplot as plt
import pandas as pd 

# Create your views here.
def index(request):
    df = pd.read_csv("app/data.csv")
    
    # Connected and disconnected Devices
    Connected_disconnected_count= df["connected"].value_counts()
    label=Connected_disconnected_count.index
    labels=[]
    data=[]
    for i in label:
        labels.append(i)
    data1=Connected_disconnected_count.values
    print(labels,data1)
    print(data1)
    for i in data1:
        data.append(int(i))
        print(i,type(i))

    
    # Product Type
    product= df["productType"].value_counts()  
    label=product.index
    labels1=[]
    data1=[]
    for i in label:
        labels1.append(i)
    datat=product.values
    for i in datat:
        data1.append(int(i))
        print(i,type(i))
    print(labels,data,labels1,data1)    
  

    #Chip Id
    chipid= df["chipId"].value_counts()
    label=chipid.index
    labels2=[]
    data2=[]
    for i in label:
        labels2.append(i)
    datat=chipid.values
    for i in datat:
        data2.append(int(i))
        print(i,type(i))

  
    #Agentid 
    agentId= df["agentId"].value_counts()
    label=agentId.index
    labels3=[]
    data3=[]
    for i in label:
        labels3.append(i)
    datat=agentId.values
    for i in datat:
        data3.append(int(i))
        print(i,type(i))

    
    #Bootstate
    bootState= df["bootState"].value_counts()
    label=bootState.index
    labels4=[]
    data4=[]
    for i in label:
        labels4.append(i)
       
    datat=bootState.values
 
    for i in datat:
        data4.append(int(i))
        print(i,type(i))


    #Buildtrain
    buildtrain= df["buildTrain"].value_counts()
    label=buildtrain.index
    labels5=[]
    data5=[]
    for i in label:
        labels5.append(i)
    datat=buildtrain.values
    for i in datat:
        data5.append(int(i))
        print(i,type(i))
    


    #buildVersion
    buildVersion= df["buildVersion"].value_counts()
    label=buildVersion.index
    labels6=[]
    data6=[]
    for i in label:
        labels6.append(i)
    datat=buildVersion.values
    for i in datat:
        data6.append(int(i))
        print(i,type(i))


    #hardwareModel
    hardwareModel= df["hardwareModel"].value_counts()
    label=hardwareModel.index
    labels7=[]
    data7=[]
    for i in label:
        labels7.append(i)
    datat=hardwareModel.values
    for i in datat:
        data7.append(int(i))
        print(i,type(i))

    return render(request, 'index.html', {
        'labels': labels,
        'labels1':labels1,
        'labels2':labels2,
        'labels3':labels3,
        'labels4':labels4,
        'labels5':labels5,
        'labels6':labels6,
        'labels7':labels7,
        'data': data,
        'data1':data1,
        'data2':data2,
        'data3':data3,
        'data4':data4,
        'data5':data5,
        'data6':data6,
        'data7':data7,
        'colors': [
 		 "#ffd1b3",
 		 "#ffc299",
 		 "#ffb380",
 		 "#ffa366",
 		 "#ff944d",
 		 "#ff8533",
		"#4B0082","#F0E68C","#E6E6FA","#FFF0F5", "#AF4136","#POF8FF","#F5DEB3","#EE82EE","#778899","#BOC4DE","#FFFFEO","#32CD32","#FAF0E6","#FF0OFF","#40EODO","#FF6347","#D8BFD8","#D2B48C", "#FF4136","#FOF8FF","#FAEBD7","#7FFFD4","#F5F5DC","#FFE4C4","#FFEBCD","#8A2BE2","#A52A2A","#DEB887","#5F9EA0","#7FFF00","#D2691E ","#FF0OFF","#FFD700","#DAA520","#ADFF2F","#FF69B4","#CD5C5C"]
    })
    