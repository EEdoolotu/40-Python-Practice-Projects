
+while True:
+    try:
+        num = int(input("What number did you want to assess? "))
+        check = num % 2
+        if check == 0:
+            print("That is an even number!")
+        else:
+            print("That is an odd number")
+        break
+    except ValueError:
+        print("Please enter a valid integer")
