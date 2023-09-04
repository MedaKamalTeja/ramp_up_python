*** Settings ***
Resource    ../../Resources/Page_objects/registrationPO(2).robot
Resource    ../../Resources/Variables/registration_variables(2).robot

*** Keywords ***
Register User
    Open Registration Page
    Fill Registration Form    ${Firstname}    ${Lastname}     ${Email}    ${Password}     ${Confirm Password}
    Submit Registration Form
    Close The Browser
