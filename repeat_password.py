password0 = 'a123456'
password1 = input('請輸入密碼: ')
count = 0
remain = 2
while True:
	if password0 == password1:
		print('登入成功')
		break
	else:
		if count < 2:
			remain = 2 - count
			print('密碼錯誤! 你還有', remain,'次機會')
			count = count + 1
			password1 = input('請輸入密碼: ')
		else:
			print('請稍後嘗試')
			break
