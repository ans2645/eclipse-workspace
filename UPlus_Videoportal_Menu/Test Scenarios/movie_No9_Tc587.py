# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC587()
    
@stepResult(descriptionMsg=u"영화 > 무료 > 배너 클릭 시 각 연결 카테고리로 이동되는지 확인한다.")       
def TC587():
    
    #베너클릭
    rc = DEV1.UIClickByTypeIndex('avwImageView', 9000)
    if rc != AT_SUCCESS:
        return rc
    
    return AT_SUCCESS
    
    