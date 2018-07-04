# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC532()
    
@stepResult(descriptionMsg=u"게임 > 채널명, 프로그레스 바, 프로그램 명, 편성시간, 스틸컷, 시청률")       
def TC532():
    HELP_TEXT = ("imageView1","imgChLogo","textProgramName","textProgramTime","prgbChannel","textRating")
    for searchingObj in HELP_TEXT: 
        rc, result = DEV1.UIWaitForName(searchingObj, 500)
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForName")
            return rc
        
    System.Sleep(5000)
    
#- 채널 리스트 선택 시 해당 채널 플레이 영역에 재생"

    rc = DEV1.UIClickByTypeIndex('avwImageView', 9006)
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(15000)
    
    DEV1.KeyPressByAlias('back')
    
    return AT_SUCCESS



    
