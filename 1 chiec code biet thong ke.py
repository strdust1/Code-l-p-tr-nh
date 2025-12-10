tai_khoan = str(input("Hãy nhập tài khoản của bạn: "))
mat_khau = str(input("Hãy nhập mật khẩu: "))
số_lần = 0
tai_khoan_nd = [{"tài khoản":"Meimei", "mật khẩu":"1611"}] 
while số_lần<= 2:
        for i in tai_khoan_nd:
            if mat_khau == i["mật khẩu"] and tai_khoan == i["tài khoản"]:
                print("đã nhập đúng mật khẩu!")
                thong_tin =[{"tên":"Nguyễn Hà Vũ", "tuổi":"17", "sinh nhật":"ngày 24 tháng 12", "tư cách": "chủ sở hữu"}]
                produckkk =[{"mã":"Sp001", "tên":"Áo thun", "giá":150000, "số lượng":10}, {"mã":"Sp002", "tên":"Quần jean", "giá":300000, "số lượng":5}]
                #1.Hiển thị ra danh sách sản phẩm
                print("Chào mừng quay trở lại trang quản lý cửa hàng thời trang")
                print("Sau đây là các thông số sản phẩm")
                print("------------------------------")
                for i in produckkk:
                    print("Mã sản phẩm: ", i["mã"])
                    print("Tên sản phẩm: ", i["tên"])
                    print("Giá bán: ", i["giá"])
                    print("Số lượng tồn kho: ", i["số lượng"])
                    print("------------------------------")
                while True:
                    a = str(input(("Muốn chỉnh sửa nó không: ")))
                    if a == "không":
                        print("Cảm ơn đã sử dụng chương trình")
                        số_lần = 5
                        break
                    elif a == "có":
                        print("1: Thêm sản phẩm")
                        print("2: Xóa sản phẩm")
                        print("3: Cập nhật sản phẩm")
                        print("4: Tìm sản phẩm")
                        print("5: Tính tổng số tiền của sản phẩm")
                        print("6: Hiện danh sách sản phẩm")
                        print("7: Hiện sản phẩm sắp hết hàng")
                        print("8: Cài đặt")
                        b = str(input("Hãy nhập số từ 1 đến 8 ứng các lựa chọn trên: "))
                #2.Thêm sản phẩm        
                        if b == "1":
                            ma = str(input("Nhập mã sản phẩm: "))
                            ten =str(input("Nhập tên sản phẩm: "))
                            gia = int(input("Nhập giá bán: "))
                            so = int(input("Nhập số lượng tồn kho: "))
                            if [ma, ten, gia, so] not in produckkk:
                                produckkk =[{"mã":"Sp001", "tên":"Áo thun", "giá":150000, "số lượng":10}, {"mã":"Sp002", "tên":"Quần jean", "giá":300000, "số lượng":5}, {"mã":ma, "tên":ten, "giá":gia, "số lượng":so}]
                            else:
                                print("Sản phẩm đã tồn tại")
                                continue
                #3.Xóa sản phẩm            
                        elif b == "2":
                            ma_xoa = str(input("Hãy nhập mã sản phẩm bạn muốn xóa: "))
                            found= False
                            for i in produckkk:
                                if i["mã"] == ma_xoa:
                                    print("Mã sản phẩm: ", i["mã"])
                                    print("Tên sản phẩm: ", i["tên"])
                                    print("Giá bán: ", i["giá"])
                                    print("Số lượng tồn kho: ", i["số lượng"])
                                    produckk = produckkk.remove(i)
                                    print("Đã xóa sản phẩm trên")
                                    found = True
                            if found == False:
                                    print("Không tìm thấy sản phẩm")
                                    continue
                #4.Cập nhật sản phẩm            
                        elif b == "3":
                            ma_cap_nhat = str(input("Hãy nhập mã sản phẩm bạn muốn cập nhật: "))
                            Cap_nhat = False
                            for i in produckkk:
                                if i["mã"] == ma_cap_nhat:
                                    ma_cn = str(input("Nhập mã sản phẩm mới: "))
                                    ten_cn = str(input("Nhập tên sản phẩm mới: "))
                                    ban_cn = int(input("Nhập giá bán mới: "))
                                    so_cn = int(input("Nhập số lượng tồn kho mới: "))
                                    i["mã"] = ma_cn
                                    i["tên"] = ten_cn
                                    i["giá"] = ban_cn
                                    i["số lượng"] = so_cn
                                    print("------------------------------")
                                    print("Mã sản phẩm: ", i["mã"])
                                    print("Tên sản phẩm: ", i["tên"])
                                    print("Giá bán: ", i["giá"])
                                    print("Số lượng tồn kho: ", i["số lượng"])
                                    print("Đã cập nhật sản phẩm trên")
                                    Cap_nhat = True
                            if Cap_nhat == False:
                                print("Không tìm thấy sản phẩm cần cập nhật")
                                continue
                #5.Tìm sản phẩm            
                        elif b == "4":
                            tim = input("Hãy nhập tên sản phẩm bạn muốn tìm: ")
                            san_pham_tim = []
                            Tim = False
                            for i in produckkk:
                                if i["tên"].lower() == tim.lower():
                                    san_pham_tim.append(i)
                                    Tim = True
                            if Tim:
                                print("Danh sách các sản phẩm bạn đã tìm:")
                                for sp in san_pham_tim:
                                    print("Mã sản phẩm: ", i["mã"])
                                    print("Tên sản phẩm: ", i["tên"])
                                    print("Giá bán: ", i["giá"])
                                    print("Số lượng tồn kho: ", i["số lượng"])
                                    print("------------------------------")
                            else:
                                print("Không tìm thấy sản phẩm!")
                #6.Tính tổng sản phẩm                
                        elif b == "5":
                            tong = str(input("Nhập mã sản phẩm bạn muốn tính tổng: "))
                            Tong = False
                            for i in produckkk:
                                if i["mã"] == tong:
                                    print("Tổng số tiền bán của sản phẩm này là: ", i["giá"]*i["số lượng"])
                                    Tong = True
                                    check = str(input("Bạn có muốn hiển thị toàn bộ giá của sản phẩm không?: "))
                                    if check == "không":
                                        continue
                                    elif check == "có":
                                        for i in produckkk:
                                            print("Mã sản phẩm: ", i["mã"])
                                            print("Tên sản phẩm: ", i["tên"])
                                            print("Tổng tiền bán: ", i["giá"]*i["số lượng"])
                                            print("------------------------------")
                                            continue
                                    else:
                                        print("Chỉ nhập 'không' hoặc 'có', hãy thử lại.")    
                            if Tong == False:
                                print("Không có sản phẩm cần tìm")
                                continue    
                #7.Thông tin các sản phẩm                
                        elif b == "6":
                            print("Danh sách các sản phẩm")
                            print("------------------------------")
                            for i in produckkk:
                                print("Mã sản phẩm: ", i["mã"])
                                print("Tên sản phẩm: ", i["tên"])
                                print("Giá bán: ", i["giá"])
                                print("Số lượng tồn kho: ", i["số lượng"])
                                print("------------------------------")
                #8.Kiểm tra sản phẩm sắp hết hàng                
                        elif b == "7":
                            san_pham_sap_het_hang = []
                            SHH = False
                            for i in produckkk:
                                if i["số lượng"] <= 5 :
                                    san_pham_sap_het_hang.append(i)
                                    print("Danh sách các sản phẩm sắp hết hàng:")
                                    for j in san_pham_sap_het_hang:
                                        print("Mã sản phẩm: ", i["mã"])
                                        print("Tên sản phẩm: ", i["tên"])
                                        print("Giá bán: ", i["giá"])
                                        print("Số lượng tồn kho: ", i["số lượng"])
                                        print("------------------------------")
                                        SHH = True
                                        continue
                            if SHH == False:
                                print("Hiện tại không có sản phẩm nào sắp hết hạn")
                                continue
                        elif b =="8":
                            print("1: Thông tin tài khoản")
                            print("2: Thay đổi mật khẩu")
                            print("3: Chỉnh sửa tên người dùng")
                            print("4: Quay lại")
                            z = str(input("Hãy nhập lựa chọn của bạn: "))
                            if z == "1":
                                for i in thong_tin:
                                    print("Họ và tên:", i["tên"])
                                    print("Tuổi:", i["tuổi"])
                                    print("Ngày sinh:", i["sinh nhật"])
                                    print("Tư cách:", i["tư cách"])
                                for i in tai_khoan_nd:
                                    print("Tên người dùng:", i["tài khoản"])    
                                cs = str(input("Muốn chỉnh sửa nó không: "))
                                if cs =="có":
                                    tn = str(input("Nhập lại họ và tên: "))
                                    tu = str(input("Nhập lại tuổi: "))
                                    sn = str(input("Nhập lại sinh nhật: "))
                                    tc = str(input("Sửa lại tư cách: "))
                                    i["tên"] = tn
                                    i["tuổi"] = tu
                                    i["sinh nhật"] = sn
                                    i["tư cách"] = tc
                                    print("Họ và tên:", i["tên"])
                                    print("Tuổi:", i["tuổi"])
                                    print("Ngày sinh:", i["sinh nhật"])
                                    print("Tư cách:", i["tư cách"])
                                    print("Đã cập nhật lại thông tin thành công")
                                elif cs =="không":
                                    continue
                                else:
                                    print("Chỉ có ghi 'có' hoặc 'không', hãy nhập lại")
                            elif z == "2":
                                for i in tai_khoan_nd:
                                    nmk = str(input("Hãy nhập lại mật khẩu của bạn: "))
                                    if i["mật khẩu"] == nmk:
                                        mkm = str(input("Hãy nhập lại mật khẩu mới: "))
                                        i["mật khẩu"] = mkm
                                        print("Đã cập nhật mật khẩu thành công")
                                        break
                                    else:
                                        print("Mật khẩu nhập đã bị sai, hãy nhập lại")
                                        continue
                            elif z == "3":
                                for i in tai_khoan_nd:
                                    tkm = str(input("Nhập tên tài khoản mới của bạn: "))
                                    i["tài khoản"] = tkm
                                    print("Đã cập nhật tên tài khoản của bạn")
                            elif z == "4":
                                continue        
                        else:    
                            print("Lựa chọn bạn nhập không hợp lệ, hãy nhập lại.")
                            continue   
                    else:
                        print("Lưu ý chỉ nhập 'có' hoặc 'không', xin hãy nhập lại.")
                        continue   
            else:
                số_lần+=1
                print("Đã nhập sai tài khoản hoặc mật khẩu, còn",3 -số_lần, "lần thử, hãy nhập lại")
                tai_khoan = str(input("Hãy nhập tài khoản của bạn: "))
                mat_khau = str(input("Hãy nhập mật khẩu: "))  
                if số_lần > 2:
                    print("Tài khoản đã bị khóa, về ăn rau moá đi kưng")

                    



     