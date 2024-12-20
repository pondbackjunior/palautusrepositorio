*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kaapo456
    Set Password Confirmation  kaapo456
    Submit Credentials
    Register Should Fail With Message  Username should be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  kaapo
    Set Password  kaap0
    Set Password Confirmation  kaap0
    Submit Credentials
    Register Should Fail With Message  Password should be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  kaapo
    Set Password  kaapoabc
    Set Password Confirmation  kaapoabc
    Submit Credentials
    Register Should Fail With Message  Password cannot contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kaapo
    Set Password  kaapo123
    Set Password Confirmation  kaapo456
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Go To Register Page
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username is already in use

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Go To Ohtu Page
    Click Button  Logout
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle
    Set Password  kalle
    Set Password Confirmation  kalle
    Submit Credentials
    Go To Login Page
    Set Username  kalle
    Set Password  kalle
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page