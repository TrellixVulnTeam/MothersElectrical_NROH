from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Product_detail,News,Retrailer_Detail,OrderDetail,clientMoblie
from django.contrib import messages
from datetime import datetime
import random
import string
import requests


import json 
# ----for sending email---
import os
import smtplib
import imghdr
from email.message import EmailMessage
# ----------login---
from django.contrib.auth import authenticate, logout, login # ---for user login logout---# ---for user login logout---

BLOG_POSTS_PER_PAGE = 2
EMAIL_ADDRESS = "rahultest445@gmail.com"
EMAIL_PASSWORD = "Test#123"
oneTimePassword='xxx'
url = "https://www.fast2sms.com/dev/bulk" #---fast2sms url

# -----------Generate alphaNumeric string
def get_random_alphanumeric_string(letters_count, digits_count):
    sample_str = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    sample_str += ''.join((random.choice(string.digits) for i in range(digits_count)))

    # Convert string to list and shuffle it to mix letters and digits
    sample_list = list(sample_str)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string
# Create your views here.
# ---------------------------------
def index(request):
    GetNews=News.objects.all()
    print(GetNews)
    return render(request,'index.html',{'AllNews':GetNews})

# ---------------------------------
def contactus(request):

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        print(f'{name}--{email}--{phone}--{message}')

        if len(name)<2 or len(email)<5 or len(phone)<10 or len(message)<25:
            messages.error(request,'Please Enter the Valid details and fill correclty')
        else:
            messages.success(request,'Your information successfuly sent. we will contact you very soon.! Thank You')
            
            # ---Sendding Email-----
            msg = EmailMessage()
            msg['Subject'] = f"Contact Request from {name}"
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = 'rahultest445@gmail.com'
            msg.set_content(f"\n{message}\n\n From {email}\nMoblie number{phone}")
            msg.add_alternative("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1" name="viewport">
    <meta name="x-apple-disable-message-reformatting">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta content="telephone=no" name="format-detection">
    
    <title></title>
   
    <style type="text/css">
 
#outlook a {{
    padding: 0;
}}

.ExternalClass {{
    width: 100%;
}}

.ExternalClass,
.ExternalClass p,
.ExternalClass span,
.ExternalClass font,
.ExternalClass td,
.ExternalClass div {{
    line-height: 100%;
}}

.es-button {{
    mso-style-priority: 100 !important;
    text-decoration: none !important;
}}

a[x-apple-data-detectors] {{
    color: inherit !important;
    text-decoration: none !important;
    font-size: inherit !important;
    font-family: inherit !important;
    font-weight: inherit !important;
    line-height: inherit !important;
}}

.es-desk-hidden {{
    display: none;
    float: left;
    overflow: hidden;
    width: 0;
    max-height: 0;
    line-height: 0;
    mso-hide: all;
}}


s {{
    text-decoration: line-through;
}}

html,
body {{
    width: 100%;
    font-family: arial, 'helvetica neue', helvetica, sans-serif;
    -webkit-text-size-adjust: 100%;
    -ms-text-size-adjust: 100%;
}}

table {{
    mso-table-lspace: 0pt;
    mso-table-rspace: 0pt;
    border-collapse: collapse;
    border-spacing: 0px;
}}

table td,
html,
body,
.es-wrapper {{
    padding: 0;
    Margin: 0;
}}

