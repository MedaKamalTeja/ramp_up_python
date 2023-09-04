*** Settings ***
Resource    ../../Resources/Page_objects/loginPO(2).robot
Resource    ../../Resources/Variables/login_variables(2).robot

*** Keywords ***
Login User
    Open Login Page
    Login Details    ${Email}    ${Password}
    Submit Login Details
    Close The Browser
