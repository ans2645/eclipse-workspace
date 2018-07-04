# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC574_577_578()
    
@stepResult(descriptionMsg=u"해외시리즈 > 최신,인기 > 서브 메뉴 영역을 확인한다.(서버편성에 따라 달라질 수 있음)")       
def TC574_577_578():
    
    #- HBO, 최신/인기, 미드, 영드, 일드, 중드, 무협/사극, 기타

    #- 좌우 Flicking 가능, tap 시 선택한 영역으로 이동"
    
    rc, result = DEV1.UIWaitForText(u"무료", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    rc = DEV1.UIClickByText(u"무료")
    if rc != AT_SUCCESS:
        return rc
    
    
    #정렬버튼 찾기
    rc, result = DEV1.UIWaitForName("rlBottomButtonLayout", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #정렬버튼 눌러보기
    rc = DEV1.UIClickByName('rlBottomButtonLayout')
    if rc != AT_SUCCESS:
        return rc
    
    
    rc, result = DEV1.UIWaitForName("llTopLayout", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    
    #포스터 클릭
    rc = DEV1.UIClickByTypeIndex('avwSubWindow', 9020)
    if rc != AT_SUCCESS:
        return rc
    
    rc, result = DEV1.UIWaitForName("backBtn", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    
    rc = DEV1.UIClickByName('backBtn')
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(3000)
    
    rc, result = DEV1.UIWaitForText(u"미드/영드", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    rc = DEV1.UIClickByText(u"미드/영드")
    if rc != AT_SUCCESS:
        return rc
    
    #정렬버튼 찾기
    rc, result = DEV1.UIWaitForName("rlBottomButtonLayout", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #정렬버튼 눌러보기
    rc = DEV1.UIClickByName('rlBottomButtonLayout')
    if rc != AT_SUCCESS:
        return rc
    
    
    System.Sleep(3000)
    
    rc, result = DEV1.UIWaitForName("llTopLayout", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    
    System.Sleep(3000)
    
    #포스터 클릭
    rc = DEV1.UIClickByTypeIndex('avwSubWindow', 9037)
    if rc != AT_SUCCESS:
        return rc
    
    
    rc, result = DEV1.UIWaitForName("backBtn", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    
    rc = DEV1.UIClickByName('backBtn')
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(3000)
    
    rc, result = DEV1.UIWaitForText(u"중드", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    rc = DEV1.UIClickByText(u"중드")
    if rc != AT_SUCCESS:
        return rc
    
    
    System.Sleep(3000)
    
    #정렬버튼 찾기
    rc, result = DEV1.UIWaitForName("rlBottomButtonLayout", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    System.Sleep(3000)
    
    #정렬버튼 눌러보기
    rc = DEV1.UIClickByName('rlBottomButtonLayout')
    if rc != AT_SUCCESS:
        return rc
    
    
    rc, result = DEV1.UIWaitForName("llTopLayout", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    System.Sleep(3000)
    
    
    #포스터 클릭
    rc = DEV1.UIClickByTypeIndex('avwSubWindow', 9037)
    if rc != AT_SUCCESS:
        return rc
    
    
    rc, result = DEV1.UIWaitForName("backBtn", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    
    rc = DEV1.UIClickByName('backBtn')
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(3000)
    
    rc = DEV1.ScrollRight("avwObject", 9001)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
    
    System.Sleep(3000)
    
    rc, result = DEV1.UIWaitForText(u"일드", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    rc = DEV1.UIClickByText(u"일드")
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(3000)
    
    
    #정렬버튼 찾기
    rc, result = DEV1.UIWaitForName("rlBottomButtonLayout", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #정렬버튼 눌러보기
    rc = DEV1.UIClickByName('rlBottomButtonLayout')
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(3000)
    
    rc, result = DEV1.UIWaitForName("llTopLayout", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    System.Sleep(3000)
    
    
    #포스터 클릭
    rc = DEV1.UIClickByTypeIndex('avwSubWindow', 9037)
    if rc != AT_SUCCESS:
        return rc
    
    
    rc, result = DEV1.UIWaitForName("backBtn", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    
    rc = DEV1.UIClickByName('backBtn')
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(3000)
    
    rc, result = DEV1.UIWaitForText(u"기타국가", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    rc = DEV1.UIClickByText(u"기타국가")
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(3000)
    
    
    #정렬버튼 찾기
    rc, result = DEV1.UIWaitForName("rlBottomButtonLayout", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #정렬버튼 눌러보기
    rc = DEV1.UIClickByName('rlBottomButtonLayout')
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(3000)
    
    
    rc, result = DEV1.UIWaitForName("llTopLayout", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    
    System.Sleep(3000)
    
    #포스터 클릭
    rc = DEV1.UIClickByTypeIndex('avwSubWindow', 9020)
    if rc != AT_SUCCESS:
        return rc
    
    
    rc, result = DEV1.UIWaitForName("backBtn", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    
    rc = DEV1.UIClickByName('backBtn')
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(3000)
    
    rc, result = DEV1.UIWaitForText(u"채널별", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    rc = DEV1.UIClickByText(u"채널별")
    if rc != AT_SUCCESS:
        return rc
    
    
    System.Sleep(3000)
    
    #정렬버튼 찾기
    rc, result = DEV1.UIWaitForName("rlBottomButtonLayout", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #정렬버튼 눌러보기
    rc = DEV1.UIClickByName('rlBottomButtonLayout')
    if rc != AT_SUCCESS:
        return rc
    
    
    System.Sleep(3000)
    
    rc, result = DEV1.UIWaitForName("llTopLayout", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    System.Sleep(3000)
    
    
    #포스터 클릭
    rc = DEV1.UIClickByTypeIndex('avwSubWindow', 9037)
    if rc != AT_SUCCESS:
        return rc
    
    rc, result = DEV1.UIWaitForName("backBtn", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    
    rc = DEV1.UIClickByName('backBtn')
    if rc != AT_SUCCESS:
        return rc
    
    return AT_SUCCESS

