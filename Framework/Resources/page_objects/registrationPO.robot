*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${Registration Page URL}    https://automationexercise.com/login
${Username Input}    //input[@data-qa='signup-name']
${Email Input}       //input[@data-qa='signup-email']
${Submit Button}     //button[@data-qa='signup-button']
${Password Input}    //input[@id="password"]
${Firstname Input}   //input[@id="first_name"]
${Lastname Input}    //input[@id="last_name"]
${Address Input}     //input[@id="address1"]
${State Input}       //input[@id="state"]
${City Input}        //input[@id="city"]
${Zipcode Input}     //input[@id="zipcode"]
${Mobile_number Input}  //input[@id="mobile_number"]
${Create account button}  //button[text()="Create Account"]

*** Keywords ***
Open Registration Page
    Open Browser    ${Registration Page URL}    firefox

Fill Registration Form
    [Arguments]   ${Username}   ${Email}    ${Password}    ${Firstname}    ${Lastname}    ${Address}    ${State}    ${City}    ${Zipcode}    ${Mobile_number}
    Input Text    ${Username Input}    ${Username}
    Input Text    ${Email Input}    ${Email}

    Click Element    ${Submit Button}
    ${Submit_Status}=   Run Keyword And Return Status    Page Should Contain    Email Address already exist!
    Run Keyword If    ${Submit_Status}    Log To Console    Email Address already exists
    Run Keyword If    ${Submit_Status}    Fail

    Input Text    ${Password Input}    ${Password}
    Input Text    ${Firstname Input}    ${Firstname}
    Input Text    ${Lastname Input}    ${Lastname}
    Input Text    ${Address Input}    ${Address}
    Input Text    ${State Input}    ${State}
    Input Text    ${City Input}    ${City}
    Input Text    ${Zipcode Input}    ${Zipcode}
    Input Text    ${Mobile_number Input}    ${Mobile_number}

Submit Registration Form
    Click Element    ${Create account button}
    ${registration_successful} =    Run Keyword And Return Status    Page Should Contain    Account Created!

    Run Keyword If    ${registration_successful}    Log To Console    Registration Successfull
    Run Keyword Unless    ${registration_successful}    Log To Console    Unexpected login result


Close The Browser
    Close All Browsers