import requests

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def intagRecovery(stringss):
    inTags = []
    instreak = False
    for char in stringss:
        if char == ">":
            temp = ""
            instreak = True
        elif char == "<" and instreak:
            if temp == "":
                continue
            inTags.append(temp)
            temp = ""
            instreak = False
        elif instreak:
            temp += char
    return inTags

def scrapFromCode(code: str) -> dict:
    """
    Parameter
    ----------
    `code`: string
        a string of code that represents the art
        biasa disebut `kode nuklir` terdiri dari
        5 atau 6 digit, biasa terletak di address atau 
        cover
        `https://nhentai.net/g/******`
    
    Return
    ------
    `info` : dictionary
        dictionary untuk kode yang diberikan

        key value pair:
        code       : string 
        altcode    : string
        thumbnail  : string
        title_en   : string
        title_jp   : string
        parodies   : list[string]
        characters : dict
        tags       : dict
        artists    : dict
        groups     : dict
        languages : dict
        categories : dict
        Pages      : integer
    """
    htmlkotor = requests.get(f"https://nhentai.net/g/{code}").text
    infoSection = htmlkotor.split("\n")
    
    title1 = htmlkotor[infoSection[4].find("""<span class="pretty">""") + 25:infoSection[4].find("""</span><span class="after">""") + 4]
    title2 = htmlkotor[find_nth(infoSection[4], """<span class="pretty">""", 2) + 25:find_nth(infoSection[4], """</span><span class="after">""", 2)]

    altcodeIndex = infoSection[4].find("""https://t.nhentai.net/galleries/""") + 36
    altCode = htmlkotor[altcodeIndex: altcodeIndex + 7]
    if not altCode.isnumeric:
        altCode = altCode[:-1]
    thumbnail = htmlkotor[altcodeIndex - 32: altcodeIndex + 17]
    parodiesSection = infoSection[6]
    characterSection = infoSection[8]
    tagsSection = infoSection[10]
    artistSection = infoSection[12]
    groupsSection = infoSection[14]
    languagesSection = infoSection[16]
    categoriesSection = infoSection[18]
    pagesSection = infoSection[20]

    result = {}
    result["code"] = code
    result["altcode"] = altCode
    result["thumbnail"] = thumbnail
    result["title1"] = title1
    result["title2"] = "" if len(title2) > 200 else title2
    result["parodies"] = {key: val for key in intagRecovery(parodiesSection)[::2] for val in intagRecovery(parodiesSection)[1::2]}
    result["characters"] = {key: val for key in intagRecovery(characterSection)[::2] for val in intagRecovery(characterSection)[1::2]}
    result["tags"] = {key: val for key in intagRecovery(tagsSection)[::2] for val in intagRecovery(tagsSection)[1::2]}
    result["artists"] = {key: val for key in intagRecovery(artistSection)[::2] for val in intagRecovery(artistSection)[1::2]}
    result["groups"] = {key: val for key in intagRecovery(groupsSection)[::2] for val in intagRecovery(groupsSection)[1::2]}
    result["languages"] = {key: val for key in intagRecovery(languagesSection)[::2] for val in intagRecovery(languagesSection)[1::2]}
    result["categories"] = {key: val for key in intagRecovery(categoriesSection)[::2] for val in intagRecovery(categoriesSection)[1::2]}
    result["pages"] = intagRecovery(pagesSection)[0]

    return result

def getCodes(tag = "main", freq = ""):
    link = "https://nhentai.net"
    link += "" if tag == "main" else f"/tag/{tag}/{freq}"
    htmlkotor = requests.get(link).text
    gIndex = [m.start() for m in re.finditer('/g/', htmlkotor)]
    return [htmlkotor[i + 3: i + 9] for i in gIndex]
