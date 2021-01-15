function indexPage() {
    window.location.href = "/index/";
}
function test(obj) {
    //对电子邮件的验证
    var myreg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
    if (!myreg.test(obj)) {
        return 0;
    }
    else {
        return 1;
    }
}
window.onload = function () {
    $("#loginPwd").focus(function () {
        $("#loginPwd").css("background-color", "#FFFFCC");
    });
    $("#loginPwd").blur(function () {
        var upassword = $("#loginPwd").val();
        $("#loginPwd").css("background-color", "white");
        if (upassword.length > 5 && upassword.length < 17) {
            //        $("#userpasswordRight").show();
            $("#userpasswordError").hide();
        } else {
            //        $("#userpasswordRight").hide();
            $("#userpasswordError").show();
        }
    });
}


function doButton() {
    var uName = document.getElementById("uName");
    var uPwd = document.getElementById("loginPwd"),
        u_cPwd = document.getElementById("c_loginPwd"),
        uEmail = document.getElementById("uEmail"),
        userName = document.getElementById("userName"),
        uPhone = document.getElementById("uPhone");
    var uAddress = document.getElementById("uAddress");
    var admitRule = document.getElementById("admitRule");

    if (admitRule.checked == false) {
        alert("请先同意本条款")
        // console.log(uName.value,uPwd.value,u_cPwd.value,sfd[index].value,identy,userName.value,identId.value,uEmail.value,uType[index1].value)
    } else {
        if (uName.value && uPwd.value && u_cPwd.value && uEmail.value && uPhone.value
            && uAddress.value) {
            if (uPwd.value.length > 5 && uPwd.value.length < 17) {
                if (test(uEmail.value) == 1) {
                    if (uPwd.value == u_cPwd.value) {
                        $.ajax({
                            url: "/doRegist/", // 这里应该前后加上/
                            type: "POST", // 提交数据的方式
                            dataType: "JSON", // 发送数据类型和响应的数据类型
                            data: {
                                "uname": uName.value, "uPwd": uPwd.value, "uPhone": uPhone.value,
                                "uEmail": uEmail.value, "uAddress": uAddress.value, "userName": userName.value
                            }, // 因为设置了json的传输格式，所以我需要配置json的数据形式进行传输
                            success: function (resp) { // 当服务器收到信息，返回数据，数据保存在resp变量中
                                alert(resp.msg);
                                uName.value = '';
                                uPwd.value = '';
                                uPhone.value = '';
                                uEmail.value = '';
                                uAddress.value = '';
                                userName.value = '';
                                u_cPwd.value = '';
                                admitRule.checked = False;
                            },
                            error: function (err) { // 如果没有数据返回，ajax认定为错误
                                alert('注册失败')
                            }
                        })

                    }
                    else {
                        alert("两次输入密码不一致，请重新输入");
                    }
                }
                else {
                    alert('请输入有效的邮箱');
                }
            }
            else {
                alert("请检查密码长度")
            }
        }
        else {
            alert("信息输入不全，请检查输入是否有空")
        }

    }
}
