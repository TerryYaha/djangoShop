function registPage(){
    window.location.href = "/regist/";
}
function toIndex(){
    window.location.href = "/index/";
}
function initCode(){
    //1.获取输入框对象
    var vailCode = document.getElementById("vailCode")
    //1.生成验证码字符串
    var codeMsa = '';
    for (var i = 0;i<4;i++){
        codeMsg = Math.floor(Math.random()*9);
        codeMsa += codeMsg
    }
    // alert(codeMsg)
    vailCode.value = codeMsa
}

window.onload = function(){
    initCode();
}

function doLogin(){
    var userName = document.getElementById("uName");
    var userPwd = document.getElementById("uPwd");
    var vailCode = document.getElementById("vailCode");
    var uvailCode = document.getElementById("uvailCode");
    if (uvailCode.value != vailCode.value){
        alert("验证码错误，请重新输入")
    }else{
        $.ajax({
            url:"/doLogin/", // 这里应该前后加上/
            type: "POST", // 提交数据的方式
            dataType: "JSON", // 发送数据类型和响应的数据类型
            data: {"name": userName.value, "pwd" : userPwd.value}, // 因为设置了json的传输格式，所以我需要配置json的数据形式进行传输
            success: function(resp) { // 当服务器收到信息，返回数据，数据保存在resp变量中
                window.location.href = resp.location;
            },
            error: function(err) { // 如果没有数据返回，ajax认定为错误
                alert("用户名或密码错误,请重新输入")
            }
        })
    }
}
