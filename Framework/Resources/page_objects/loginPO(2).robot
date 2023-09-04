*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${Login Page URL}       https://demo.nopcommerce.com/login?returnUrl=%2F
${Email Input}      //input[@id="Email"]
${Password Input}       //input[@id="Password"]
${Login Button}     //button[text()="Log in"]

*** Keywords ***
Open Login Page
    Open Browser    ${Login Page URL}       firefox

Login Details
    [Arguments]     ${Email}    ${Password}
    Input Text    ${Email Input}    ${Email}
    Input Text    ${Password Input}    ${Password}

Submit Login Details
    Set Window Size    1200    1200
    Scroll Element Into View    ${Login Button}
    Wait Until Element Is Visible    ${Login Button}
    Click Element    ${Login button}

    ${login_successful} =    Run Keyword And Return Status    Page Should Contain    Welcome to our store
    ${login_unsuccessful} =    Run Keyword And Return Status    Page Should Contain    Login was unsuccessful. Please correct the errors and try again.

    Run Keyword If    ${login_successful}    Log To Console    Login Successful
    Run Keyword If    ${login_unsuccessful}    Log To Console    Login Unsuccessful: The credentials provided are incorrect
    Run Keyword Unless    ${login_successful} or ${login_unsuccessful}    Log To Console    Unexpected login result

Close The Browser
    Close All Browsers