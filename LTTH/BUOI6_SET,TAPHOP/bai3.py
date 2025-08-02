def nhap_n_tap(n):
    tap_list = []
    for i in range(n):
        print(f"\nNhập các phần tử cho tập thứ {i} (Enter để kết thúc):")
        tap = set()
        while True:
            x = input(f"Tập-{i}: ").strip()
            if x == "":
                break
            tap.add(x)
        tap_list.append(tap)
    return tap_list

def in_tap(tap):
    print("{", ", ".join(tap), "}")


n = int(input("Nhập số lượng tập hợp (n): "))
ds_tap = nhap_n_tap(n)

print("\n--- Câu 1: Các phần tử thuộc cả tập k và tập m ---")
k = int(input("Nhập chỉ số k: "))
m = int(input("Nhập chỉ số m: "))
if 0 <= k < n and 0 <= m < n:
    ketqua1 = ds_tap[k] & ds_tap[m]
    print(f"Các phần tử thuộc cả tập {k} và tập {m}:")
    in_tap(ketqua1)
else:
    print("Chỉ số k hoặc m không hợp lệ!")

print("\n--- Câu 2: Phần tử thuộc tập k mà KHÔNG thuộc tập còn lại ---")
k = int(input("Nhập chỉ số k: "))
if 0 <= k < n:
    cac_tap_con_lai = set()
    for i in range(n):
        if i != k:
            cac_tap_con_lai.update(ds_tap[i])
    ketqua2 = ds_tap[k] - cac_tap_con_lai
    print(f"Các phần tử chỉ thuộc tập {k}, không thuộc các tập khác:")
    in_tap(ketqua2)
else:
    print("Chỉ số k không hợp lệ!")

print("\n--- Câu 3: Phần tử thuộc tập k và cũng thuộc các tập khác ---")
k = int(input("Nhập chỉ số k: "))
if 0 <= k < n:
    cac_tap_con_lai = set()
    for i in range(n):
        if i != k:
            cac_tap_con_lai.update(ds_tap[i])
    ketqua3 = ds_tap[k] & cac_tap_con_lai
    print(f"Các phần tử thuộc tập {k} và cũng thuộc các tập khác:")
    in_tap(ketqua3)
else:
    print("Chỉ số k không hợp lệ!")
