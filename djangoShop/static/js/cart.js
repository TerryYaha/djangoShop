function doExit(){
    alert("即将退回主界面，请重新登录")
    window.location.href = "/doExit/";
}
function toIndex(){
    window.location.href = "/index/";
}
function toOrder(){
    window.location.href = "/order/";
}
function toService(){
    window.location.href = "/service/"
}
function myInfo(){
    window.location.href = "/myInfo/"
}

var count = 0, //一共多少条数据
    currPage = 1,  //当前页码
    allPage = 0,   //全部多少页
    limit = 3, //每页条数
    start = 0; //从第几条开始


//2.显示购物车页面
function initDataTable(){
    $.ajax({
        url:"/doCart/",
        type:'GET',
        dataType:'JSON',
        data:{
            "start":start,
            "limit":limit,
        },
        async: false, // 同步
        success:function(resp){
            arr = resp.datas;
            //1.删除已经存在的数据
            var items = document.getElementsByClassName("itemData")
            for (var i = items.length-1;i>=0;i--){
                items[i].remove()
            }
            //2.添加数据到table中
            var mytable = document.getElementById("dataTable");
            for (var i = 0 ; i<arr.length;i++){
                var msg = `
 <tr align="center" class="bottom itemData">
                        <td>
                            <input type="checkbox" class="ck" value="${arr[i].goodsPrice},${arr[i].buyId}">
                        </td>
                        <td class="item" align="left">
                            <img src="/static/img/${arr[i].goodsImg}" alt="">
                            <div class="text">
                                <span class="name">${arr[i].goodsName}</span><br/>
                                <span class="remarks">{颜色：QY7654}</span>
                            </div>
                        </td>
                        <td>
                            <span>默认</span>
                        </td>
                        <td class="price">
                            <span>￥ ${arr[i].goodsPrice+30}</span><br/>
                            <span>￥ ${arr[i].goodsPrice}</span>
                        </td>
                        <td>
                            　　　　<div class="btn-numbox">

                                <ul class="count">
                                    <li><span id="num-jian" class="num-jian">-</span></li>
                                    <li><input type="text" class="input-num" id="input-num" value="${arr[i].goodsNum}" /></li>
                                    <li><span id="num-jia" class="num-jia">+</span></li>
                                </ul>


                            　　　  </div>
                            <!-- <input type="button" value="-">
                            <span class="num">${arr[i].goodsNum}</span>
                            <input type="button" value="+"> -->
                        </td>
                        <td>
                            <span>￥ ${arr[i].goodsPrice}</span>
                        </td>
                        <td>
                            <span onclick="deleteAdmin(this,${arr[i].buyId})">删除</span>
                            <span>|</span>
                            <span>移入收藏夹</span>
                        </td>
                    </tr>`;
                mytable.innerHTML = mytable.innerHTML + msg
            }
            //设置页码
            count = resp.counts

            if (count % limit == 0){
                allPage = parseInt(count/limit);
            }else{
                allPage = parseInt(count/limit+1);
            }
//            document.getElementById("pageNum").innerHTML  = currPage+ "/"+ allPage
        },
        error:function(err){
            alert("请求失败")
        }
    }
    )
}
initDataTable();
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
function deleteAdmin(obj,buyId) {

	obj.parentElement.parentElement.parentElement.remove()
        $.ajax({
        url:"/toDeleteBuy/",
        type:'GET',
        dataType:'JSON',
        data:{
            "buyId":buyId,
        },
        success:function(resp){
            alert(resp.msg)
            initDataTable();
        },
        error:function(err){
            alert("请求失败")
        }
    }
    )
    initDataTable()
}
function checkAll(obj) {
	var bool = obj.checked;
	// 1.给所有表格中的复选框添加class属性，这里的值叫aaa
	// 2.获取所有class名字叫做aaa的复选框对象(得到复选框数组)
	var arr = document.getElementsByClassName('ck');
	console.log(arr.length)
	for(var i = 0; i < arr.length; i ++) {
		arr[i].checked = bool;
	}
}

var sumPrice = 0;
var counts = 0;
var goodsId = [];
function tip(){
	var checkboxs = document.getElementsByClassName('ck'),
	    onum = document.getElementById('onum'),
	    sprice = document.getElementById('sprice');
    if(checkboxs.length>0){
    	for(var i = 0;i<checkboxs.length;i++){
    	    var checkbox = checkboxs[i]
    	    if (checkbox.checked == true){
    	        goodlist = checkbox.value.split(",")
    	        sumPrice += parseInt(goodlist[0]);
    	        counts += 1;
    	        goodsId.push(parseInt(goodlist[1]))
    	    }
	    }
    }
    sprice.innerText = '￥' + sumPrice;
    onum.innerText = counts;
}
//全选框触发
$('.ckAll').click(function(){
    counts = 0;
    sumPrice = 0;
    goodsId = [];
    tip();
})
$('.ck').click(function(){
    counts = 0;
    sumPrice = 0;
    goodsId = [];
    tip();
})

function payBuyCar(){
    goodsId = goodsId.toString()
    $.ajax({
        url:"/payBuyCar/",
        type:'GET',
        dataType:'JSON',
        async: false, // 同步
        data:{
            "buy_id":goodsId,
            "sum_price":sumPrice,
        },
        success:function(resp){
            alert(resp.msg);
            initDataTable();
            tip();
            },
        error:function(err){
            alert("商品结算失败")
        }
    }
    )
    tip();

}
