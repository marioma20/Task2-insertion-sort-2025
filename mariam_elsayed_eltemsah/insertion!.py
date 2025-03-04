def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key.lower() < arr[j].lower():
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# قراءة البيانات من ملف نصي
with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  # قراءة جميع الأسطر

# تنظيف البيانات من أي مسافات زائدة
lines = [line.strip() for line in lines if line.strip()]

# ترتيب البيانات
insertion_sort(lines)

# حفظ البيانات بعد الترتيب في نفس الملف
with open("data.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line + "\n")

print("The text data is arranged and saved in the file.")

# إذا كانت القائمة مرتبة بالفعل، فإن الحلقة الداخلية while لن تتحرك أبدًا، وسنقوم فقط بمرور واحد على كل عنصر، أي زمن التنفيذ سيكون خطيًا O(n).
# الحالة الثانية: عندما تكون البيانات مخزنة في ملف (.txt)
# قراءة الملف O(n) لأننا نمر على كل سطر.
# الترتيب في أفضل حالة O(n) (عند ترتيب البيانات مسبقًا).
# الكتابة إلى الملف O(n) لأننا نحفظ كل البيانات مرة أخرى.
#  O(n)+O(n)+O(n)=O(n)

# أفضل حالة (Best Case) – O(n)
#  أسوأ حالة (Worst Case) – O(n²)
# إذا كانت القائمة مرتبة عكسيًا، فإن كل عنصر جديد يحتاج إلى تحريك جميع العناصر التي قبله، مما يجعل عدد المقارنات والحركات يساوي (n-1) + (n-2) + ... + 1 = O(n²).
# قراءة الملف = O(n).
# ترتيب البيانات = O(n²) (لأن القائمة غير مرتبة وسنحتاج لتحريك العديد من العناصر).
# حفظ البيانات إلى الملف = O(n).
# O(n)+O(n 2 )+O(n)=O(n 2 )


