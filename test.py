# import requests

# url="https://kolnovel.me/s%d8%a7%d9%84%d9%82%d8%b3-%d8%a7%d9%84%d9%85%d8%ac%d9%86%d9%88%d9%86-%d8%a7%d9%84%d8%a3%d8%b1%d9%83-%d8%a7%d9%84%d8%a3%d8%ae%d9%8a%d8%b1-%d9%86%d8%b3%d8%ae%d8%a9-%d8%a7%d9%84%d9%81%d8%a7%d9%86z-209487/"

# content=requests.get(url)

# print(content.text)



# import re

# text = "Legend of the Great Sage 19 "
# numbers = re.findall(r'\d+', text)[0]

# print(numbers)



# import re

# s = " الأب الزومبي ٧"
# numbers = re.findall(r'[0-9]+\.?[0-9]*', s)

# print(numbers)  # Output: ['6.1']








import re

s1 = "الأب الزومبي ٧"
s2 = "القس المجنون: الأرك الأخير (نسخة الفان) 3"
s3 = "روشيدير 6.1"

numbers1 = re.findall(r'[0-9٠١٢٣٤٥٦٧٨٩]+\.?[0-9٠١٢٣٤٥٦٧٨٩]*', s1)
numbers2 = re.findall(r'[0-9٠١٢٣٤٥٦٧٨٩]+\.?[0-9٠١٢٣٤٥٦٧٨٩]*', s2)
numbers3 = re.findall(r'[0-9٠١٢٣٤٥٦٧٨٩]+\.?[0-9٠١٢٣٤٥٦٧٨٩]*', s3)

print(numbers1)  # Output: ['٧']
print(numbers2)  # Output: ['3']
print(numbers3)  # Output: ['6.1']
