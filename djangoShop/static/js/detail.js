url = window.location.href;
var arr = url.split("=");
var a = arr[1];

function doExit(){
    window.location.href = "/doExit/";
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
function toIndex(){
    window.location.href = "/index/";
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

//显示详情页数据
function initDataTable(){
    $.ajax({
        url:"/doDetail/",
        type:'GET',
        dataType:'JSON',
        data:{
            "a":a
        },
        async: false, // 同步
        success:function(resp){
            arr = resp.datas;

            //1.添加数据到table中
            var item = document.getElementById("itemInfo");
            var msg = `
                                <div class="proImg">
                                                    <div id="box">
                                <div class="big_pic">
                                    <img class="big_img" src="/static/img/${arr[0].gimg}" width="500" height="400" />
                                </div>
                                <div class="small_pic">
                                    <span class="slider"></span>
                                    <img src="/static/img/${arr[0].gimg}" />
                                </div>
                            </div>
                        <ul>
                            <li class="active">
                                <img src="/static/img/macb1.jpg" alt="">
                            </li>
                            <li>
                                <img src="/static/img/macb2.jpg" alt="">
                            </li>
                            <li>
                                <img src="/static/img/macb3.jpg" alt="">
                            </li>
                            <li>
                                <img src="/static/img/macb4.jpg" alt="">
                            </li>
                            <li>
                                <img src="/static/img/macb5.jpg" alt="">
                            </li>
                        </ul>

                    </div>

                    <div class="proAct">
                        <span>${arr[0].gname}</span>
                        <ul class="proInfo">
                            <li>
                                <span>库存：${arr[0].gnum}</span>
                            </li>
                            <li>
                                <span>销量：${arr[0].gsalenum}</span>
                            </li>
                            <li>
                                <span>规格：</span><span class="default">默认</span>
                            </li>
                            <li class="num">
                                <span>数量：</span>
                                <input type="button" value="-" class="mlus">
                                <input type="text" value="1" class="itemNum" id="goodsNum">
                                <input type="button" value="+" class="plus">
                            </li>
                            <li class="price">
                                <span>价格：</span>
                                <span class="nowPrice">￥${arr[0].gprice}</span>
                            </li>
                        </ul>
                        <div class="btn">
                            <input type="button" value="立即购买" onclick="toBuy(${arr[0].gid},${arr[0].gprice},'${arr[0].gname}','${arr[0].gimg}')">
                            <input type="button" value="加入购物车" onclick="addCart(${arr[0].gid},'${arr[0].gname}','${arr[0].gimg}',${arr[0].gprice})">
                        </div></div>`;
            item.innerHTML = item.innerHTML + msg
//            }

        },
        error:function(err){
            alert("请求失败")
        }
    }
    )
}
initDataTable()
window.onload = function(){
    //选择器封装
    function $(name) {
        return document.querySelector(name);
    };
    var small_pic = $(".small_pic"),   //左侧的图片
        slider = $(".slider"),    //滑块
        big_pic = $(".big_pic"),    //右侧BOX
        big_img  = $(".big_img");    //右侧大图
    //移入
    small_pic.onmousemove = function(event){   //event对象  事件的状态
        slider.style.display = 'block';
        big_pic.style.display = 'block';
        //event.clientX  当前移入点与X轴的坐标   slider.offsetWidth   滑块的宽度
        var left = event.clientX-330 - slider.offsetWidth/2;//这里因为父类选择器的宽度居中需要剪掉
        var top = event.clientY-190 - slider.offsetHeight/2;
        var w = this.offsetWidth - slider.offsetWidth;
        var h = this.offsetHeight - slider.offsetHeight;
        //移动范围
        if(left <0) {
            left = 0;
        }else if(left > w) {
            left = w;
        };
        if(top <0) {
            top = 0;
        }else if(top > h) {
            top = h;
        };
        slider.style.left = left +'px';
        slider.style.top = top +'px';
        big_img.style.left = -(left*1.7) +'px';   //右侧大图的距离
        big_img.style.top = -(top*1.7) +'px';
    };
    //移出  onmouseout有问题，浏览器兼容性
    small_pic.onmouseleave= function(){
        slider.style.display = 'none';
        big_pic.style.display = 'none';
    };
}
//立即购买，加入订单,参数obj为该商品得id
function toBuy(obj,price,gname,gimg){
    var goodsNum = document.getElementById("goodsNum")
    $.ajax({
        url:"/toBuy/",
        type:'GET',
        dataType:'JSON',
        data:{
            "goods_id":obj,
            "goods_price":price,
            "goods_name":gname,
            "goods_img":gimg,
            "goods_num":goodsNum.value,
        },
        success:function(resp){
            alert(resp.msg)
            window.location.href = resp.location
        },
        error:function(err){
            alert("请求失败")
        }
    }
    )
}

//立即购买，加入订单,参数obj为该商品得id
function addCart(gid,goods_name,goods_img,goods_price){
    var goodsNum = document.getElementById("goodsNum")
    $.ajax({
        url:"/addCart/",
        type:'GET',
        dataType:'JSON',
        data:{
            "goods_id":gid,
            "goods_name":goods_name,
            "goods_img":goods_img,
            "goods_price":goods_price,
            "goodsNum":goodsNum.value,
        },
        success:function(resp){
            alert(resp.msg)
            window.location.href = resp.location
        },
        error:function(err){
            alert("请求失败")
        }
    }
    )
}