#CRM-APC 阅读笔记
#---------- 数据结构 ----------
Flights={"I1":{"origin":"AAA" ,"scheduled_dep":0,"scheduled_arr":0,"destination":"BBB"},
         "I2":{"origin":"CCC","scheduled_dep":0,"scheduled_arr":0,"destination":"DDD"},
         }
Crews = {"K1": {...}, "K2": {...}}
CrewStrings={"S1":["I1","I2","I3"],
             "S2":["I1","I2","I5"],}
AircraftRotation={"R1":["I1","I2","I3"],
                  "R2":["I1","I2","I5"],}
PasssengerItineraries ={"P1":["I1","I2","I3"],
                       "P2":["I1","I2","I5"],}
NonpropagatedDelay= {"I1":"","I2":""}  # 分钟
#-------------派生数据----------------
#sequence对应的就是CrewString,AircraftRotation,PassengerItineraries
def get_consecutive_pairs(sequence):
    """Set Consecutive flight pairs in crew string s ∈ S,
    Consecutive flight pairs in passenger itinerary p ∈ P,
    Consecutive flight pairs in aircraft rotation r ∈ R
"""
    dic={}
    for i ,j in sequence.items():
         dic[i]=list(zip(j[:-1],j[1:]))
    return dic

