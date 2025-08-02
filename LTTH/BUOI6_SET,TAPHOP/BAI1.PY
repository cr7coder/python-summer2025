def nhap_tap(ten_tap):
    tap = set()
    print(f"Nhập các phần tử cho tập {ten_tap} (Enter để kết thúc):")
    while True:
        x = input(f"{ten_tap} > ").strip()
        if x == "":
            break
        tap.add(x)
    return tap

A = nhap_tap("A")
B = nhap_tap("B")
if B.issubset(A):
    print("B là tập con của A.")
    A.difference_update(B)  
    print("Tập A sau khi xóa các phần tử của B:", A)
else:
    print("B không là tập con của A.")
Z = A.symmetric_difference(B)
print("Tập Z (các phần tử thuộc A hoặc B nhưng không đồng thời thuộc cả hai):", Z)

if A.isdisjoint(B):
    print("A và B không có phần tử chung. B sẽ được bổ sung toàn bộ phần tử của A.")
    B.update(A)
    print("Tập B sau khi bổ sung:", B)
else:
    khacnhau = A.difference(B)
    print("Các phần tử thuộc A mà không thuộc B:", khacnhau)
