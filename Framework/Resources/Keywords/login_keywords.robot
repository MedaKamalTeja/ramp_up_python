*** Settings ***
Resource    ../../Resources/Page_objects/loginPO.robot
Resource    ../../Resources/Variables/login_variables.robot

*** Keywords ***
Login User
    Open Login Page
    Login Details    ${Email}    ${Password}
    Submit Login Details
    Close The Browser

