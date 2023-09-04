*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${Login Page URL}    https://automationexercise.com/login
${Email Input}      //input[@data-qa="login-email"]
${Password Input}       //input[@data-qa="login-password"]
${Login button}     //button[@data-qa="login-button"]

*** Keywords ***
Open Login Page
    Open Browser    ${Login Page URL}       firefox

Login Details
    [Arguments]     ${Email}    ${Password}
    Input Text    ${Email Input}    ${Email}
    Input Text    ${Password Input}    ${Password}

Submit Login Details
    Click Element    ${Login button}
    ${login_successful} =    Run Keyword And Return Status    Page Should Contain    Full-Fledged practice website for Automation Engineers
    ${login_unsuccessful} =    Run Keyword And Return Status    Page Should Contain    Your email or password is incorrect!

    Run Keyword If    ${login_successful}    Log To Console    Login Successful
    Run Keyword If    ${login_unsuccessful}    Log To Console    Login Unsuccessful: The credentials provided are incorrect
    Run Keyword Unless    ${login_successful} or ${login_unsuccessful}    Log To Console    Unexpected login result

Close The Browser
    Close All Browsers