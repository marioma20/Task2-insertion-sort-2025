def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key.lower() < arr[j].lower():  # مقارنة النصوص مع تجاهل الحالة (صغير/كبير)
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# بيانات نصية
data = ["zain", "ahmed", "lina", "mohamed", "amira"]

# تطبيق الترتيب
insertion_sort(data)

print("Data after sorting:", data)
# الحلقة الخارجية for تمر على جميع العناصر n مرة.
# الحلقة الداخلية while في أسوأ الحالات قد تقوم بتحريك جميع العناصر السابقة، أي حتى n مرة.
#   
# (Worst Case) – O(n²) عندما تكون القائمة مرتبة عكس المطلوب.
# (Best Case) –(O(n) عندما تكون القائمة مرتبة مسبقًا.
