from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import re
# Create your views here.


def bubbleSort(arr):
    n = len(arr)
    
    swapped = False
   
    for i in range(n-1):
       
        for j in range(0, n-i-1):
            k = re.sub('[^.0-9]', '', arr[j][0])
            l = re.sub('[^.0-9]', '', arr[j+1][0])
            if k > l:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            
            return
    

    print("After change ")
    print(arr)
    return arr






def MainView(request):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'referer':'https://www.google.com/'
    }
    superval = []
    tesco_data = []
    dun = []
    default_products = ["drinks","vegetables","milk","fruits"]
    for i in default_products:
        a = supervalue(i,headers)
        superval.append(a)
        b = tesco(i,headers)
        tesco_data.append(b)
        c = dunnes(i,headers)
        dun.append(c)

    
    print(dun)
    
        


    return render(request,"home/main.html",context={"superval":superval,"tesco":tesco_data,"dunnes":dun})
    


def search(request):
    if request.method == 'POST':
        print("Entered here")
        cookies = dict(BCPermissionLevel='PERSONAL')
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'referer':'https://www.google.com/'
        }
        keyword = str(request.POST.get('keyword'))
        print(keyword.lower())
        # dun = dunnes(keyword,headers,cookies)
        superval = supervalue(keyword,headers)
        tesco_data = tesco(keyword,headers)
        
        print(superval)
        superval = bubbleSort(superval)
        print(tesco_data)
        tesco_data = bubbleSort(tesco_data)
        return render(request,"home/search.html",context={'superval':superval,'tesco':tesco_data})

    


def defaultcarts(request):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'referer':'https://www.google.com/'
    }
    superval = []
    tesco_data = []
    default_products = ["drinks","vegetables","milk","fruits"]
    for i in default_products:
        superval.append(supervalue(i,headers))
        tesco_data.append(supervalue(i,headers))

    return render(request,"home/main.html",context=[superval,tesco_data])


    


def tesco(keyword,headers):
    try:
        maindata = []
        print("reached here")
        page = requests.get(f'https://www.tesco.ie/groceries/en-IE/search?query={keyword}',headers=headers).text
        soup = BeautifulSoup(page,'html.parser')
        data = soup.find_all(name="li" ,class_='product-list--list-item')
        
        for i in data:
            price = i.find_all(name="p" , class_='styled__StyledHeading-sc-119w3hf-2')[0].getText()
            title = i.find_all(name="span" , class_='styled__Text-sc-1xbujuz-1')[0].getText()
            img = str(i.find_all(name="img")[0].get('srcset')).split(" ")[0]
            maindata.append((price,title,img))
    except:
        print("In exception")

    return maindata

def supervalue(keyword,headers):
    maindata = []
    print("reached here")
    page = requests.get(f'https://shop.supervalu.ie/shopping/search/allaisles?q={keyword}',headers=headers).text
    soup = BeautifulSoup(page,'html.parser')
    result = soup.find_all(name="div",class_="ga-product")
    print(len(result))
    for i in result:
        price = str(i.find_all(name="span",class_='product-details-price-item')[0].getText()).strip()
        title = i.find_all(name="h4",class_='product-list-item-details-title')[0].getText()
        img = i.find_all(name="img")[0].get('data-src')
        maindata.append((price,title,img))

    return maindata

def dunnes(keyword,headers):
    maindata = []
    print("reached here")
    page = requests.get(f'https://www.dunnesstoresgrocery.com/sm/delivery/rsid/412/results?q={keyword}').text
    soup = BeautifulSoup(page,'html.parser')
    print(soup)
    result = soup.find_all(name="div",class_="Listing--vkq6wb kayCMG")
    print(len(result))
    for i in result:
        print(i)

# def aldigroceries(keyword,headers,cook):
#     maindata = []
#     print("reached here")
#     page = requests.get(f'https://groceries.aldi.ie/en-GB/Search?keywords={keyword}',headers=headers).text
#     soup = BeautifulSoup(page,'lxml')
#     print(soup)
#     result = soup.find(name="span",class_="h4")
#     print(len(result))
#     for i in result:
#         print(i)

def carts(request,product):
    print(product)
     
    return HttpResponse("Reached here")
