function doExit(){
    alert('您将回到首页，请重新登录')
    window.location.href = "/doExit/";
}
function toIndex(){
    window.location.href = "/index/";
}
function doLogin(){
    var userName = document.getElementById("uname");
    var userPwd = document.getElementById("upwd");
    if (userName && userPwd){
        $.ajax({
            url:"/doAdminLogin/", // 这里应该前后加上/
            type: "POST", // 提交数据的方式
            dataType: "JSON", // 发送数据类型和响应的数据类型
            data: {"name": userName.value, "pwd" : userPwd.value}, // 因为设置了json的传输格式，所以我需要配置json的数据形式进行传输
            success: function(resp) { // 当服务器收到信息，返回数据，数据保存在resp变量中
                alert(resp.msg)
                window.location.href = resp.location;
            },
            error: function(err) { // 如果没有数据返回，ajax认定为错误
                alert('数据有错误')
            }
        })
    }else{
        alert("用户名或密码有空值，请重新输入")
    }
}