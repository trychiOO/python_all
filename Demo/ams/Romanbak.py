class Solution:
	def intToRoman(self, num):
		res=""
		def dealWithFive(sym1,sym5,sym10,num,res):
			if num==4:
				if res and res[-1]==sym5:
					res=res[:-1]+sym1+sym10
				else:
					res+=sym1+sym5
			else:
				res+=num*sym1
			return res

		if num==0:
			return ""
		else:
			quo,num=int(num/1000), num%1000
			res+=quo*'M'
			quo,num=int(num/500), num%500
			res+=quo*'D'
			quo,num=int(num/100), num%100
			res=dealWithFive('C','D','M',quo,res)
			quo,num=int(num/50), num%50
			res+=quo*'L'
			quo,num=int(num/10), num%10
			res=dealWithFive('X','L','C',quo,res)
			quo,num=int(num/5), num%5
			res+=quo*'V'
		return res

print(intToRoman(123))