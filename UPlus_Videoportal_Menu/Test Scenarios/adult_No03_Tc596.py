# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    DEV1.StopApp()
    TC596()
    
@stepResult(descriptionMsg=u"19금 > 최신 > 성인잠금 ON 상태일 경우, 청소년관람불가 표시되며 선택 시 비밀번호를 묻는지 확인")       
def TC596():
    rc = DEV1.ClearAppData()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.LauchApp()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.ClearAppDataAgree()
    if rc != AT_SUCCESS:
        return rc

    rc = DEV1.CheckMainDisplayLoaded()
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(1000)
    
    #설정클릭
    rc = DEV1.ClickPersonlSetting()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.CheckPersonalSettingDisplayShown()
    if rc != AT_SUCCESS:
        return rc
    
    
    rc, result = DEV1.UIWaitForName("personal_setting_environment_setting_run", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    
    #환경설정 진입
    rc = DEV1.UIClickByName('personal_setting_environment_setting_run')
    if rc != AT_SUCCESS:
        return rc
    
    #비밀번호 설정 버튼 
    rc, result = DEV1.UIWaitForName("btn_setPwd", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    rc = DEV1.UIClickByName('btn_setPwd')
    if rc != AT_SUCCESS:
        return rc
    
    #비밀번호 입력 창 클릭
    rc, result = DEV1.UIWaitForName("setPwd", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    rc = DEV1.UIClickByName(u"setPwd")
    if rc != AT_SUCCESS:
        return rc
    
    #비밀번호 1회 입력
    rc = DEV1.UIEnterTextByName("setPwd", "1234")
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, "Impossible to enter text")
        
    
    rc, result = DEV1.UIWaitForText(u"확인", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #입력 후 확인
    rc = DEV1.UIClickByText(u"확인")
    if rc != AT_SUCCESS:
        return rc
    
    #2번째 비밀번호 확인 입력 
    rc, result = DEV1.UIWaitForName("setPwd", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #비밀번호 입력 창 클릭
    rc = DEV1.UIClickByName(u"setPwd")
    if rc != AT_SUCCESS:
        return rc
    
    
    #비밀번호 입력
    rc = DEV1.UIEnterTextByName("setPwd", "1234")
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, "Impossible to enter text")
    
    #확인버튼 클릭
    rc = DEV1.UIClickByTypeIndex('avwStaticText', 9003, UITarget.TopWindow)
    if rc != AT_SUCCESS:
        return rc
    
    #올바르게 입력이 완료되면 비밀번호 설정이 완료됨을 알리는 팝업 발생
    for i in range(1,5):
        DEV1.StoreImage("passwordInSucces"+str(i),100)
    
    #성인컨텐츠 잠금 토글 버튼 클릭  
    
    rc, result = DEV1.UIWaitForName("adultConLock", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    rc = DEV1.UIClickByName(u"adultConLock")
    if rc != AT_SUCCESS:
        return rc
    
    
    
    """rc = DEV1.UIClickByTypeIndex('avwToggleButton', 9002, UITarget.TopWindow)
    if rc != AT_SUCCESS:
        return rc""" 
    
    #환경설정 나가기
    DEV1.KeyPressByAlias('back,back')
    
    rc = DEV1.LauchApp()
    if rc != AT_SUCCESS:
        return rc
    
    
    rc = DEV1.CheckMainDisplayLoaded()
    if rc != AT_SUCCESS:
        return rc
    
    #더보기 나타났는지 확인
    rc = DEV1.CheckMoreMenuShown()
    if rc != AT_SUCCESS:
        return rc
    
    #더보기 클릭
    rc = DEV1.ClickMoreMenu()
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(1000)
    
    #19금 메뉴 클릭
    rc = DEV1.Click19Menu()
    if rc != AT_SUCCESS:
        return rc
    
    #19금 메뉴 진입 확인
    rc = DEV1.Check19MenuSubHomeShown()
    if rc != AT_SUCCESS:
        return rc      
    
    rc = DEV1.UIClickByTypeIndex('avwImageView', 9002)
    if rc != AT_SUCCESS:
        return rc
    
    
    rc = DEV1.UIEnterTextByName("checkPwd", "1234")
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, "Impossible to enter text")
        
    rc = DEV1.UIClickByTypeIndex('avwStaticText', 9002, UITarget.TopWindow)
    if rc != AT_SUCCESS:
        return rc 
    
    
    return AT_SUCCESS