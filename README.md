# nhentai-simple-api
Unofficial nhentai api to fetch information of an *art* using python

## methods

### scrapFromCode

  get information of an art from known code
  
  parameter : 
  
    code (string)
              
  return    : 
  
    nhentai info (dictionary)
  
  example output
<details>

  ```
   >>> scrapFromCode("177013")
 
 {
    "code": "177013",
    "altcode": "987560",
    "thumbnail": "https://t.nhentai.net/galleries/987560/cover.jpg",
    "title1": "METAMORPHOSIS",
    "title2": "",
    "parodies": {},
    "characters": {},
    "tags": {
        "group": "586",
        "stockings": "586",
        "anal": "586",
        "schoolgirl uniform": "586",
        "nakadashi": "586",
        "blowjob": "586",
        "ahegao": "586",
        "incest": "586",
        "double penetration": "586",
        "dark skin": "586",
        "x-ray": "586",
        "impregnation": "586",
        "mind break": "586",
        "story arc": "586",
        "mmf threesome": "586",
        "pregnant": "586",
        "drugs": "586",
        "prostitution": "586",
        "piercing": "586",
        "blackmail": "586",
        "gyaru": "586",
        "deepthroat": "586",
        "snuff": "586",
        "already uploaded": "586",
        "vomit": "586",
        "moral degeneration": "586",
        "full body tattoo": "586"
    },
    "artists": {
        "shindol": "290"
    },
    "groups": {},
    "languages": {
        "translated": "75K",
        "english": "75K"
    },
    "categories": {
        "manga": "83K"
    },
    "pages": "225"
}
  ```
</details>

### getCodes

  get newest art given tag and frequency

  parameter : 
  
    tag (string)  default : "main"  valid [ any tag, if whitespace exist, replace with "-"]
    
    freq (string) default : "" valid [ "" | "popular-today" | "popular-week" | "popular]
    
  return :
    
    codes (list[string])
    
  example output
    
   ```
   >>> getCodes()
   ['381103', '381114', '381083', '381117', '381001', '381158', '381157', '381156', '381155', '381154', '381153', '381152', '381151', '381150', '381149', '381148', '381147', '381146', '381145', '381144', '381143', '381142', '381141', '381140', '381139', '381138', '381137', '381136', '381135', '381134']
   >>> getCodes("femdom", "popular-week"))
   ['380847', '380745', '380405', '380286', '380280', '380857', '380493', '380830', '379667', '287312', '380808', '292932', '380159', '380333', '366224', '380760', '380742', '380492', '381107', '380124', '379683', '270437', '379397', '380606', '378994']
   
