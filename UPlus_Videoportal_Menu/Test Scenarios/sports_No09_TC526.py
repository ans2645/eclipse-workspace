# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC526()
    
@stepResult(descriptionMsg=u"스포츠 > 골프  > 리스트 영역을 확인- 리스트 선택 시 상세화면으로 이동")
def TC526():
    #리스트 하나 선택 
    rc = DEV1.UIClickByTypeIndex('avwImageView', 9000)
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(2000)
    
    
    DEV1.KeyPressByAlias('back')
    
    return AT_SUCCESS

