*** Settings ***
Resource    ../../Resources/Page_objects/registrationPO.robot
Resource    ../../Resources/Variables/registration_variables.robot

*** Keywords ***
Register User
    Open Registration Page
    Fill Registration Form    ${Username}   ${Email}    ${Password}    ${Firstname}    ${Lastname}    ${Address}    ${State}    ${City}    ${Zipcode}    ${Mobile_number}
    Submit Registration Form
    Close The Browser
