var names = document.getElementsByClassName("name");

function nowtime(){
    var timestamp=new Date().getTime();
    var now = new Date(timestamp),
        y = now.getFullYear(),
        m = now.getMonth() + 1,
        d = now.getDate(),
        time = y + "-" + (m < 10 ? "0" + m : m) + "-" + (d < 10 ? "0" + d : d) + " " + now.toTimeString().substr(0, 8);
    return time
}

//回车事件绑定
$('#inputPanel').bind('keyup', function(event) {
　　　　//回车执行查询
　　if (event.keyCode == "13") {
　　　　 event.returnValue = false;
　　　　$('#search_button').click();
       event.returnValue = false;
       return false;
　　}
});
var clearActive = function () {
    for(var i = 0;i<names.length;i++) {
        names[i].className = "name";
    }
}
function toIndex(){
    window.location.href = "/index/";
}
function change(obj){
    clearActive();
    var index= [].indexOf.call(obj.parentNode.querySelectorAll(obj.tagName),obj);
    names[index].className = "name active";
}
ws = new WebSocket("ws://localhost:8000/");
ws.onopen = function () {
    console.log('客服连接上服务器');
    jsonObj = {"service": "addAdmin", "content": "admin"};
    ws.send(JSON.stringify(jsonObj));
}
ws.onmessage = function (e) {
    var data = e.data;
    console.log('收到数据：', data);
    var jsonObj = JSON.parse(data);
    if(jsonObj.service == 'userNames') {
        // 1.得到所有用户信息
        var arr = jsonObj.content;
        // 2.将数据添加到ul的用户列表中
        if(arr) {
            var ulObj = document.getElementById('users');
            for(var item of arr) {
                ulObj.innerHTML = ulObj.innerHTML + `<li onclick="chooseUser(this)">${item}</li>`
            }
        }
    }
    if(jsonObj.service == 'addUser') {
        var ulObj = document.getElementById('users');
        ulObj.innerHTML = ulObj.innerHTML + `<li class="name" onclick="change(this)">${jsonObj.content}</li>`
    }
    if(jsonObj.service == 'sendUserMsg') {
        var showPanel = document.getElementById('showPanel');
        showPanel.value = showPanel.value + jsonObj.content;
    }
    if(jsonObj.service == 'sendTalks') {
        var arr = jsonObj.content;
        // 2.将数据添加到ul的用户列表中
        if(arr) {
            var showPanel = document.getElementById('showPanel');
            // 清空面板的数据
            showPanel.value = "";
            for(var item of arr) {
                showPanel.value = showPanel.value + item;
            }
        }
    }
    if(jsonObj.service == 'tipMsg') {
        alert(jsonObj.content);
    }
}
ws.onclose = function () {
    console.log('关闭数据连接...');
}

function sendMsg() {
    var  arr = document.getElementsByClassName('active');
    if( arr.length == 0) {
        alert('请选择用户');
    }else {
        var who = arr[0].innerHTML;
        var msg = document.getElementById('inputPanel').value;

        var jsonObj = {'service':'sendAdminMsg', 'who':who, 'content':"\n"+nowtime()+":"+" 小库:" +msg};
        ws.send(JSON.stringify(jsonObj));

        document.getElementById('inputPanel').value = "";
    }
}
//定义发送到聊天框函数
    function AddSentMsgIntoBox(msg_text){
        //拼接聊天内容
        /*气泡实现
        <div class="clearfix">
            <div class="arrow"></div>
            <div class="content_send"><div style="margin-top: 10px;margin-left: 5px;">Hello Shuaige</div></div>
        </div>
         */
        var msg_ele = "<div class='clearfix' style='padding-top:10px'>" + "<div class='arrow'>" + "</div>" +
                        "<div class='content_send'>" + "<div style='margin-top: 10px;margin-left: 5px;'>" +
                        msg_text + "</div>" + "</div>";
        $(".chat_contener").append(msg_ele);
        //animate 动画效果
        $('.chat_contener').animate({
            scrollTop: $('.chat_contener')[0].scrollHeight}, 500
        );//动画效果结束
        }//发送到聊天框函数结束

// 选择对应的用户进行聊天
function chooseUser(obj) {
    // 添加高亮的样式
    var arr = obj.parentElement.children;
    for(var i = 0; i < arr.length; i ++) {
        arr[i].classList.remove('active');
    }
    obj.classList.add('active');

    var jsonObj = {'service':'lightUser', 'content': obj.innerHTML};
    ws.send(JSON.stringify(jsonObj));
}
function doUpload() {
    // 1.创建一个数据对象，这个数据对象用来存放文件的所有数据
    var d = new FormData();
    // 2.获取文件的信息
    // 2.1.先获取输入框对象
    var inputObj = document.getElementById('fileUpload');
    // 2.2.从输入框中获取文件信息
    fileInfo = inputObj.files[0];
    // 3.将文件信息保存到数据对象中
    d.append("aaa", fileInfo);
    $.ajax({
        url:'/doFileUpload/',
        type:'POST',
        data: d,
        processData: false, // 我们的ajax默认传递的是字符串，如果要传递文件信息解析方式取消
        contentType: false, // 我们的ajax默认的格式是json，设置该属性意味着ajax不要做json格式的验证
        success: function(resp) {
            alert("ok");
        },
        error : function(err) {
            alert('上传失败');
        }
    })
}