# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC2037()
    
@stepResult(descriptionMsg=u"아프리카TV > 실시간 개인 방송 > Live icon > 리스트에 LIVE아이콘이 노출되는지 확인")       
def TC2037():
    
    #live icon 찾기
    rc, result = DEV1.UIGetObjectByTypeIndex('avwObject', 9032)
    if rc != AT_SUCCESS:
        return rc
    
    
    return AT_SUCCESS
    
    
    