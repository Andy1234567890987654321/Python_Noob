"""
請用以下list完成之前的果汁功能
juices_list=["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]
"""
juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "可樂", "系統關閉"]
while True:
    applebananaorange = int(input('請給我錢!'))
    if applebananaorange >= len(juices_list):
        break
    else:
        print(juices_list[applebananaorange-1])
