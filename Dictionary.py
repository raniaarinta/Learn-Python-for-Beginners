MonthConvert = {
        
        "Jan":"January",
        "Feb":"February",
        "Mar":"March",
        "Apr":"April",
        "May":"May",
        "Jun":"June",
        "Jul":"July",
        "Aug":"August",
        "Sep":"September",
        "Oct":"Octorber",
        "Nov":"November",
        "Dec":"December",
        
        }
MonthConvertNum = {
        
        1:"January",
        2:"February",
        3:"March",
        4:"April",
        5:"May",
        6:"June",
        7:"July",
        8:"August",
        9:"September",
        10:"Octorber",
        11:"November",
        12:"December",
        
        }
#key
print(MonthConvert["Nov"])
#pass key get fuction
print(MonthConvert.get("Dec"))
print(MonthConvertNum.get("Dec","invalid key"))
print(MonthConvertNum.get(2))