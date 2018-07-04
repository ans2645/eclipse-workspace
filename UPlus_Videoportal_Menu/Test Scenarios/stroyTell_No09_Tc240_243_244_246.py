# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC240_243_244_246()
    
@stepResult(descriptionMsg=u"영상카드 > 스토리텔링 콘텐츠 선택 시 스토리텔링 콘텐츠 타입에 따라 카드형/블로그형 상세화면으로 이동")
def TC240_243_244_246():
    
    #카드 하나 선택
    result = False
    for i in range(0,5):
        rc = DEV1.UIClickByTypeIndex('avwStaticText',9002+i)
        if rc != AT_SUCCESS:
            return rc
    #wifi가 아닌 LTE or 3G 사용 중 외부 연동을 통해 서비스되는 동영상 콘텐츠를 선택 시 데이터 요금안내 팝업을 제공
        data_char = u"데이터 요금안내"
        rc, result = DEV1.UIWaitForText(data_char, 5000)
        if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
            rc = DEV1.UIClickByText(u"확인")
            if rc != AT_SUCCESS:
                return rc
            return rc
        
        if result == False:   # 텍스트가 나타났는지 확인
            pass
        
        
        
        DEV1.KeyPressByAlias('back')
        
    
    return AT_SUCCESS