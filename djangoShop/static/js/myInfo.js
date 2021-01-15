function doExit(){
    alert("即将退回主界面，请重新登录")
    window.location.href = "/doExit/";
}
function toIndex(){
    window.location.href = "/index/";
}
function toCart(){
    window.location.href = "/cart/";
}
function toOrder(){
    window.location.href = "/order/";
}
function toService(){
    window.location.href = "/service/"
}
function initInfo(){
    var uname = document.getElementById("uname"),
        uemail = document.getElementById("uemail"),
        utel = document.getElementById("utel"),
        userName = document.getElementById("userName"),
        uaddress = document.getElementById("uaddress");

    $.ajax({
        url:"/myInfoInit/", // 这里应该前后加上/
        type: "GET", // 提交数据的方式
        dataType: "JSON", // 发送数据类型和响应的数据类型
//        data: {"name": userName.value, "pwd" : userPwd.value},
        success: function(resp) { // 当服务器收到信息，返回数据，数据保存在resp变量中
            arr = resp.datas;
            console.log(arr);
            uname.value = arr[0].uname;
            uemail.value = arr[0].uEmail;
            utel.value = arr[0].uphone;
            userName.value = arr[0].uer_name;
            uaddress.value = arr[0].uAddress;
        },
        error: function(err) { // 如果没有数据返回，ajax认定为错误
            alert('请联系管理员...')
        }
    })
}
initInfo();

function updateUser(){
    var uname = document.getElementById("uname"),
        uemail = document.getElementById("uemail"),
        utel = document.getElementById("utel"),
        userName = document.getElementById("userName"),
        uaddress = document.getElementById("uaddress");

    $.ajax({
    url:"/updateInfo/", // 这里应该前后加上/
    type: "POST", // 提交数据的方式
    dataType: "JSON", // 发送数据类型和响应的数据类型
    data: {"uname": uname.value, "uemail" : uemail.value,
        "utel":utel.value,"userName":userName.value,"uaddress":uaddress.value},
    success: function(resp) { // 当服务器收到信息，返回数据，数据保存在resp变量中
        alert(resp.msg);
        initInfo();
    },
    error: function(err) { // 如果没有数据返回，ajax认定为错误
        alert('请联系管理员...')
    }
})
}