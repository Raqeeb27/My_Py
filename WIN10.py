import random

import win10toast
a=["Assalamualaikum","Mohammed","Abdul","Raqeeb","Arshad","sahab"]
b=win10toast.ToastNotifier()
b.show_toast(random.choice(a),random.choice(a),None,1)
