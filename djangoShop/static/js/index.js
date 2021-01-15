//window.onload = function(){
//
//}

function doExit(){
    window.location.href = "/doExit/";
}
function doAdminLoginPage(){
    window.location.href = "/adminLogin/";
}
function doLogin(){
    window.location.href = "/login/";
}
function toService(){
    window.location.href = "/service/";
}
function registPage(){
    window.location.href = "/regist/";
}
function orderPage(){
    window.location.href = "/order/";
}
function toChat(user){
   console.log(user)
   if(user=='None')
   {
      alert('请先登录');
      window.location.href = "/login/";
   }else{
        window.location.href = "/user/";
   }
}
function toCart(user){
   if(user=='None')
   {
      alert('请先登录');
      window.location.href = "/login/";
   }else{
      window.location.href = "/cart/";
   }
}
var items = document.getElementsByClassName("item");
// var goPrevBtn = document.getElementById("goPrev");
// var goNextBtn = document.getElementById("goNext");
var points = document.getElementsByClassName("point")

var index = 0;//表示第几张图片在展示
var clearActive = function () {
    for(var i = 0;i<items.length;i++) {
        items[i].className = "item";
        // items[i].addListener("item");
    }
    for(var i = 0;i<points.length;i++) {
        points[i].className = "point";
    }

}
var goIndex = function () {
    clearActive();
    items[index].className = 'item active';
    points[index].className = 'point active';
}
var goNext = function () {
    if(index < 4){
        index++;
    }else{
        index = 0;
    }
    goIndex();
}
//定时器
var timer = setInterval(goNext,3000);
// var goPrev = function () {
//     if(index == 0){
//         index = 4;
//     }else {
//         index--;
//     }
//     goIndex();
// }

// goNextBtn.addEventListener('click',function () {
//     goNext();
// })

// goPrevBtn.addEventListener('click',function () {
//     goPrev();
// })

for(var i = 0; i < points.length;i++){
    points[i].addEventListener('click',function () {
        var pointIndex = this.getAttribute('data-index');
        index = pointIndex;
        goIndex();

    })
}

var count = 0, //一共多少条数据
    currPage = 1,  //当前页码
    allPage = 0,   //全部多少页
    limit = 13, //每页条数
    start = 0; //从第几条开始


//2.设置搜索的变量
var content = '';

function initDataTable(){
    $.ajax({
        url:"/proPage/",
        type:'POST',
        dataType:'JSON',
        data:{
            "pro":content,
            "start":start,
            "limit":limit,
        },
        success:function(resp){
            arr = resp.datas;
            //1.删除已经存在的数据
            var pros = document.getElementsByClassName("itempro")
            for (var i = pros.length-1;i>=0;i--){
                pros[i].remove()
            }
            //2.添加数据到table中
            var mytable = document.getElementById("table");
            for (var i = 0 ; i<arr.length-1;i++){
                var msg = `
                <a href="/detail/?a=${arr[i].gid}">
                 <li class="itempro">
                                <img src="/static/img/${arr[i].gimg}" alt="">
                                <div class="saleInfo">
                                    <span class="saleNum">销量：${arr[i].gnum}</span>
                                    <span class="salePrice">${arr[i].gprice}&nbsp;元</span>
                                </div>
                                <span class="name">${arr[i].gname}</span>

                            </li></a>`;
                mytable.innerHTML = mytable.innerHTML + msg
            }
            //设置页码
            count = resp.counts
            if (count % limit == 0){
                allPage = parseInt(count/limit);
            }else{
                allPage = parseInt(count/limit+1);
            }
            document.getElementById("pageNum").innerHTML  = currPage+ "/"+ allPage
        },
        error:function(err){
            alert("请求失败")
        }
    }
    )
}
initDataTable()

function doPre(){
    if (currPage == 1){
        alert("当前已是第一页");
    }else{
        currPage-=1;
        start -= limit;
        initDataTable();

    }
}
function doNext(){
    if (currPage == allPage)
        alert("当前为最后一页");
    else{
        currPage+=1;
        start += limit;
        initDataTable();
    }
}
function doSearch(){
    count = 0;
    currPage = 1;
    allPage = 0;
    limit = 13;
    start = 0;
    content = document.getElementById("pro").value;
    initDataTable()
}

function toDetail(gid){


}