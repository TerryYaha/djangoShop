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
function toService(){
    window.location.href = "/service/"
}
function myInfo(){
    window.location.href = "/myInfo/"
}
//显示订单页数据
var count = 0, //一共多少条数据
    currPage = 1,  //当前页码
    allPage = 0,   //全部多少页
    limit = 3, //每页条数
    start = 0; //从第几条开始
function initDataTable(){
    var onum = document.getElementById("orderNum");
    $.ajax({
        url:"/doOrder/",
        type:'GET',
        dataType:'JSON',
        data:{
            "orderNum":onum.value,
            "start":start,
            "limit":limit,
        },
        success:function(resp){
            arr = resp.datas;
            console.log(arr)
            //1.删除已经存在的数据
            var items = document.getElementsByClassName("container")
            for (var i = items.length-1;i>=0;i--){
                items[i].remove()
            }
            //2.添加数据到table中
            var item = document.getElementById("itemInfo");
            for (var i = 0 ; i<arr.length;i++){
                var msg1 = `
                                         <div class="container">
                        <div class="orderNum">
                            <span>订单号：<span class="num">${arr[i].orderNum}</span></span>
                            <span class="time">${arr[i].octime}</span>
                        </div>

                        <div class="itemContent">
                            <div class="item">
                                <div class="proimg">
                                    <img src="/static/img/${arr[i].goods_img}" alt="">
                                    <div class="text">
                                        <span class="name">${arr[i].goods_name}</span>
                                        <span class="def">默认</span>
                                        <span class="def">选择颜色：玫瑰金600</span>
                                    </div>
                                </div>
                                <ul class="itemAct">
                                    <li class="lineh">
                                        <span>${arr[i].goods_price}</span>
                                    </li>
                                    <li class="lineh">
                                        <span>${arr[i].goods_num}</span>
                                    </li>
                                    <li class="lineh def">
                                        <span>不可退换货</span>
                                    </li>
                                    <li class="lineh def">
                                        <span>不可评价</span>
                                    </li>
                                    <li class="lineh">
                                        <span>${arr[i].oprice}</span>
                                    </li>
                                    <li class="lineh">
                                        <span>未发货</span>
                                    </li>
                                    <li>

                                        <ul class="act">
                                            <li>
                                                <input type="button" value="订单详情">
                                            </li>
                                            <li class="active">
                                                <input type="button" value="立即支付" onclick="pay('${arr[i].orderNum}',${arr[i].oprice})">
                                            </li>
                                            <li>
                                                <input type="button" value="取消订单" onclick="deleteOrder(${arr[i].orderNum})">
                                            </li>
                                        </ul>
                                    </li>
                                </ul>
                            </div>
                        </div>
                                </div>`;
                var msg2 = `
             <div class="container">
                        <div class="orderNum">
                            <span>订单号：<span class="num">${arr[i].orderNum}</span></span>
                            <span class="time">${arr[i].octime}</span>
                        </div>

                        <div class="itemContent">
                            <div class="item">
                                <div class="proimg">
                                    <img src="/static/img/${arr[i].goods_img}" alt="">
                                    <div class="text">
                                        <span class="name">${arr[i].goods_name}</span>
                                        <span class="def">默认</span>
                                        <span class="def">选择颜色：玫瑰金600</span>
                                    </div>
                                </div>
                                <ul class="itemAct">
                                    <li class="lineh">
                                        <span>${arr[i].goods_price}</span>
                                    </li>
                                    <li class="lineh">
                                        <span>${arr[i].goods_num}</span>
                                    </li>
                                    <li class="lineh def">
                                        <span>不可退换货</span>
                                    </li>
                                    <li class="lineh def">
                                        <span>不可评价</span>
                                    </li>
                                    <li class="lineh">
                                        <span>${arr[i].oprice}</span>
                                    </li>
                                    <li class="lineh">
                                        <span>未发货</span>
                                    </li>
                                    <li>
                                       <ul class="act">
                                            <li>
                                                <input type="button" value="订单详情">
                                            </li>
                                            <li class="active">
                                                <input type="button" value="已支付">
                                            </li>
                                            <li>
                                                <input type="button" value="取消订单" onclick="deleteOrder('${arr[i].orderNum}')">
                                            </li>
                                        </ul>

                                    </li>
                                </ul>
                            </div>
                        </div>
                                </div>`;

                if (arr[i].ostate == 1){
                    item.innerHTML = item.innerHTML + msg1

                }else if(arr[i].ostate == 2){
                    item.innerHTML = item.innerHTML + msg2;
                }

            }
                        //设置页码
            count = resp.counts
            console.log(count)
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
    limit = 3;
    start = 0;

    orderNum = document.getElementById("orderNum").value;
    initDataTable()
}
//orderId是该商品得订单号
function deleteOrder(orderId){
        $.ajax({
        url:"/delOrder/",
        type:'GET',
        dataType:'JSON',
        data:{
            "orderId":orderId,
        },
        success:function(resp){
            alert(resp.msg);
            initDataTable();
            },
        error:function(err){
            alert("取消订单失败")
        }
    }
    )

}

//订单支付功能
function pay(orderNum,orderPrice){
    $.ajax({
        url:"/payOrder/",
        type:'GET',
        dataType:'JSON',
        data:{
            "orderNum":orderNum,
            "orderPrice":orderPrice,
//            "orderState":orderState,
        },
        success:function(resp){
            alert(resp.msg);
            initDataTable()
            },
        error:function(err){
            alert("订单支付失败")
        }
    }
    )

}