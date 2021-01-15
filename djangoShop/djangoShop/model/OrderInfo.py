class OrderInfo():
        def __init__(self,goods_num,ogid,onum,goods_id,goods_name,goods_price,goods_img,oid,octime,ostate,oprice):
                self.goods_num = goods_num
                self.order_goodsId = ogid #订单商品id
                self.orderNum = onum    #订单号
                self.goodsId = goods_id #商品id
                self.goods_name = goods_name #商品名字
                self.goods_price = goods_price #商品价格
                self.goods_img = goods_img #商品图片地址
                self.oid = oid #订单id
                self.octime = octime  #订单下单时间
                self.ostate = ostate #订单状态
                self.oprice = oprice #订单价格
                pass