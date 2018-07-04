# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC529_539_540()
    
@stepResult(descriptionMsg=u"게임 > 서브메뉴를 확인한다.(서버편성에 따라 달라질 수 있음)")       
def TC529_539_540(): 
#- 실시간 채널 / 인기 / LOL / 게임쿠폰 / 스타크래프트 / 모바일게임 / 기타 / 테마추천
    GAME_TV = (u"실시간 채널", u"LOL", u"스타크래프트", u"게임BJ")        
    #튜플 이용해 실시간TV 상단에 홈버튼, 검색  , GNB 있는지 확인
    for searchingObj in GAME_TV: 
        
        rc, result = DEV1.UIWaitForText(searchingObj, 5000)
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForName")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND
        
        rc = DEV1.UIClickByText(searchingObj)
        if rc != AT_SUCCESS:
            return rc
        
        System.Sleep(1000)
        
    return AT_SUCCESS