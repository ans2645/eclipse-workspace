# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC938()
    
@stepResult(descriptionMsg=u"360도 영상 > 360도 컨텐츠에 해당하는 컨텐츠의 경우 360도 배지 표시되어야 한다.")       
def TC938():
    #육안으로 확인해야함
    DEV1.StoreImage(u"360badge" , 3000)
                
    return AT_SUCCESS