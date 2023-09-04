*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${Registration Page URL}        https://demo.nopcommerce.com/register?returnUrl=%2F
${Firstname Input}      //input[@id="FirstName"]
${Lastname Input}       //input[@id="LastName"]
${Email Input}      //input[@id="Email"]
${Password Input}       //input[@id="Password"]
${Confirm Password Input}       //input[@id="ConfirmPassword"]
${Register Button}      //button[@id="register-button"]

*** Keywords ***
Open Registration Page
    Open Browser    ${Registration Page URL}    firefox

Fill Registration Form
    [Arguments]     ${Firstname}    ${Lastname}     ${Email}    ${Password}     ${Confirm Password}
    Input Text    ${Firstname Input}    ${Firstname}
    Input Text    ${Lastname Input}    ${Lastname}
    Input Text    ${Email Input}    ${Email}
    Set Window Size    1280    1200
    Scroll Element Into View    //strong[text()="Your Password"]
    Wait Until Element Is Visible    //strong[text()="Your Password"]
    Input Text    ${Password Input}    ${Password}
    Input Text    ${Confirm Password Input}    ${Confirm Password}

Submit Registration Form
    Click Element    ${Register Button}
    ${registration_successful} =    Run Keyword And Return Status    Page Should Contain    Your registration completed

    Run Keyword If    ${registration_successful}    Log To Console    Registration Successfull
    Run Keyword Unless    ${registration_successful}    Log To Console    Email already Exists!

Close The Browser
    Close All Browsers