.es-content,
.es-header,{{
.es-footer {{
    table-layout: fixed !important;
    width: 100%;
}}

img {{
    display: block;
    border: 0;
    outline: none;
    text-decoration: none;
    -ms-interpolation-mode: bicubic;
}}

table tr {{
    border-collapse: collapse;
}}

p,
hr {{
    Margin: 0;
}}

h1,
h2,
h3,
h4,
h5 {{
    Margin: 0;
    line-height: 120%;
    mso-line-height-rule: exactly;
    font-family: arial, 'helvetica neue', helvetica, sans-serif;
}}

p,
ul li,
ol li,
a {{
    -webkit-text-size-adjust: none;
    -ms-text-size-adjust: none;
    mso-line-height-rule: exactly;
}}

.es-left {{
    float: left;
}}

.es-right {{
    float: right;
}}

.es-p5 {{
    padding: 5px;
}}

.es-p5t {{
    padding-top: 5px;
}}

.es-p5b {{
    padding-bottom: 5px;
}}

.es-p5l {{
    padding-left: 5px;
}}

.es-p5r {{
    padding-right: 5px;
}}

.es-p10 {{
    padding: 10px;
}}

.es-p10t {{
    padding-top: 10px;
}}

.es-p10b {{
    padding-bottom: 10px;
}}

.es-p10l {{
    padding-left: 10px;
}}

.es-p10r {{
    padding-right: 10px;
}}

.es-p15 {{
    padding: 15px;
}}

.es-p15t {{
    padding-top: 15px;
}}

.es-p15b {{
    padding-bottom: 15px;
}}

.es-p15l {{
    padding-left: 15px;
}}

.es-p15r {{
    padding-right: 15px;
}}

.es-p20 {{
    padding: 20px;
}}

.es-p20t {{
    padding-top: 20px;
}}

.es-p20b {{
    padding-bottom: 20px;
}}

.es-p20l {{
    padding-left: 20px;
}}

.es-p20r {{
    padding-right: 20px;
}}

.es-p25 {{
    padding: 25px;
}}

.es-p25t {{
    padding-top: 25px;
}}

.es-p25b {{
    padding-bottom: 25px;
}}

.es-p25l {{
    padding-left: 25px;
}}

.es-p25r {{
    padding-right: 25px;
}}

.es-p30 {{
    padding: 30px;
}}

.es-p30t {{
    padding-top: 30px;
}}

.es-p30b {{
    padding-bottom: 30px;
}}

.es-p30l {{
    padding-left: 30px;
}}

.es-p30r {{
    padding-right: 30px;
}}

.es-p35 {{
    padding: 35px;
}}

.es-p35t {{
    padding-top: 35px;
}}

.es-p35b {{
    padding-bottom: 35px;
}}

.es-p35l {{
    padding-left: 35px;
}}

.es-p35r {{
    padding-right: 35px;
}}

.es-p40 {{
    padding: 40px;
}}

.es-p40t {{
    padding-top: 40px;
}}

.es-p40b {{
    padding-bottom: 40px;
}}

.es-p40l {{
    padding-left: 40px;
}}

.es-p40r {{
    padding-right: 40px;
}}

.es-menu td{{
    border: 0;
}}

.es-menu td a img {{
    display: inline-block !important;
}}


a {{
    font-family: arial, 'helvetica neue', helvetica, sans-serif;
    font-size: 14px;
    text-decoration: underline;
}}

h1 {{
    font-size: 30px;
    font-style: normal;
    font-weight: normal;
    color: #333333;
}}

h1 a {{
    font-size: 30px;
}}

h2 {{
    font-style: normal;
    font-weight: normal;
    color: #9E9E9E;
    font-size: 25px;;
}}

h2 a {{
    font-size: 24px;
}}

h3 {{
    font-size: 20px;
    font-style: normal;
    font-weight: normal;
    color: #333333;
}}

h3 a {{
    font-size: 20px;
}}

p,
ul li,
ol li {{
    font-size: 14px;
    font-family: arial, 'helvetica neue', helvetica, sans-serif;
    line-height: 150%;
}}

ul li,
ol li {{
    Margin-bottom: 15px;
}}

.es-menu td a {{
    text-decoration: none;
    display: block;
}}

.es-wrapper {{
    width: 100%;
    height: 100%;
    background-repeat: repeat;
    background-position: center top;
}}

.es-wrapper-color {{
    background-color: #ffffff;
}}

.es-content-body {{
    background-color: #ffffff;
}}

.es-content-body p,
.es-content-body ul li,
.es-content-body ol li {{
    color: #333333;
}}

.es-content-body a {{
    color: #ee6c6d;
}}

.es-header {{
    background-color: transparent;
    background-repeat: repeat;
    background-position: center top;
}}

.es-header-body {{
    background-color: transparent;
}}

.es-header-body p,
.es-header-body ul li,
.es-header-body ol li {{
    color: #333333;
    font-size: 14px;
}}

.es-header-body a {{
    color: #ee6c6d;
    font-size: 14px;
}}

.es-footer {{
    background-color: transparent;
    background-repeat: repeat;
    background-position: center top;
}}

.es-footer-body {{
    background-color: #f7f7f7;
}}

.es-footer-body p,
.es-footer-body ul li,
.es-footer-body ol li {{
    color: #333333;
    font-size: 14px;
}}

.es-footer-body a {{
    color: #333333;
    font-size: 14px;
}}

.es-infoblock,
.es-infoblock p,
.es-infoblock ul li,
.es-infoblock ol li {{
    line-height: 120%;
    font-size: 12px;
    color: #cccccc;
}}

.es-infoblock a {{
    font-size: 12px;
    color: #cccccc;
}}

a.es-button {{
    border-style: solid;
    border-color:#022c5a;
    border-width: 6px 25px 6px 25px;
    display: inline-block;
    background: #022c5a;
    border-radius: 20px;
    font-size: 20px;
    font-family: helvetica, 'helvetica neue', arial, verdana, sans-serif;
    font-weight: normal;
    font-style: normal;
    line-height: 120%;
    color: #efefef;
    text-decoration: none;
    width: auto;
    text-align: center;
}}

.es-button-border {{
    border-style: solid solid solid solid;
    border-color: #474745 #474745 #474745 #474745;
    background: #474745;
    border-width: 0px 0px 0px 0px;
    display: inline-block;
    border-radius: 20px;
    width: auto;
}}


@media only screen and (max-width: 600px) {{

    p,
    ul li,
    ol li,
    a {{
        font-size: 16px !important;
        line-height: 150% !important;
    }}

    h1 {{
        font-size: 30px !important;
        text-align: center;
        line-height: 120% !important;
    }}

    h2 {{
        font-size: 26px !important;
        text-align: center;
        line-height: 120% !important;
    }}

    h3 {{
        font-size: 20px !important;
        text-align: center;
        line-height: 120% !important;
    }}

    h1 a {{
        font-size: 30px !important;
    }}

    h2 a {{
        font-size: 26px !important;
    }}

    h3 a {{
        font-size: 20px !important;
    }}

    .es-menu td a {{
        font-size: 16px !important;
    }}

    .es-header-body p,
    .es-header-body ul li,
    .es-header-body ol li,
    .es-header-body a {{
        font-size: 16px !important;
    }}

    .es-footer-body p,
    .es-footer-body ul li,
    .es-footer-body ol li,
    .es-footer-body a {{
        font-size: 16px !important;
    }}

    .es-infoblock p,
    .es-infoblock ul li,
    .es-infoblock ol li,
    .es-infoblock a {{
        font-size: 12px !important;
    }}

    *[class="gmail-fix"] {{
        display: none !important;
    }}

    .es-m-txt-c,
    .es-m-txt-c h1,
    .es-m-txt-c h2,
    .es-m-txt-c h3 {{
        text-align: center !important;
        
    }}

    .es-m-txt-r,
    .es-m-txt-r h1,
    .es-m-txt-r h2,
    .es-m-txt-r h3 {{
        text-align: right !important;
    }}

    .es-m-txt-l,
    .es-m-txt-l h1,
    .es-m-txt-l h2,
    .es-m-txt-l h3 {{
        text-align: left !important;
    }}

    .es-m-txt-r img,
    .es-m-txt-c img,
    .es-m-txt-l img {{
        display: inline !important;
    }}

    .es-button-border {{
        display: inline-block !important;
    }}

    a.es-button {{
        font-size: 20px !important;
        display: inline-block !important;
        border-width: 6px 25px 6px 25px !important;
    }}

    .es-btn-fw {{
        border-width: 10px 0px !important;
        text-align: center !important;
    }}

    .es-adaptive table,
    .es-btn-fw,
    .es-btn-fw-brdr,
    .es-left,
    .es-right {{
        width: 100% !important;
    }}

    .es-content table,
    .es-header table,
    .es-footer table,
    .es-content,
    .es-footer,
    .es-header {{
        width: 100% !important;
        max-width: 600px !important;
    }}

    .es-adapt-td{{
        display: block !important;
        width: 100% !important;
    }}

    .adapt-img {{
        width: 100% !important;
        height: auto !important;
    }}

    .es-m-p0 {{
        padding: 0px !important;
    }}

    .es-m-p0r {{
        padding-right: 0px !important;
    }}

    .es-m-p0l {{
        padding-left: 0px !important;
    }}

    .es-m-p0t {{
        padding-top: 0px !important;
    }}

    .es-m-p0b {{
        padding-bottom: 0 !important;
    }}

    .es-m-p20b {{
        padding-bottom: 20px !important;
    }}

    .es-mobile-hidden,
    .es-hidden {{
        display: none !important;
    }}

    tr.es-desk-hidden,
    td.es-desk-hidden,
    table.es-desk-hidden {{
        display: table-row !important;
        width: auto !important;
        overflow: visible !important;
        float: none !important;
        max-height: inherit !important;
        line-height: inherit !important;
    }}

    .es-desk-menu-hidden {{
        display: table-cell !important;
    }}

    table.es-table-not-adapt,
    .esd-block-html table {{
        width: auto !important;
    }}

    table.es-social {{
        display: inline-block !important;
    }}

    table.es-social td {{
        display: inline-block !important;
    }}
}}


    </style>
   
</head>

<body>
    <div class="es-wrapper-color">
        <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
            <tbody>
                <tr>
                    <td class="esd-email-paddings" valign="top">
                        <table class="es-content" align="center" cellspacing="0" cellpadding="0">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table class="es-content-body" align="center" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p20t" esd-custom-block-id="8430" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" align="center" width="600" valign="top">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image es-p20r es-p20l" align="center" style="font-size:0"><a target="_blank"><img class="adapt-img" src="cid:Logo.jpg" alt="Image" style="display: block;" title="Image" width="180"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content" align="center" cellspacing="0" cellpadding="0">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table class="es-content-body" style="border-left:1px solid transparent;border-right:1px solid transparent;border-top:1px solid transparent;border-bottom:1px solid transparent;" align="center" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p20t es-p40b es-p40r es-p40l" esd-custom-block-id="8537" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" align="left" width="518">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-m-txt-c" align="center">
                                                                                        <h2>Hey MothersElectrical<br></h2>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-m-txt-c" align="center">
                                                                                        <h3><strong><em>{fname}
                                                                                        </em></strong> message you,He/She wants contact you. !!<br></h3>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-m-txt-c es-p15t" align="center">
                                                                                        <p>{fmessage}</p>
                                                                                    </td>
                                                                                </tr>
                                                                                <br/>
                                                                                <tr>
                                                                                    <td class="esd-block-button es-p20t es-p15b es-p10r es-p10l" align="center">
                                                                                        <p><strong>Regards<em>
                                                                                        </em> {femail}, {fphone}</strong></p>
                                                                                        <br/>
                                                                                        <!-- <span class="es-button-border"><a href="https://boski.app/" class="es-button" target="_blank">Go to Boski</a></span></td> -->
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table cellpadding="0" cellspacing="0" class="es-footer" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" esd-custom-block-id="8442" style="background-color: #f7f7f7;" bgcolor="#f7f7f7" align="center">
                                        <table class="es-footer-body" width="600" cellspacing="0" cellpadding="0" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p20t es-p20b es-p20r es-p20l" esd-general-paddings-checked="false" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="560" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-p10b" align="center">
                                                                                        <p style="line-height: 150%;"><strong>This mail only for MothersElectrical Owner.</strong></p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-p10t es-p10b" align="center">
                                                                                        <p>© MothersElectrical 2020<br></p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    <div style="position: absolute; left: -9999px; top: -9999px; margin: 0px;"></div>
</body>
</html>""".format(fname=name, fmessage=message,fphone=phone,femail=email), subtype='html')
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
    return render(request,'contactus.html')


# ---------------------------------
def aboutus(request):
    return render(request,'aboutus.html')

# ---------------------------------
def Type(request,type):
    return render(request,'Type.html',{'Type':type})

# ---------------------------------
def product(request,category,company):
    GetProd=Product_detail.objects.filter(p_company=company,p_category=category)
    return render(request,'product.html',{'Products':GetProd,'Category':category})

def AllProduct(request,type):
    GetProd=Product_detail.objects.filter(p_type=type)
    return render(request,'product.html',{'Products':GetProd,'Type':type})

def productDetail(request,id):
    GetProd=Product_detail.objects.filter(p_id=id)
    return render(request,'ProductDetail.html',{'Product':GetProd[0]})

# ------------HandleLogin------------------
def retailers(request):
    GetRetrailer=Retrailer_Detail.objects.all()
    if request.method=="POST":
        loginusername=request.POST['username']
        loginpassword=request.POST['password']
        myuser=authenticate(username=loginusername,password=loginpassword)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"You are Successfully Login")
           
            return redirect('wretrailers')
        else:
            messages.error(request,"Invalid credentials..! Please check your detials and Try Again")
            return redirect('wretrailers')
    print(GetRetrailer)
    return render(request,'retailer.html',{"Retrailers":GetRetrailer})

# ------------HandleLogout------------------
def handleLogout(request):
    if request.method=="POST":
        logout(request)
        messages.success(request,"You are Successfully LOGOUT...! Thanks For Coming")
        return redirect('wretrailers')
    else:
        return HttpResponse("Logout page")


#------------------Checkout----------------
def checkout(request):
    isMoblieVerified=False
    global oneTimePassword
    if request.method=="POST" :
        phone=request.POST.get('phone')
        phoneOTP=request.POST.get('phoneOTP')
        print(phone, phoneOTP)
        if phoneOTP==None:
            userMoblieNumber=phone
            getClients=clientMoblie.objects.filter(clientMoblieNumber=phone)
            
            if len(getClients)==0:
                print('number save in db')
                saveMoblie=clientMoblie(clientMoblieNumber=userMoblieNumber)
                saveMoblie.save()

            # write a code to send a OTP msg to customer moblies
            oneTimePassword=get_random_alphanumeric_string(5, 3)
            # payload = "sender_id=MEOTP&language=english&route=qt&numbers="+userMoblieNumber+"&message=36259&variables={#BB#}&variables_values="+oneTimePassword+""
            # print(payload)
            # headers = {
            #             'authorization': "ZnmqBLXuWcHiG8jSCJ95do2bQ06p4R3k7tAFIaNMgvsP1wVhfDHER3mgUcbWXyzjMr6weJ250qOdZuf4", #---- api authorization key
            #             'cache-control': "no-cache",
            #             'content-type': "application/x-www-form-urlencoded"
            #              }
            # response = requests.request("POST", url, data=payload, headers=headers)
            # responseJson=json.loads(response.text)
            msgTag="success"
            msg=f"OTP(One Time Password is successfully send on this {phone}"
            # if responseJson['message'][0]!='Message sent successfully':
            #     msgTag='error'
            #     msg=f"Something is wrong, Please retry after sometime"
           
            return JsonResponse({"message":msg,'otp':oneTimePassword,"msgTag":msgTag})

        else:
            print(oneTimePassword)
            if phoneOTP==oneTimePassword:
                 isMoblieVerified=True
                 msgTag='success'
                 msg=f"OTP(One Time Password is Successfully Verified {phone}"
            else:
                 msgTag='error'
                 msg=f"You enter wrong OTP(One Time Password),Please enter carefully"
           
            return JsonResponse({"isMoblieVerified":isMoblieVerified,"message":msg,"msgTag":msgTag})


    return render(request,'checkout.html',{"isMoblieVerified":isMoblieVerified})

# ---------------------PlacedOrder-----------
def placedOrder(request):
    if request.method=="POST":
        clientOrder=request.POST.get('bookedOrder')
        order_TotalPrice=request.POST.get('orderTotalPrice')
        clientName=request.POST.get('clientName')
        clientMoblie=request.POST.get('clientMoblie')
        clientAddress1=request.POST.get('clientAddress1')
        clientAddress2=request.POST.get('clientAddress2')
        clientState=request.POST.get('clientState')
        clientCity=request.POST.get('clientCity')
        clientZip=request.POST.get('clientZip')
        clientEmail=request.POST.get('clientEmail')
        clientAltMoblie=request.POST.get('clientAltMoblie')
        orderDate=datetime.now()

        order=OrderDetail(order_Items=clientOrder,order_Total=order_TotalPrice,c_Name=clientName,c_Moblie=clientMoblie,c_AltMoblie=clientAltMoblie,c_Address=clientAddress1,c_Address2=clientAddress2,
        c_Email=clientEmail,c_State=clientState,c_City=clientCity,c_Zip=clientZip,Date=orderDate)
        order.save()

        getBookedOdr=OrderDetail.objects.latest('order_id')
        booked_order_items=json.loads(getBookedOdr.order_Items)
        print('line 944',booked_order_items)
        print('line 995', type(booked_order_items))
        orderTable=''
        serialNo=0
        for key,value in booked_order_items.items():
            serialNo=serialNo+1
            price=value['price']
            orderTable=orderTable+f"""<tr>
                    <th scope='row'>{serialNo}</th>
                    <td>{value['name']}</td>
                    <td>{value['price']}</td>
                    <td{value['qty']}</td>
                    <td><span id='prefix' class='font-weight-bold'>&#x20b9;
                    </span>{value['qty']*price}</td>
                  </tr>"""
        if getBookedOdr.order_id!=None:
            msg = EmailMessage()
            msg['Subject'] = f"Successfully orderm booked from MothersElectrical"
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = getBookedOdr.c_Email
            msg.set_content(f"Order Successfully Booked")
            msg.add_alternative("""<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
        integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous" />

    <title>Hello, world!</title>
</head>
<style>
    .banner_FirstWord {{
        color: #d20909fa;
        font-size: 20px;
        font-weight: 700;
    }}

    .banner_SecondWord {{
        color: black;
        font-size: 20px;
        font-weight: 700;
    }}

    .company_Logo {{
        height: 120px;
        width: 170px;
    }}
</style>

<body>
    <div class="container">
        <div class="row bg-light mt-2 py-2">
            <div class="col">
                <span class="banner_FirstWord">Mothers</span><span class="banner_SecondWord">Electrical</span>
            </div>
        </div>
       
    <div class="row mt-3">
        <div class="col-md-10 col-xs-12 offset-md-1">
            <h4>#Your Orders</h4>
        
            <table class="table table-sm">
                <thead>
                  <tr>
                    <th scope="col">S.no#</th>
                    <th scope="col">Product</th>
                    <th scope="col">Rate/Qty</th>
                    <th scope="col">Qty</th>
                    <th scope="col">Amount</th>
                  </tr>
                </thead>
                <tbody>
                  {orderTable}
                </tbody>
              </table>
        </div>
    </div>
    <hr/>
        <div class="row">
            <div class="offset-lg-1 offset-md-1 offset-sm-1 offset-xs-1  col-lg-5 col-md-5 col-sm-10 col-xs-10">
                <h4 class="bg-light">#Recipient</h4>
                <p>{Name} <br/>
                    {Address} <br/>
                   {Address2} <br/>
                    {Zip},{State}
                    +91-{Moblie} <br/>
                    +91-{AltMoblie} <br/>
                    

                </p>
            </div>
            <div class="col-lg-5 col-md-5 col-sm-10 col-xs-10">
                <h4 class="bg-light">#Total Amount</h4>
               <div class="row">
                   <div class="col">Due Amount </div>
                   <div class="col"><span id="prefix" class="font-weight-bold">&#x20b9;
                </span>{TotalAmount}.00</div>
               </div>
               <div class="row">
                <div class="col">Date </div>
                <div class="col"><span id="prefix" class="font-weight-bold">&#x20b9;
             </span>{Date}</div>
               </div>
            </div>
        </div>
        -<div class="row my-3 ">
            <div class="col text-center ">
                <h3>Thank you for your order</h3>
                I hope your shoping experienceis good with us. If you have any suggestion or feedback please reply us.
            </div>
        </div>
        <hr/>
        <div class="row bg-light my-4 pb-5">
            <div class="col text-center">
                <span class="banner_FirstWord">Mothers</span><span class="banner_SecondWord">Electrical</span>
                <p class="my-0"><em> electricalmothers@gmail.com</em></p>
                <p class="my-0"> Shop No. :- 7, New Market,
                    Hathua Road Mirganj (841438)
                    Phone: +91 8193945463
                    Business Number: +91 8193945463 </p>

            </div>
        </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
        integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"
        integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN"
        crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"
        integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV"
        crossorigin="anonymous"></script>
</body>

</html>""".format(Name=getBookedOdr.c_Name,
Moblie=getBookedOdr.c_Moblie,
            AltMoblie=getBookedOdr.c_AltMoblie,
            Address=getBookedOdr.c_Address,
            Address2=getBookedOdr.c_Address,
            Email=getBookedOdr.c_Email,
            State=getBookedOdr.c_State,
            City=getBookedOdr.c_City,  
            Zip=getBookedOdr.c_Zip,
            Date=getBookedOdr.Date,
            orderTable=orderTable,          
            TotalAmount=order_TotalPrice), 

subtype='html')
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)

        DetailForInvoice={
            'c_Name':getBookedOdr.c_Name,
            'c_Moblie':getBookedOdr.c_Moblie,
            'c_AltMoblie':getBookedOdr.c_AltMoblie,
            'c_Address':getBookedOdr.c_Address,
            'c_Address2':getBookedOdr.c_Address,
            'c_Email':getBookedOdr.c_Email,
            'c_State':getBookedOdr.c_State,
            'c_City':getBookedOdr.c_City,  
            'c_Zip':getBookedOdr.c_Zip,
            'Date':getBookedOdr.Date,
            'order_Total':getBookedOdr.order_Total   
             }
        return render(request,'placedOrder.html',{'TempInvoice':DetailForInvoice,'order_items':booked_order_items,'totalprice':order_TotalPrice})

    return render(request,'checkout.html')

    