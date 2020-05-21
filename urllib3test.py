import requests
import csv
import os
from datetime import datetime

def getDataByCode(code):
    url='http://hq.sinajs.cn/list='+code
    print(url)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    }

    get_response = requests.get(url,headers=headers,params=None)
    post_response=requests.post(url,headers=headers,data=None,json=None)

    #print(post_response)
    #print(get_response.text)
    origtext = get_response.text
    equalIndex = get_response.text.find('=')
    str1 = get_response.text[equalIndex+1:len(get_response.text)+1].strip()
    #print(str1)
    lists = str1.split('"')[1].split(',')
    #print(lists[30])
    return lists
    #['华友钴业', '33.400', '32.910', '34.440', '34.630', '33.300', '34.440', '34.450', '45475944', '1551919987.000', '127080', '34.440', '30600', '34.430', '74200', '34.420', '48148', '34.410', '82800', '34.400', '194900', '34.450', '38800', '34.460', '36848', '34.470', '49400', '34.480', '85900', '34.490', '2020-04-30', '15:00:00', '00', '']

    # 文件头，一般就是数据名
    #fileHeader = ["name", "score"]

#read code list in code.dat
def getCodeList(filename):
    datFile = open("code.dat","r")
    for item in datFile:
        codeList = item.split(',')
    #print(codeList)
    return codeList

def isVaildDate(date):
	try:
		datetime.strptime(date, '%Y-%m-%d')
		return 1
	except ValueError:
		return 0
		
def isNeedToAdd(code):
	if os.path.exists("instance.csv") == False:
		return 1
	csvFile = open("instance.csv", "r")

	reader = csv.reader(csvFile)

	for item in reader:
	#	print(len(item))
		#if (len(item) > 30):
		#	print(item[31])
		if len(item) > 30 and isVaildDate(item[31]) > 0:
			#print('valid date')
			#dt = datetime.strptime(item[30], '%Y/%m/%d')
			#curr = dt.strftime('%Y-%m-%d')
			#print(curr)
			#print(lists[30])
			if item[0] == code and item[31] == lists[31]:
				print('already have data of '+item[31])
				return 0
	csvFile.close()
	return 1


def saveDataToCSV(data,filepath):
	csvFileR = open("instance.csv", "a")
	reader = csv.reader(csvFileR)
def changeStyleOfCode(code):
    if code.startswith('6'):
        return 'sh'+code
    elif code.startswith('0') or code.startswith('3'):
        return 'sz'+code
if __name__ == '__main__':
    codeList = getCodeList("code.dat")
    csvFile = open("instance.csv", "a",newline='')
    writer = csv.writer(csvFile)
    for code in codeList:
        #print(changeStyleOfCode(code))
        codeClear = code.strip()
        fullcode = changeStyleOfCode(codeClear)
        lists = getDataByCode(fullcode)
        lists.insert(0,codeClear)
        #print(lists)
        if isNeedToAdd(codeClear) > 0:
            print(codeClear)
            writer.writerow(lists)
    csvFile.close()
# 写入的内容都是以列表的形式传入函数
#writer.writerow(fileHeader)
#writer.writerow(d1)
#writer.writerow(lists)
#writer.writerow(d1)


#csvFileR = open("instance.csv", "r")
#reader = csv.reader(csvFileR)
#for item in reader:
#	print(item[0])
#	print(item[30])

#print(get_response.content)

#print(get_response.json)
